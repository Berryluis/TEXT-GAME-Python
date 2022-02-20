from portulipe import *
interface = ['#**********************','***********************','***********************']
x = 0
y = 0


blank_string = '''



'''

player = '#'

def update():
    dormir(0.003)
    print(blank_string)
    for a in interface:
        print(a)

def moverdireita():
    global x, interface, y

    current_int = interface[y]

    current_int = list(current_int)

    if x + 1 < len(current_int):
        x += 1

        current_int[x] = '#'
        current_int[x-1] = '*'

    resultado = ''.join(current_int)

    interface[y] = resultado

    update()

def moveresquerda():
    global x, interface, y

    current_int = interface[y]

    current_int = list(current_int)

    if x - 1 >= 0:
        x -= 1

        current_int[x] = '#'
        current_int[x+1] = '*'

    resultado = ''.join(current_int)

    interface[y] = resultado

    update()

def moverbaixo():
    global x, interface, y


    if y + 1 < len(interface):
        y += 1


        interface[y] = list(interface[y])
        interface[y-1] = list(interface[y-1])

        interface[y-1][x] = '*'

        interface[y][x] = '#'

        interface[y-1] = ''.join(interface[y-1])
        interface[y] = ''.join(interface[y])

    update()

def movercima():
    global x, interface, y


    if y - 1 >= 0:
        y -= 1


        interface[y] = list(interface[y])
        interface[y+1] = list(interface[y+1])

        interface[y+1][x] = '*'

        interface[y][x] = '#'

        interface[y+1] = ''.join(interface[y+1])
        interface[y] = ''.join(interface[y])

    update()



update()

while True:
    if keyboard.is_pressed('s'):
        moverbaixo()
    if keyboard.is_pressed('a'):
        moveresquerda()
    if keyboard.is_pressed('d'):
        moverdireita()
    if keyboard.is_pressed('w'):
        movercima()



    