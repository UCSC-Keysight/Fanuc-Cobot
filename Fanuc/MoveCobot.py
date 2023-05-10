from OpenTap import Display
from opentap import *
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


    def __init__(self):
        super(MoveCobot, self).__init__()
    
    def Run(self):

        command = ''
        for i in range(1, 7):
            joint_value = getattr(self, f'joint{i}')
            command += f'{joint_value},'
        
        self.cobot.send_request_movement(command)
   