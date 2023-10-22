# SPDX-FileCopyrightText: 2021 ladyada & Kattni Rembor for Adafruit Industries
# sdr-keys: 2023 K7MHI

# Setup:
MYCALL = "K7MHI"

# Lets Gooooooo!
from adafruit_macropad import MacroPad
import time

#define objects and variables
macropad = MacroPad() # Create the macropad object
last_position = 0 # Rotary Encoder Position

"""Quad I2C rotary encoder."""
import board
import digitalio
import adafruit_seesaw.seesaw
import adafruit_seesaw.rotaryio
import adafruit_seesaw.digitalio

# For boards/chips that don't handle clock-stretching well, try running I2C at 50KHz
# import busio
# i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
# For using the built-in STEMMA QT connector on a microcontroller
i2c = board.STEMMA_I2C()
seesaw = adafruit_seesaw.seesaw.Seesaw(i2c, 0x49)

encoders = [adafruit_seesaw.rotaryio.IncrementalEncoder(seesaw, n) for n in range(4)]
switches = [adafruit_seesaw.digitalio.DigitalIO(seesaw, pin) for pin in (12, 14, 17, 9)]
for switch in switches:
    switch.switch_to_input(digitalio.Pull.UP)  # input & pullup!

encoders = [adafruit_seesaw.rotaryio.IncrementalEncoder(seesaw, n) for n in range(4)]
switches = [adafruit_seesaw.digitalio.DigitalIO(seesaw, pin) for pin in (12, 14, 17, 9)]
for switch in switches:
    switch.switch_to_input(digitalio.Pull.UP)  # input & pullup!
    
last_positions = [-1, -1, -1, -1]

print("SDR Keys v0.2")

while True:
    key_event = macropad.keys.events.get() # Get the key event
    macropad.encoder_switch_debounced.update() # Update the rotary encoder button state
    current_position = macropad.encoder # Get the current rotary encoder position

    if key_event:
        if key_event.pressed:
            mykey_timer = key_event.timestamp # Get the key change time
            if key_event.key_number < 12: # No pixel for encoder button
                macropad.pixels[key_event.key_number] = 0xFFFFFF
                macropad.pixels.show()

            # Top Row Keyboard Event Keys
            if key_event.key_number == 0:
                macropad.keyboard.press(macropad.Keycode.G)

            if key_event.key_number == 2:
                macropad.keyboard.press(macropad.Keycode.T)
                
            if key_event.key_number == 3:
                macropad.keyboard.press(macropad.Keycode.F)

            if key_event.key_number == 5:
                macropad.keyboard.press(macropad.Keycode.R)

            if key_event.key_number == 6:
                macropad.keyboard.press(macropad.Keycode.D)

            if key_event.key_number == 8:
                macropad.keyboard.press(macropad.Keycode.E)

            # Three Bottom Keys Using Keyboard Functions for theitus
            if key_event.key_number == 9:
                macropad.keyboard.press(macropad.Keycode.V)

            if key_event.key_number == 11:
                macropad.keyboard.press(macropad.Keycode.B)

            if key_event.key_number == 10:
                macropad.midi.send(macropad.NoteOn(22, 127))
                time.sleep(0.5)
                macropad.midi.send(macropad.NoteOff(22, 0))
                time.sleep(0.5)
                
            # # Three Bottom Keys Using Media Functions
            # if key_event.key_number == 9:
            #     macropad.consumer_control.send(
            #         macropad.ConsumerControlCode.VOLUME_DECREMENT
            #     )
            # if key_event.key_number == 10:
            #     macropad.consumer_control.send(
            #         macropad.ConsumerControlCode.MUTE
            #     )
            # if key_event.key_number == 11:
            #     macropad.consumer_control.send(
            #         macropad.ConsumerControlCode.VOLUME_INCREMENT
            #     )
            
            # MIDI Key Events
            if key_event.key_number == 1:
                macropad.pixels[key_event.key_number] = 0xFF0000
                macropad.midi.send(macropad.NoteOn(33, 127))
                time.sleep(0.5)
                macropad.midi.send(macropad.NoteOff(33, 0))
                time.sleep(0.5)
            if key_event.key_number == 4:
                macropad.midi.send(macropad.NoteOn(77, 127))
                time.sleep(0.5)
                macropad.midi.send(macropad.NoteOff(77, 0))
                time.sleep(0.5)
            if key_event.key_number == 7:
                macropad.midi.send(macropad.NoteOn(69, 127))
                time.sleep(0.5)
                macropad.midi.send(macropad.NoteOff(69, 0))
                time.sleep(0.5)

        if key_event.released:
            macropad.keyboard.release_all()
            if key_event.key_number < 12: # No pixel for encoder button
                macropad.pixels[key_event.key_number] = 0x000000
            
    # MicroPad Rotary Encoder Button
    if macropad.encoder_switch_debounced.pressed:
        #macropad.keyboard.send(macropad.Keycode.SPACE)
        macropad.pixels.fill((0, 255, 0))
        time.sleep(0.5)
        macropad.pixels.fill((0, 0, 0))
        print("Mode Select")
        print("Thitus Mode")

    # MicroPad Rotary Encoder Behavior
    if macropad.encoder > last_position:
        macropad.mouse.move(wheel=+5)
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.mouse.move(wheel=-5)
        last_position = current_position
        
    """Quad I2C rotary encoder.""" 
    # negate the position to make clockwise rotation positive
    positions = [encoder.position for encoder in encoders]
    for n, rotary_pos in enumerate(positions):
        if rotary_pos != last_positions[n]:
            print(f"Rotary #{n}: {rotary_pos}")

            # Behavior for the rotary encoders 
            # zero for the VFO
            if n == 0:
                if rotary_pos > last_positions[n]:
                    macropad.mouse.move(wheel=+5)
                if rotary_pos < last_positions[n]:
                    macropad.mouse.move(wheel=-5)
            
            # 1 for the
            if n == 1:
                if rotary_pos > last_positions[n]:
                    # Down or left
                    macropad.midi.send(macropad.NoteOn(44, 127))
                    time.sleep(0.25)
                    macropad.midi.send(macropad.PitchBend(44,rotary_pos))
                    time.sleep(0.25)
                    macropad.midi.send(macropad.NoteOff(44, 0))
                if rotary_pos < last_positions[n]:
                    # Up or right
                    macropad.midi.send(macropad.NoteOn(44, 127))
                    time.sleep(0.25)
                    macropad.midi.send(macropad.PitchBend(rotary_pos))
                    time.sleep(0.25)
                    macropad.midi.send(macropad.NoteOff(44, 0))



            last_positions[n] = rotary_pos
