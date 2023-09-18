# sdr-keys: K7MHI
import storage
import usb_midi
import usb_hid
import board, digitalio

# button press detection to enable USB
# MacroPad button A
button = digitalio.DigitalInOut(board.BUTTON_A)
button.pull = digitalio.Pull.DOWN

if not button.value:
    #storage.disable_usb_drive()
    #usb_cdc.disable()
    print ("USB Disabled")

# enable MIDI
usb_midi.enable()

# These are the default devices
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     usb_hid.Device.CONSUMER_CONTROL)
)
