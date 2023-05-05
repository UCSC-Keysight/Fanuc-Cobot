from opentap import *
from System import Double
import OpenTap
import clr
import socket
import tkinter as tk
import time
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
        self.joint_values = [0.20, 0.01, 99.57, 80.23, 97.12, 22.22]
        self.initial_position = [0.20, 0.01, 99.57, 80.23, 97.12, 22.22]
        self.target_position_command = ''

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

    def seek_target_position(self) -> str:
        """
        Launches a GUI for the user to manually adjust the cobot's joint positions and capture the 
        target position.

        Details:
            Every button press modifies related joint value, dynamically generates a formatted
            message to be sent to the KAREL server.

        Returns:
            Currently, nothing.
        """
        
        home_command = ','.join([f'{num:.2f}' for num in self.initial_position]) + ','
        self.send_request_movement(home_command)

        # Create the main window
        root = tk.Tk()
        root.title("Modify Joint Values")
        root.geometry("300x300")
        root.resizable(True, True)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True, fill=tk.BOTH)

        # Define button appearance settings
        button_bg = "light gray"
        button_fg = "black"
        button_relief = "raised"

        # Joint names
        joint_names = ["Joint1", "Joint2", "Joint3", "Joint4", "Joint5", "Joint6"]

        # Create the joint value controls
        for idx, joint_name in enumerate(joint_names):
            label = tk.Label(button_frame, text=joint_name)
            label.grid(row=idx, column=0, padx=(10, 0), pady=(10, 0), sticky='w')

            minus_button = tk.Button(button_frame, text="-", command=lambda idx=idx: self.decrement_joint(idx), width=5, height=1, bg=button_bg, fg=button_fg, relief=button_relief)
            minus_button.grid(row=idx, column=1, padx=(10, 5), pady=(10, 0))

            plus_button = tk.Button(button_frame, text="+", command=lambda idx=idx: self.increment_joint(idx), width=5, height=1, bg=button_bg, fg=button_fg, relief=button_relief)
            plus_button.grid(row=idx, column=2, padx=(5, 10), pady=(10, 0))

        # Create the Capture button
        capture_button = tk.Button(button_frame, text="Capture", command=lambda: self.capture(root), width=10, height=2, bg=button_bg, fg=button_fg, relief=button_relief)
        capture_button.grid(row=6, column=1, padx=10, pady=20)

        root.mainloop()
        return self.target_position_command


    def increment_joint(self, index):
        """
        Decrements the joint value at the given index and sends the updated joint positions to the cobot.

        Args:
            index (int): The index of the joint value to increment.
        """

        self.joint_values[index] += 1.0
        seek_command = ','.join([f'{num:.2f}' for num in self.joint_values]) + ','
        print(seek_command)
        self.send_request_movement(seek_command)


    def decrement_joint(self, index):
        """
        Decrements the joint value at the given index and sends the updated joint positions to the cobot.

        Args:
            index (int): The index of the joint value to decrement.
        """

        self.joint_values[index] -= 1.0
        seek_command = ','.join([f'{num:.2f}' for num in self.joint_values]) + ','
        print(seek_command)
        self.send_request_movement(seek_command)


    def capture(self, root):
        """
        Captures the target position command and sends the initial position command to the cobot.

        Args:
            root (tk.Tk): The root Tkinter window.
            initial (list): The initial position of the cobot.
        """

        # self.target_position_command = f"movej({self.joint_values}, v=1.0, a=1.0)\n"
        # initial_position_command = f"movej({self.initial_position}, v=1.0, a=1.0)\n"
        # print(f"Initial: {initial_position_command}, target:{self.target_position_command}")

        # # Potential bug:
        # # Caller goes out of scope before callee can finish.
        # # This needs to be handled better.
        # self.send_request_movement(initial_position_command)
        # time.sleep(5)

        root.destroy()


