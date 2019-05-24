# openlabs

Connect the SHA2017 badge

screen /dev/ttyUSB0 115200

CTRL+C (if the openlabs app is running)

CTRL+A k (kill the screen!)

ampy -p /dev/ttyUSB0 put openlabs.py /lib/openlabs/__init__.py

remove the USB, plug it back in to the power again
