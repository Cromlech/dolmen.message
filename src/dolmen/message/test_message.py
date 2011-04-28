# -*- coding: utf-8 -*-

import pytest
import grokcore.component as grok
from cromlech.browser import setSession, getSession
from cromlech.io.testing import TestRequest
from zope.component import getUtility
from zope.testing.cleanup import cleanUp
from dolmen.message import IMessagerReceiver, IMessageSource


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
    print source
