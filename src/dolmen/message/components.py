# -*- coding: utf-8 -*-
import crom
from cromlech.browser import getSession
from zope.interface import implementer

from .interfaces import (
    IMessage, IMessageSource, IMessageReceiver, BASE_MESSAGE_TYPE)


@implementer(IMessage)
class Message(object):

    def __init__(self, message, type=BASE_MESSAGE_TYPE):
        self.message = message
        self.type = type


@crom.component_factory
@crom.sources()
@crom.target(IMessageSource)
@implementer(IMessageSource)
class SessionSource(object):
    """A message source storing messages into the session.
    """

    _key = u'dolmen.message.session'

    def send(self, text, type=BASE_MESSAGE_TYPE):
        session = getSession()
        if session is None:
            return False
        messages = session.get(self._key, [])
        messages.append(Message(text, type))
        session[self._key] = messages
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
        if session is None or self._key not in session:
            raise ValueError("No session")
        session[self._key].remove(item)


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
            if (type and message.type == type) or not type:
                yield message
                self.context.remove(message)
