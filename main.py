import time
from smbus2 import SMBus
from bme280 import BME280
from ltr559 import LTR559
from enviroplus import gas
import st7735
from PIL import Image, ImageDraw, ImageFont

# Define sensors

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
ltr = LTR559()

# Define Screen

disp = st7735.ST7735(
    port=0,
    cs=1,
    dc="GPIO9",
    backlight="GPIO12",
    rotation=270,
    spi_speed_hz=10000000
)


# Read gas levels from MICS6814 Module
def gasRead():
    while True:
        readings = gas.read_all()
        print(readings)
        time.sleep(1.0)

# Test Temperature, Pressure, Humidity, Gas Levels
print(bme280.get_temperature())
print(bme280.get_pressure())
print(bme280.get_humidity())
print(gasRead())
