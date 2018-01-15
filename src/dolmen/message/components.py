# -*- coding: utf-8 -*-

import crom
import uuid
from cromlech.browser import getSession
from zope.interface import implementer

from .interfaces import IMessageSource, IMessageReceiver, BASE_MESSAGE_TYPE


@crom.component_factory
@crom.sources()
@crom.target(IMessageSource)
@implementer(IMessageSource)
class SessionSource(object):
    """A message source storing messages into the session.
    """

    # Here, we explicitly re-assign the value through
    # the session __setitem__, to be sure we trigger
    # any mechanism meant to mark the session as dirty on set/remove.
    # This is not fool-proof. Improve in your own implementation
    # if needed.

    _key = u'dolmen.message.session'

    def send(self, body, type=BASE_MESSAGE_TYPE):
        session = getSession()
        if session is None:
            return False
        messages = session.get(self._key, [])
        messages.append(
            dict(body=body, type=type, id=str(uuid.uuid4().hex))
        )
        session[self._key] = messages  # Trigger
        return True

    def __call__(self):
        return self

    def __len__(self):
        session = getSession()
        return len(session.get(self._key, []))

    def __iter__(self):
        session = getSession()
        if session is None or self._key not in session:
            return iter([])
        return iter(session[self._key])

    def remove(self, item):
        session = getSession()
        if session is None:
            raise ValueError("No session")

        messages = session.get(self._key)
        if messages is None:
            raise KeyError("Session does contains messages.")

        messages.remove(item)
        session[self._key] = messages  # Trigger


@crom.adapter
@crom.sources(IMessageSource)
@crom.target(IMessageReceiver)
@implementer(IMessageReceiver)
class MessageReceiver(object):
    """A receiver that can receive from any source.
    """
    def __init__(self, context):
        self.context = context

    def receive(self, type=None):
        messages = list(self.context)  # copy as we will mutate
        for message in messages:
            if (type and message['type'] == type) or not type:
                yield message
                self.context.remove(message)
