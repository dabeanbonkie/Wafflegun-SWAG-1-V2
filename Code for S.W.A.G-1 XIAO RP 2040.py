
from machine import Pin, PWM
from time import sleep
#Do I need to change the pins to fit the new board?
servo_pin = machine.Pin(27) #Xiao RP2040 Pin, Pico pin = 2
servo = PWM(servo_pin)
#button for servo
button = Pin(28, Pin.IN, Pin.PULL_DOWN) #Xiao RP2040 Pin, Pico pin = 3
motor_pin = Pin(26, Pin.OUT, value=0) #Xiao RP2040 Pin, Pico pin = 1
motor_button = Pin(29, Pin.IN, Pin.PULL_DOWN)  #Xiao RP2040 Pin, Pico pin = 5
max_duty = 8192
min_duty = 1638
frequency = 50
servo.freq(frequency)

print("before loop/hello world")

try:
    while True:
        if motor_button.value() == 1:
            print("button pressed motor")
            motor_pin.on()
            sleep(1)
            motor_pin.off()
        if button.value() == 1:
            print("button pressed servo")
            servo.duty_u16(min_duty)
            sleep(2)
            servo.duty_u16(max_duty)
            sleep(2)
        sleep(0.01)
        
       
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    servo.deinit()
   

