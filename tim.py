from controller import Robot, Camera
import time
import math

robot = Robot()

elbow_left = robot.getDevice('elbow_left')
shoulder_left = robot.getDevice('shoulder_horizontal_left')

# Example: Set motor position with clamping
min_pos = 0.1  # From joint specs
max_pos = math.radians(90)  # Example max; check URDF for actual


shoulder_left.setPosition(min_pos)
# elbow_left.setPosition(max_pos)

