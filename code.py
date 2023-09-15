# SPDX-FileCopyrightText: 2021 ladyada & Kattni Rembor for Adafruit Industries
# sdr-keys: 2023 K7MHI
"""
MacroPad HID KBD&Mouse wheel left and right when the rotary encoder is rotated
note macropad.keyboard.release_all()
"""
from adafruit_macropad import MacroPad
import time

# Rotary Encoder
macropad = MacroPad()
last_position = 0

print("K7MHI SDR Controller")

while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            # Frequency Step
            if key_event.key_number == 0:
                macropad.keyboard.send(macropad.Keycode.T)
            if key_event.key_number == 2:
                macropad.keyboard.press(macropad.Keycode.G)
            # Band Step
            if key_event.key_number == 3:
                macropad.keyboard.send(macropad.Keycode.M)
            if key_event.key_number == 5:
                macropad.keyboard.press(macropad.Keycode.N)
            # Filter Step
            if key_event.key_number == 6:
                macropad.keyboard.send(macropad.Keycode.B)
            if key_event.key_number == 8:
                macropad.keyboard.press(macropad.Keycode.V)            
            # Three Bottom Keys Volume Functions
            if key_event.key_number == 9:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_DECREMENT
                )
            if key_event.key_number == 10:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.VOLUME_INCREMENT
                )
            if key_event.key_number == 11:
                macropad.consumer_control.send(
                    macropad.ConsumerControlCode.MUTE
                )
            # MIDI Keys
            if key_event.key_number == 1:
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
            
            
    macropad.encoder_switch_debounced.update()
    # Rotary Encoder PTT Behavior
    if macropad.encoder_switch_debounced.pressed:
        macropad.keyboard.send(macropad.Keycode.SPACE)

    current_position = macropad.encoder
    # Rotary Encoder Behavior
    if macropad.encoder > last_position:
        macropad.mouse.move(wheel=+5)
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.mouse.move(wheel=-5)
        last_position = current_position
