from piracer.gamepads import ShanWanGamepad

if __name__ == "__main__":
    gamepad = ShanWanGamepad()

    while True:
        gamepad_input = gamepad.read_data()
        print(gamepad_input)
        break
