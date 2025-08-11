from piracer.gamepads import ShanWanGamepad
import time
import os

def format_bool(val):
    return "ON" if val else "OFF"

def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

if __name__ == '__main__':
    
    shanwan_gamepad = ShanWanGamepad()

    while True:

        gamepad_input = shanwan_gamepad.read_data()


        print("ShanWan Gamepad State")
        print("=========================")

        print("Left Stick:")
        print(f"  X: {gamepad_input.analog_stick_left.x:+.3f}")
        print(f"  Y: {gamepad_input.analog_stick_left.y:+.3f}")

        print("Right Stick:")
        print(f"  X: {gamepad_input.analog_stick_right.x:+.3f}")
        print(f"  Y: {gamepad_input.analog_stick_right.y:+.3f}")

        print("Buttons:")
        #print(f"  A: {gamepad_input.button_a}")
        #print(f"  B: {gamepad_input.button_b}")
        #print(f"  X: {gamepad_input.button_x}")
        #print(f"  Y: {gamepad_input.button_y}")

        time.sleep(0.1)
