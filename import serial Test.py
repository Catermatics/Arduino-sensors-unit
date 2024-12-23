#Test Sync 123
# pip install pymata4
# pip install pyserial

# Import the necessary libraries
import time
from pymata4 import pymata4
import tkinter
Top = tkinter.Tk()
Top.title("Distance Sensor test")




# Define the pins
triggerPin = 10
echo_pin = 11
pins_green = 7
num_steps=512

# Create a pymata4 instance
board = pymata4.Pymata4()

# Define the callback function
def the_callback(data):
    print("Distance: ", data[2])

# Set the pin mode
board.set_pin_mode_sonar(triggerPin, echo_pin, the_callback)
board.set_pin_mode_digital_output(pins_green)


while True:
    try:
        board.sonar_read(triggerPin)
        time.sleep(1)
    except Exception:
        board.shutdown()
        break


while True:
    print('ON')
    board.digital_write(pins_green, 1)
    time.sleep(2)
    print('OFF')
    board.digital_write(pins_green, 0)
    board.sonar_read(triggerPin)
    time.sleep(2)    
    





        


    
