from controller import Robot, Camera
import time
import math

robot = Robot()

#Armgelenke initialisieren
elbow_right = robot.getDevice('elbow_right')
shoulder_h_right = robot.getDevice('shoulder_horizontal_right')
shoulder_v_right = robot.getDevice('shoulder_vertical_right')
upper_arm_right = robot.getDevice('upper_arm_right')

# Daumen initialisieren
thumb_right_o = robot.getDevice('thumb_right_opposition')
thumb_right_p = robot.getDevice('thumb_right_proximal')
thumb_right_d = robot.getDevice('thumb_right_distal')

# Zeigefinger initialisieren
index_right_p = robot.getDevice('index_right_proximal')
index_right_d = robot.getDevice('index_right_distal')

#Mittelfinger initialisieren
middle_right_p = robot.getDevice('middle_right_proximal')
middle_right_d = robot.getDevice('middle_right_distal')

# Ringfinger initialisieren
ring_right_p = robot.getDevice('ring_right_proximal')
ring_right_d = robot.getDevice('ring_right_distal')

# Kleiner Finger initialisieren
pinky_right_p = robot.getDevice('pinky_right_proximal')
pinky_right_d = robot.getDevice('pinky_right_distal')

start_pos_v_shoulder = math.radians(-90)  
start_pos_h_shoulder = math.radians(90)
start_pos_elbow = math.radians(45)
start_pos_finger = math.radians(90)

#shoulder_h_right.setPosition(max_pos)
shoulder_v_right.setPosition(start_pos_v_shoulder)
shoulder_h_right.setPosition(start_pos_h_shoulder)

elbow_right.setPosition(start_pos_elbow)

thumb_right_p.setPosition(start_pos_finger)
thumb_right_d.setPosition(start_pos_finger)
thumb_right_o.setPosition(start_pos_finger)

index_right_d.setPosition(start_pos_finger)
index_right_p.setPosition(start_pos_finger)

middle_right_p.setPosition(start_pos_finger)
middle_right_d.setPosition(start_pos_finger)

ring_right_p.setPosition(start_pos_finger)
ring_right_d.setPosition(start_pos_finger)

pinky_right_p.setPosition(start_pos_finger)
pinky_right_d.setPosition(start_pos_finger)