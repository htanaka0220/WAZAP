# coding: utf-8
## @package FaBoProximity_VCNL4010
#  This is a library for the FaBo Proximity I2C Brick.
#
#  http://fabo.io/205.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoProximity_VCNL4010
import time
import sys
import smbus

vcnl4010 = FaBoProximity_VCNL4010.VCNL4010()

try:
    while True:
        prox = vcnl4010.readProx()
        ambi = vcnl4010.readAmbi()

        print("Prox = ", str(prox))
        print("Ambi = ", str(ambi))

        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
