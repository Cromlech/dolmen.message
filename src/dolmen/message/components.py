# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.io import IRequest
from cromlech.browser import getSession
from dolmen.message import IMessage, IMessageSource, IMessageReceiver
from zope.interface import implements
from zope.component import getUtility


BASE_MESSAGE_TYPE = u'message'


class Message(object):
    implements(IMessage)

    def __init__(self, message, type=BASE_MESSAGE_TYPE):
        self.message = message
        self.type = type


class SessionSource(grok.GlobalUtility):
    """A message source storing messages into the session.
    """
    grok.context(IRequest)
    grok.implements(IMessageSource)

    _key = u'dolmen.message.session'

    def send(self, text, type=BASE_MESSAGE_TYPE):
        session = getSession()
        if session is None:
            return False
        messages = session.get(self._key, [])
        messages.append(Message(text, type))
        session[self._key] = messages
        return True

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


class MessageReceiver(grok.Adapter):
    """A receiver that can receive from any source.
    """
    grok.context(IMessageSource)
    implements(IMessageReceiver)

    def receive(self, type=None):
        for message in self.context:
            if (type and message.type == type) or not type:
                yield message
                self.context.remove(message)
