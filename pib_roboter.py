"""my_controllerRobot controller."""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Camera
import time

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
# Get the total number of devices

device_count = robot.getNumberOfDevices()

# Loop through all devices and print their names and types
for i in range(device_count):
    m = robot.getDeviceByIndex(i)
try:
    m.setPosition(1.0)
except Exception as e:
    print(e)
    pass

def moveDigits(digits, position):
    for digit in digits:
        digit.setPosition(position)

def closeDigitsTimed(digits, sleepTime):
    position=0.0
    while position<=3.4:
        for digit in digits:
            digit.setPosition(position)
        position=position+0.1
        time.sleep(sleepTime)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
thumb_left_p = robot.getDevice('thumb_left_proximal')
index_left_p = robot.getDevice('index_left_proximal')
middle_left_p = robot.getDevice('middle_left_proximal')
ring_left_p = robot.getDevice('ring_left_proximal')
pinky_left_p = robot.getDevice('pinky_left_proximal')
#motor4= robot.getDevice('ring_left_distal')

moveDigits([thumb_left_p,index_left_p,middle_left_p,ring_left_p,pinky_left_p], 0.0)

thumb_left_d = robot.getDevice('thumb_left_distal')
index_left_d = robot.getDevice('index_left_distal')
middle_left_d = robot.getDevice('middle_left_distal')
ring_left_d = robot.getDevice('ring_left_distal')
pinky_left_d = robot.getDevice('pinky_left_distal')
#motor4= robot.getDevice('ring_left_distal')

moveDigits([thumb_left_d,index_left_d,middle_left_d,ring_left_d,pinky_left_d], 0.0)

# - perform simulation steps until Webots is stopping the controller
while True:
    t = robot.step(timestep)
    if t == -1:
        break
    closeDigitsTimed([thumb_left_p,index_left_p,middle_left_p,ring_left_p,pinky_left_p,
                 thumb_left_d,index_left_d,middle_left_d,ring_left_d,pinky_left_d], 0.2)

# Enter here exit cleanup code.