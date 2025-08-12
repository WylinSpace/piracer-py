from piracer.vehicles import PiRacerStandard
from piracer.gamepads import ShanWanGamepad
import time

if __name__ == '__main__':
    shanwan_gamepad = ShanWanGamepad()
    piracer = PiRacerStandard()

    # CALIBRATION FOR SERVO STEERING
    steering_calibration = 0.72
    print("CALIBRATION COMPLETE - Value:", steering_calibration)

    # CONTROL LOGIC
    speed_multiplier = 0.5

    # Prevent multiple increments per button press
    prev_button_a_state = False

    while True:
        gamepad_input = shanwan_gamepad.read_data()

        throttle = gamepad_input.analog_stick_right.y * speed_multiplier
        steering = gamepad_input.analog_stick_left.x + steering_calibration

        print(f'Throttle = {throttle:.2f}, Steering = {steering:.2f}')

        piracer.set_throttle_percent(throttle)
        piracer.set_steering_percent(-steering)

        # Debounced A button to increase speed
        if gamepad_input.button_a and not prev_button_a_state:
            speed_multiplier = min(speed_multiplier + 0.05, 1.0)  # max cap at 1.0
            print("Increased Speed Multiplier:", speed_multiplier)
        prev_button_a_state = gamepad_input.button_a

        time.sleep(0.05)  # Slight delay to reduce CPU load
