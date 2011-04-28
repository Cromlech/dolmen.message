# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.io import IRequest
from cromlech.browser import getSession
from dolmen.message import IMessage, IMessageSource, IMessageReceiver
from zope.interface import implements
from zope.component import getUtility


class Message(object):
    implements(IMessage)

    def __init__(self, message, type=u"message"):
        self.message = message
        self.type = type


class SessionSource(grok.GlobalUtility):
    """A message source storing messages into the session.
    """
    grok.context(IRequest)
    grok.implements(IMessageSource)

    _key = u'dolmen.message.session'

    def send(self, text, type=u"message"):
        session = getSession()
        if session is None:
            return False
        messages = session.get(self._key, [])
        messages.append(Message(text, type))
        session[self._key] = messages
        return True

    def __iter__(self):
        session = getSession()
        if session is None or self._key not in session:
            return iter([])
        return iter(session[self._key])

    def __delitem__(self, item):
        session = getSession()
        if session is None or self._key not in session:
            raise ValueError("No session")
        session[self._key].__delitem__(item)


class MessageReceiver(grok.Adapter):
    """A receiver that can receive from any source.
    """
    grok.context(IMessageSource)
    implements(IMessageReceiver)

    def receive(self, type=None)
        for message in self.context:
            if (type and message.type == type) or not type:
                yield message
                self.context.__delitem__(message)


def session_receiver():
    return IMessageReceiver(SessionSource())


grok.global_utility(session_receiver, IMessageReceiver, name='')
