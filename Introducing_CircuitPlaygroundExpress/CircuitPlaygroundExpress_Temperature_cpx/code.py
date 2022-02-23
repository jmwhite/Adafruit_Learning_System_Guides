# SPDX-FileCopyrightText: 2017 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

from adafruit_circuitplayground.express import cpx

while True:
    print(cpx.temperature)
    time.sleep(0.5)
