def on_button_pressed_a():
    global x
    if x > 0:
        x += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    if x < 4:
        x += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

cur = 0
x = 0
target = randint(0, 4)
led.plot(target, 0)
x = 2

def on_forever():
    global cur
    global target
    for i in range(5):
        cur = x
        led.plot(cur, 4 - i)
        basic.pause(100)
        if cur == target and i == 0:
            target = randint(0, 4)
            led.plot(target, 0)
        led.unplot(cur, 4 - i)
        basic.pause(100)
basic.forever(on_forever)
