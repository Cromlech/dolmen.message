# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.schema import TextLine

BASE_MESSAGE_TYPE = u'message'


class IMessageSource(Interface):
    """A component that sends and stores messages.
    """

    def send(text, type=u"message"):
        """Sends a message.
        """

    def __len__():
        """Returns the number of existing messages.
        """

    def __iter__():
        """Iterates over existing messages.
        """

    def remove(message):
        """Removes a message.
        """


class IMessageReceiver(Interface):
    """A component that receives messages.
    """

    def receive(type=None):
        """Return all messages of the given type relevant to the current
        request.
        """
