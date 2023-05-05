from opentap import *
from System import Double
import OpenTap
import clr
import socket
clr.AddReference("Fanuc.Api")

@attribute(OpenTap.Display("CRX-20iA/L", "Driver for Fanuc's CRX-20iA/L collaborative robot model.", "Fanuc"))
class CRX_20iA(Instrument):
    """
    CRX_20iA is a class representing a driver for the CRX_20iA collaborative robot.
    """

    robot_ip_address = property(String, "127.0.0.1")\
        .add_attribute(OpenTap.Display("Robot IP Address", "The static IP address of the robot."))

    def __init__(self):
        super(CRX_20iA, self).__init__() # The base class initializer must be invoked.
        self.Name = "CRX-20iA/L"

    def send_request_movement(self, command):
        """
        Sends a movement command to the cobot's server and waits for an acknowledgment.

        Args:
            command (str): A string containing the movement command.
        """
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))
    
        try:
            client_socket.sendall(command.encode('utf-8'))
            
            buffer_size = 2048
            acknowledgment = client_socket.recv(buffer_size).decode('utf-8')
            self.log.Info(f"Received acknowledgment: {acknowledgment!r}")

            client_socket.close()

            return acknowledgment
        
        except socket.error as e:
            self.log.Error(f"Send command failed.\nError: {e}")
            return None        
    


