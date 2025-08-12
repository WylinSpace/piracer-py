from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

# Detected I2C addresses from i2cdetect
addresses = [0x3c, 0x40, 0x41, 0x60, 0x70]

i2c = busio.I2C(SCL, SDA)

def is_pca9685(addr):
    try:
        print(f"Testing PCA9685 at address {hex(addr)}...")
        pca = PCA9685(i2c, address=addr)
        pca.frequency = 60

        # Try toggling channels 3 and 4 (motor driver S3, S4)
        print(f"Setting channel 3 and 4 HIGH on {hex(addr)}")
        pca.channels[3].duty_cycle = 0xFFFF
        pca.channels[4].duty_cycle = 0x0000
        time.sleep(1)

        print(f"Setting channel 3 and 4 LOW on {hex(addr)}")
        pca.channels[3].duty_cycle = 0x0000
        pca.channels[4].duty_cycle = 0xFFFF
        time.sleep(1)

        # Clean up
        pca.channels[3].duty_cycle = 0x0000
        pca.channels[4].duty_cycle = 0x0000
        print(f"Done with {hex(addr)}\n")

    except Exception as e:
        print(f"Address {hex(addr)} is not a PCA9685 or failed: {e}\n")

while not i2c.try_lock():
    pass

try:
    for addr in addresses:
        is_pca9685(addr)
finally:
    i2c.unlock()
