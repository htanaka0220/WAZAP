#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
ST7032i LCD driver control library
"""

import wiringpi as wp
import time

I2C_ADDR = 0x3e

class St7032iLCD:
    """
    ST7032i LCD control class
    """
    def __init__(self, i2c_addr = I2C_ADDR):
        self.i2c = wp.I2C()
        self.fd = self.i2c.setup(i2c_addr)
        self._init()

    def _init(self):
        self.write_instruction(0x38) # function set: 8 bit, 2 line
        self.write_instruction(0x39) # function set: 8 bit, 2 line, IS=1
        self.write_instruction(0x14) # internal OSC freq
        self.write_instruction(0x70) # contrast set
        self.write_instruction(0x56) # Power/ICON/Constrast
        self.write_instruction(0x6c) # Follower control
        time.sleep(0.2)             # wait time > 200 ms
        self.write_instruction(0x38) # function set: 8 bit, 2 line, IS=0
        self.write_instruction(0x06) # Entry mode set
        self.write_instruction(0x0c) # Display on/off
        self.write_instruction(0x01) # Clear display
        time.sleep(0.01)             # wait time > 1.08 ms
        self.write_instruction(0x02) # return home
        time.sleep(0.01)             # wait time > 1.08 ms

    def _write(self, control, data):
         self.i2c.writeReg8(self.fd, control, data)

    def write_instruction(self, data):
        """ Send Instruction code. """
        self._write(0x00, data)

    def write_data(self, data):
        """ Send data into data register. """
        self._write(0x40, data)

    def clear(self):
        """ Clear display and return to home position. """
        self.write_instruction(0x01) # clear display
        time.sleep(0.01)             # wait time > 1.08 ms
        self.write_instruction(0x02) # return home
        time.sleep(0.01)             # wait time > 1.08 ms

    def return_home(self):
        """ return to home """
        self.write_instruction(0x02) # return home
        time.sleep(0.01)             # wait time > 1.08 ms

    def set_contrast(self, contrast):
        """ Set contrast (0 - 15). """
        if contrast < 0:
            contrast = 0
        if contrast > 0x0f:
            contrast = 0x0f
        self.write_instruction(0x39)
        self.write_instruction(0x70 + contrast)

    def set_cursor(self, x, y):
        """ set cursor location (address counter)."""
        if x < 0: x = 0
        if y < 0: y = 0
        ddram_addr = y * 0x40 + x
        self.write_instruction(0x80 + ddram_addr) # set DDRAM address

    def set_entry_mode(self, increment, shift):
        mode = 0x04
        if (increment): mode = mode + 2
        if (shift): mode = mode + 1
        self.write_instruction(mode)

    def print(self, str, wait = 0):
        for c in str:
            self.write_data(ord(c))
            if (wait > 0): time.sleep(wait)

if __name__ == '__main__':
    lcd = St7032iLCD(I2C_ADDR)

    # show characters in 2 lines
    lcd.set_cursor(0, 0)
    lcd.print('1234')
    lcd.set_cursor(4, 1)
    lcd.print('5678')

    # LCD clear
    time.sleep(2)
    lcd.clear()

    # ticker
    lcd.set_entry_mode(True, True)
    lcd.set_cursor(8, 0)
    lcd.print('Hello, this is a ticker message.', 0.5)
