# Example code. Do with it what you like.
# no rights reserved.

from opentap import *
from System import Double
import OpenTap
import clr
import socket
clr.AddReference("Fanuc.Api")

@attribute(OpenTap.Display("CRX-20iA/L", "Driver for Fanuc's CRX-20iA/L collaborative robot model.", "Fanuc"))
class CRX_20iA(Instrument):

    robot_ip_address = property(String, "127.0.0.1")\
        .add_attribute(OpenTap.Display("Robot IP Address", "The static IP address of the robot."))
    def __init__(self):
        super(CRX_20iA, self).__init__() # The base class initializer must be invoked.
        self.name = "CRX-20iA/L"
        
    @method(Double)
    def send_message(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.robot_ip_address, 12345))

        message = "Hello World"

        client_socket.sendall(message.encode('utf-8'))
        client_socket.close()
        
        print("Message sent.")

