import time
from smbus2 import SMBus
from bme280 import BME280

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

# Test Temperature, Pressure, and Humidity
print(bme280.get_temperature())
print(bme280.get_pressure())
print(bme280.get_humidity())
