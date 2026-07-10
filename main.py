status = 0
radio.set_group(1)
pins.set_audio_pin(DigitalPin.P0)

def change_status():
    global status
    if status == 0: status = 1
    else: status = 0

def send_number():
    if input.button_is_pressed(Button.A) and status == 0: 
        radio.send_number(1)
    else: 
        radio.send_number(0)

def change_arrow():
    if status == 0:
        basic.show_arrow(ArrowNames.NORTH, 0)
    else: 
        basic.show_arrow(ArrowNames.SOUTH, 0)
    
def on_number(receivedNumber):
    if receivedNumber == 1 and status == 1:
        music.ring_tone(1000)
    else:
        music.stop_all_sounds()

basic.forever(send_number)
basic.forever(change_arrow)
radio.on_received_number(on_number)
input.on_button_pressed(Button.B, change_status)
