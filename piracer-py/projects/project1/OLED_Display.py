import time
import board
import busio
from digitalio import DigitalInOut
import adafruit_ssd1306
import socket
import subprocess
from adafruit_ina219 import INA219
from PIL import Image, ImageDraw, ImageFont

# I2C Setup
i2c = busio.I2C(board.SCL, board.SDA)

# OLED Setup
WIDTH = 128
HEIGHT = 32
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)
oled.show()

# INA219 setup
ina219 = INA219(i2c)

# Load 8px font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)

def get_ip():
    try:
        return subprocess.check_output("hostname -I", shell=True).decode().split()[0]
    except:
        return "No IP"

def get_wifi():
    try:
        return subprocess.check_output("iwgetid -r", shell=True).decode().strip()
    except:
        return "No WiFi"

def get_battery():
    voltage = ina219.bus_voltage
    current = ina219.current
    return voltage, current

def display_lines(lines):
    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    for i, line in enumerate(lines):
        draw.text((0, i * 8), line, font=font, fill=255)
    oled.image(image)
    oled.show()

# Main loop
while True:
    # Show Battery Info
    voltage, current = get_battery()
    now = time.strftime("%H:%M:%S")
    date = time.strftime("%d-%b")
    display_lines([
        f"{date}  {now}",
        f"Voltage: {voltage:.2f}V",
        f"Current: {current:.1f}mA",
    ])
    time.sleep(9)

    # Show WiFi Info
    wifi = get_wifi()
    ip = get_ip()
    display_lines([
        f"WiFi: {wifi}",
        f"IP: {ip}",
    ])
    time.sleep(9)
