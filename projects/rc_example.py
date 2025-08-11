from piracer.vehicles import PiRacerStandard
from piracer.gamepads import ShanWanGamepad

if __name__ == '__main__':

    shanwan_gamepad = ShanWanGamepad()
    # piracer = PiRacerPro() # Commented Out as not a relavant module here!
    piracer = PiRacerStandard()

    # CALIBRATION FOR SERVO STEERING
    steering_calibration = 0.72
    print("CALIBRATION COMPLETE - Value:", steering_calibration)

    # CONTROL LOGIC
    speed_multiplier = 0.5

    while True:
        gamepad_input = shanwan_gamepad.read_data()

        throttle = gamepad_input.analog_stick_left.y * speed_multiplier
        steering = gamepad_input.analog_stick_right.x + steering_calibration

        print(f'throttle={throttle}, steering={steering}')

        piracer.set_throttle_percent(throttle)
        piracer.set_steering_percent(-steering)
