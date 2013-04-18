# -*- coding: utf-8 -*-
from . import IMessageSource, IMessageReceiver, BASE_MESSAGE_TYPE


def send(message, type=BASE_MESSAGE_TYPE, name=''):
    """Adds a short message to a given source.

    If the message has been sent with success, True is returned.
    Otherwise, False is returned.
    """
    source = IMessageSource.component(name=name)
    if source is None:
        return False
    source.send(message, type)
    return True


def get_from_source(name=''):
    """List messages from a given source.

    If the received has been found with success, a list
    of messages is returned. Otherwise, False is returned.
    """
    source = IMessageSource.component(name=name)
    if source is None:
        return None
    return list(source)


def receive(name='', type=BASE_MESSAGE_TYPE):
    """Receives messages from a given receiver.

    If the received has been found with success, an iterable
    of messages is returned. Otherwise, None is returned.
    """
    source = IMessageSource.component(name=name)
    if source is None:
        return None
    receiver = IMessageReceiver(source)
    if receiver is None:
        return None
    return receiver.receive(type)
