import Beaker

from cromlech.io import IRequest
import grokcore.component as grok
from grokcore.message import IMessageSource, IMessageReceiver

class BeakerSource(grok.Adapter, list):
    """
    A message source storing messages to the beaker session
    """
    grok.context(IRequest)
    grok.implements(IMessageSource)

    def send(self, message, type=u"message"):
        
