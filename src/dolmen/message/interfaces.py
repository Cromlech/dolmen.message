# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute
from zope.schema import TextLine


class IMessage(Interface):
    """A message that can be displayed to the user.
    """
    message = TextLine(
        title=u"The message itself.")
    
    type = TextLine(
        title=u"A classifier for the message",
        default=u"message")


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
