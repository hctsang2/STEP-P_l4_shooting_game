input.onButtonPressed(Button.A, function () {
    if (x > 0) {
        x += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (x < 4) {
        x += 1
    }
})
let cur = 0
let x = 0
let target = randint(0, 4)
led.plot(target, 0)
x = 2
basic.forever(function () {
    for (let i = 0; i <= 4; i++) {
        cur = x
        led.plot(cur, 4 - i)
        basic.pause(100)
        led.unplot(cur, 4 - i)
        basic.pause(100)
        if (cur == target && i == 4) {
            target = randint(0, 4)
            led.plot(target, 0)
        }
    }
})
