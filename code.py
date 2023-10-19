import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

Left_motor_forward = board.GP12
left_motor_backward = board.GP13
right_motor_forward = board.GP9
right_motor_backward = board.GP10


Left_motor_forward = pwmio.PWMOut(Left_motor_forward, frequency=10000)
left_motor_backward = pwmio.PWMOut(left_motor_backward, frequency=10000)
right_motor_forward = pwmio.PWMOut(right_motor_forward, frequency=10000)
right_motor_backward = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(Left_motor_forward, left_motor_backward)
Left_Motor_speed = 0
right_Motor = motor.DCMotor(right_motor_forward, right_motor_backward)
right_Motor_speed = 0
while True:
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
    right_Motor_speed = -1
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)




'''
#robot backward
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
    right_Motor_speed = 1
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)

#Robot forward
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
    right_Motor_speed = -1
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)

#Left motor forward
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
#left motor backward
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
#right motor forward
    right_Motor_speed = -1
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)
#right motor backward
    right_Motor_speed = 1
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)

'''
