# -*- coding: utf-8 -*-

import pytest
import grokcore.component as grok
from cromlech.browser import setSession, getSession
from cromlech.io.testing import TestRequest
from zope.component import getUtility
from zope.testing.cleanup import cleanUp
from dolmen.message import IMessageReceiver, IMessageSource
from dolmen.message import components, utils


SESSION = {}


def setup_module(module):
    """ grok the publish module
    """
    setSession(SESSION)
    grok.testing.grok("dolmen.message.components")


def teardown_module(module):
    """ undo groking
    """
    setSession()
    cleanUp()


def test_registered_source():
    source = getUtility(IMessageSource)
    assert source.__class__ == components.SessionSource

    source.send(u'Message that is a test.')
    assert 'dolmen.message.session' in SESSION
    assert len(source) == 1

    assert ([(msg.message, msg.type) for msg in source] ==
            [(u'Message that is a test.', u'message')])

    # iterating did not pop anything
    assert len(source) == 1


def test_registered_receiver():
    source = getUtility(IMessageSource)
    receiver = IMessageReceiver(source)
    assert receiver.__class__ == components.MessageReceiver

    # Receiving will delete by default.
    messages = list(utils.receive())
    assert len(messages) ==  1
    assert len(source) == 0
