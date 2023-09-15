# sdr-keys alpha
 HID and MIDI Programable Keys for SDR Tactical Control

 ![img](/img/adakbd.jpeg)
 
 Built on RP2040 using Adafruit MacroPad running [CircutPython](https://learn.adafruit.com/adafruit-macropad-rp2040) with offical [Library-Pack](https://learn.adafruit.com/adafruit-macropad-rp2040/macropad-circuitpython-library)

 # use / install
The code is very early alpha nothing fancy

 1) once device is built and running circuit python (See errata)
 2) download and copy the lib pack above
 3) copy code.py to CIRCUITPY disk with step 2 lib directory

# adding more whatever..
- [breakout](https://learn.adafruit.com/adafruit-macropad-rp2040/attaching-external-hardware) devices details
  - add an additional higher resolution or weighty VFO knob! 
  - foot switch for PTT
  - IR Control

# Errata
 - [Adafruit Downloads](https://learn.adafruit.com/adafruit-macropad-rp2040/downloads) for Scats etc.
 - [MIDI-API](https://docs.circuitpython.org/projects/midi/en/latest/)
    - [UART-MIDI](https://projectgus.github.io/hairless-midiserial/)
 - [HID-API](https://docs.circuitpython.org/projects/macropad/en/latest/api.html)
 - [IR-API](https://learn.adafruit.com/ir-sensor/circuitpython)