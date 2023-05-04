from opentap import *
from .CRX_20iA import CRX_20iA
from System import Int32
import OpenTap

@attribute(OpenTap.Display("Send Message", "Sends a TCP/IP message to the CRX-20iA/L controller unit.", "Fanuc"))
class Send_Message (TestStep):
   
    robot = property(CRX_20iA, None).\
        add_attribute(OpenTap.Display("Instrument", "The instrument to use in the step.", "Resources"))
    
    def __init__(self):
        super(Send_Message, self).__init__()
    
    def Run(self):
    
        self.robot.send_message()
   