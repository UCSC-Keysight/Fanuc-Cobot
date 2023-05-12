from opentap import *
from OpenTap import *
from System import String, Int32
import socket
import clr

clr.AddReference("Fanuc.Api")

@attribute(OpenTap.Display("CRX-20iA/L", "Driver for Fanuc's CRX-20iA/L collaborative robot model.", "Fanuc"))
class CRX_20iA(Instrument):

    robot_ip_address = property(String, "127.0.0.1")\
        .add_attribute(OpenTap.Display("Robot IP Address", "The static IP address of the robot."))
    robot_port = property(Int32, 12345)\
        .add_attribute(OpenTap.Display("Robot Port", "The port used by the robot's server."))


    def __init__(self):
        super(CRX_20iA, self).__init__()
        self.Name = "CRX-20iA/L"

    def send_request_movement(self, command):
        """
        Sends a movement command to the cobot's server and waits for an acknowledgment.

        Args:
            command (str): A string containing the movement command.

        Returns:
            str: A string containing the response message from server.
        """

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5) 
        
        try:
            client_socket.connect((self.robot_ip_address, self.robot_port))
        except (socket.timeout, socket.error) as e:
            self.log.Error(f"Connection failed.\nError: {e}")
            client_socket.close()
            return f"Error: {e}"

        try:
            client_socket.sendall(command.encode('utf-8'))
        except socket.error as e:
            self.log.Error(f"Send command failed.\nError: {e}")
            client_socket.close()
            return f"Error: {e}"

        buffer_size = 2048
        try:
            acknowledgment = client_socket.recv(buffer_size).decode('utf-8')
            self.log.Info(f"Received acknowledgment: {acknowledgment!r}")
        except (socket.timeout, socket.error) as e:
            self.log.Error(f"Receive acknowledgment failed.\nError: {e}")
            client_socket.close()
            return f"Error: {e}"

        client_socket.close()

        return acknowledgment