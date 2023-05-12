from opentap import *
from OpenTap import Display
from .CRX_20iA import CRX_20iA
from System import String

@attribute(OpenTap.Display("Move Cobot", "Moves collaborative robot to specified location.", "Fanuc"))
class MoveCobot (TestStep):
   
    cobot = property(CRX_20iA, None).\
        add_attribute(OpenTap.Display("Instrument", "The instrument to use in the step.", "Resources"))
    joint1 = property(String, "88.29")\
        .add_attribute(Display("joint1", "Position of joint1", "Joints", -1, True))
    joint2 = property(String, "23.10")\
        .add_attribute(Display("joint2", "Position of joint2", "Joints", -1, True))
    joint3 = property(String, "66.87")\
        .add_attribute(Display("joint3", "Position of joint3", "Joints", -1, True))
    joint4 = property(String, "100.29")\
        .add_attribute(Display("joint4", "Position of joint4", "Joints", -1, True))
    joint5 = property(String, "52.12")\
        .add_attribute(Display("joint5", "Position of joint5", "Joints", -1, True))
    joint6 = property(String, "38.22")\
        .add_attribute(Display("joint6", "Position of joint6", "Joints", -1, True))
    Mode = property(String, "Seek Mode")\
        .add_attribute(OpenTap.AvailableValues("Available"))\
        .add_attribute(OpenTap.Display("Mode", "Values from Available Values can be selected here.", "Mode"))
    Available = property(List[String], None)\
        .add_attribute(OpenTap.Display("Available Values", "Select which values are available for 'Mode'.", "Mode"))


    def __init__(self):
        super(MoveCobot, self).__init__()
        self.Available = List[String]()
        self.Available.Add("Seek Mode")
        self.Available.Add("Manual Mode")
    
    def Run(self):

        command = ''
        if self.Mode == "Seek Mode":
            self.cobot.seek_target_position()
        elif self.Mode == "Manual Mode":
            
            # Prepare move message with user inputs.
            for i in range(1, 7):
                joint_value = getattr(self, f'joint{i}')
                command += f'{joint_value},'
            
            print(command)
            self.cobot.seek_target_position()
        

        
   