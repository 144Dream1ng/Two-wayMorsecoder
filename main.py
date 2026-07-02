status = 0
radio.set_group(1)
pins.set_audio_pin(DigitalPin.P0)

def on_received_number(receivedNumber):
    if receivedNumber == 1 and status == 1: music.ring_tone(1000)
    else: music.stop_all_sounds()

def on_button_pressed_b():
    global status
    if status == 0: status = 1
    else: status = 0

def on_forever1():
    if input.button_is_pressed(Button.A) and status == 0: radio.send_number(1)
    else: radio.send_number(0)

def on_forever2():
    if status == 0:
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            """)

basic.forever(on_forever1)
basic.forever(on_forever2)
radio.on_received_number(on_received_number)
input.on_button_pressed(Button.B, on_button_pressed_b)