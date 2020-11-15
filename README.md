# coop3
Automated Chicken Coop Door and Lights using a Raspberry Pi 3 B

Setup the Raspberry Pi 3 B per 
[this tutorial](https://jethornton.github.io/rpi/install-10D.html)

Copy `__init__.py, coop3, coop3.ui, and rpi_utilities.py` to your local bin directory.
Make sure coop3 is executable, right click on it in the file manager and select
properties.

Additional notes are in the coop3 file.

LED is driven with a mosfet driver connected to the Raspberry Pi.
I used the following items:

[Mosfet Driver](https://www.amazon.com/gp/product/B07GLNCRR4)

[6500K LED](https://www.ledsupply.com/leds/12v-led-light-nichia-757)

[Mean Well Power Supply](https://www.ledsupply.com/power-supplies/mean-well-lpf-series-constant-voltage-constant-current-output)

led-test is a simple test to see if you have the led wired up correctly to the
PWM driver.

sun-led simulates sunrise then sunset in an accelerated to 30 seconds each.
