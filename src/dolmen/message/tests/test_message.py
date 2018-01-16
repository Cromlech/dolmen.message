# -*- coding: utf-8 -*-

import uuid
import pytest
import grokcore.component as grok
from cromlech.browser import setSession
from zope.component import getUtility
from zope.testing.cleanup import cleanUp
from dolmen.message import IMessageReceiver, IMessageSource
from dolmen.message import components, utils, BASE_MESSAGE_TYPE


SESSION = {}


@pytest.fixture
def mocked_uuid(mocker):
    mock_uuid = mocker.patch.object(uuid, 'uuid4', autospec=True)
    mock_uuid.return_value = uuid.UUID(hex='2abc74bdfd784bf5ba81e9d79d2a9f21')
    return mock_uuid


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


def test_registered_source_receiver(mocked_uuid):
    source = getUtility(IMessageSource)
    assert source.__class__ == components.SessionSource

    source.send(u'Message that is a test.')
    assert 'dolmen.message.session' in SESSION
    assert len(source) == 1

    assert [msg for msg in source] == [{
        'message': u'Message that is a test.',
        'type': u'message',
        'uid': '2abc74bdfd784bf5ba81e9d79d2a9f21',
    }]

    # iterating did not pop anything
    assert len(source) == 1

    # a receiver can be fetched through adapation of the source.
    receiver = IMessageReceiver(source)
    assert receiver.__class__ == components.MessageReceiver

    # Receiving will delete by default.
    messages = list(receiver.receive())
    assert len(messages) == 1
    assert len(source) == 0
    assert messages[0]['type'] == BASE_MESSAGE_TYPE


def test_send_receive():
    utils.send('Something')

    messages = utils.receive('nothing')
    assert messages == None

    messages = list(utils.receive())
    assert len(messages) == 1
    assert messages[0]['type'] == BASE_MESSAGE_TYPE


def test_send_receive_type():
    result = utils.send('Something', type='error')
    assert result == True

    messages = list(utils.receive(type='nothing'))
    assert len(messages) == 0

    messages = list(utils.receive())
    assert len(messages) == 0

    messages = list(utils.receive(type='error'))
    assert len(messages) == 1


def test_send_receive_failing_name():
    messages = utils.receive(name='unexisting')
    assert messages == None

    result = utils.send('Some message', name='unexisting')
    assert result == False


def test_send_receive_some():
    """verify we get all message if there are some"""
    utils.send('Tomorrow, and tomorrow, and tomorrow,')
    utils.send('Creeps in this petty pace from day to day,')
    utils.send('To the last syllable of recorded time;')
    utils.send('And all our yesterdays have lighted fools')
    utils.send('The way to dusty death. Out, out, brief candle!')

    messages = list(utils.receive())
    assert len(messages) == 5
