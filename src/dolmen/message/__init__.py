# -*- coding: utf-8 -*-

from dolmen.message.interfaces import (
    IMessageSource, IMessageReceiver, BASE_MESSAGE_TYPE)

from dolmen.message.components import SessionSource, MessageReceiver
from dolmen.message.utils import send, get_from_source, receive
