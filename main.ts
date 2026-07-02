let status = 0
radio.setGroup(1)
basic.forever(function on_forever1() {
    if (input.buttonIsPressed(Button.A) && status == 0) {
        radio.sendNumber(1)
    } else {
        radio.sendNumber(0)
    }
    
})
basic.forever(function on_forever2() {
    if (status == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    }
    
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    if (receivedNumber == 1 && status == 1) {
        music.ringTone(1000)
    } else {
        music.stopAllSounds()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (status == 0) {
        status = 1
    } else {
        status = 0
    }
    
})
