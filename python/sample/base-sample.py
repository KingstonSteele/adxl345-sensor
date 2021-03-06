#!/usr/bin/env python

# This sample print acceleration value on all 3 axes every second 

import time
from adxl345.i2c import ADXL345

def main():
  # Build the I2C implementation of the driver. It expect two arguments
  #   port: the I2C bus to use
  #   alternate: must reflect if the pin SDO/ALT_ADDRESS is high or low
  adxl = ADXL345(port=1, alternate=True)

  # Print device ID
  deviceId = adxl.get_device_id()
  print("ADXL DeviceID: " + str(deviceId))

  # Set data rate at about 8 hz
  rate_hz = adxl.set_data_rate(8, 1)
  print("Rate: " + str(rate_hz) + " hz")

  # Select Range
  adxl.set_range(16, True)
  
  # Turn off sleep mode (default when powered)
  adxl.power_on()

  # Indefinitely print acceleration measures
  print("Press CTRL-C to stop")
  while True:
    val = adxl.get_axes()
    print("X,Y,Z: " + str(val))
    time.sleep(1)
    
main()
