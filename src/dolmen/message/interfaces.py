# -*- coding: utf-8 -*-

import zope.interface
import zope.schema


class IMessage(zope.interface.Interface):
    """A message that can be displayed to the user."""

    message = zope.schema.TextLine(title=u"The message itself.")

    type = zope.schema.TextLine(title=u"A classifier for the message",
                                default=u"message")


class IMessageSource(zope.interface.Interface):

    def send(message, type=u"message"):
        """Send a message to this source.

        Message can either be a unicode string or an IMessage object.
        """
    
    def __iter__():
        """iter over sent message"""

    def __delitem__(message):
        """remove message"""


class IMessageReceiver(zope.interface.Interface):
    """Receive messages.

    Depending on the implementation, this receives messages from various
    sources.
    """

    def receive(type=None):
        """Return all messages of the given type relevant to the current
        request.
        """
