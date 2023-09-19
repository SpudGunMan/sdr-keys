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
            
    # Rotary Encoder Button
    if macropad.encoder_switch_debounced.pressed:
        #macropad.keyboard.send(macropad.Keycode.SPACE)
        macropad.pixels.fill((0, 255, 0))
        time.sleep(0.5)
        macropad.pixels.fill((0, 0, 0))
        print("Mode Select")
        print("Thitus Mode")

    # Rotary Encoder Behavior
    if macropad.encoder > last_position:
        macropad.mouse.move(wheel=+5)
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.mouse.move(wheel=-5)
        last_position = current_position
