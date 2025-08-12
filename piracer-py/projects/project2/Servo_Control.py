from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

# I2C setup
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=0x40)  # or 0x41 if needed
pca.frequency = 50  # For motor or servo

# Example: Set channel 0 to some duty cycle (speed)
pca.channels[3].duty_cycle = 0x7FFF  # 50% speed

time.sleep(2)
pca.channels[3].duty_cycle = 0x0000  # Stop
