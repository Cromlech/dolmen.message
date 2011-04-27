# -*- coding: utf-8 -*-

from zope.component import queryUtility
from grokcore.message import IMessageSource, IMessageReceiver


def send(message, type='message', name='session'):
    """Adds a short message to a given source.

    If the message has been sent with success, True is returned.
    Otherwise, False is returned.
    """
    source = queryUtility(IMessageSource, name=name)
    if source is None:
        return False
    source.send(message, type)
    return True


def get_from_source(name=''):
    """List messages from a given source.

    If the received has been found with success, a list
    of messages is returned. Otherwise, False is returned.
    """
    source = queryUtility(IMessageSource, name=name)
    if source is None:
        return None
    return list(source)


def receive(name=''):
    """Receives messages from a given receiver.

    If the received has been found with success, an iterable
    of messages is returned. Otherwise, None is returned.
    """
    receiver = queryUtility(IMessageReceiver, name=name)
    if receiver is None:
        return None
    return receiver.receive()
