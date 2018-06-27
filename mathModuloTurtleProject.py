import turtle, math


def modulo_function(x):
    global MODULUS
    try:
        return x % 50 + 10 % MODULUS
    except TypeError:
        return 'pass'


def modulo_division(x, y):
    global MODULUS
    for z in range(MODULUS):
        if z * y % MODULUS == x % MODULUS:
            return z


def calculate_colors(initial_color, second_color, number_of_colors):
    (ir, ig, ib) = initial_color
    (sr, sg, sb) = second_color
    colors = []
    differenceR = (sr - ir) / (number_of_colors - 1)
    differenceG = (sg - ig) / (number_of_colors - 1)
    differenceB = (sb - ib) / (number_of_colors - 1)
    for i in range(number_of_colors):
        colors.append(
            (max(0, int(differenceR * i + ir)), max(0, int(differenceG * i + ig)), max(0, int(differenceB * i + ib))))
    return colors


MODULUS = 2000
COORDINATES = []
for i in range(MODULUS):
    angle = math.radians((360 / MODULUS * i) + 90)
    COORDINATES.append([math.cos(angle) * 500, math.sin(angle) * 500])
screen = turtle.Screen()
drawingTurtle = turtle.Turtle()
drawingTurtle.speed(0)
drawingTurtle.right(90)
drawingTurtle.penup()
drawingTurtle.forward(500)
drawingTurtle.pendown()
drawingTurtle.left(90)
drawingTurtle.circle(500)
screen.colormode(255)
colors = calculate_colors((66, 244, 235), (255, 162, 86), MODULUS)

tTableFile = open('tTableFile.txt', 'w')
for i in range(MODULUS):
    if modulo_function(i) == 'pass':
        pass
    else:
        drawingTurtle.pencolor(colors[i])
        drawingTurtle.penup()
        drawingTurtle.goto(COORDINATES[i])
        drawingTurtle.pendown()
        drawingTurtle.goto(COORDINATES[modulo_function(i)])
        tTableFile.write(str(i)+ ' '+ str(modulo_function(i))+ '\n')

tTableFile.close()
drawingTurtle.goto(COORDINATES[0])
screen.mainloop()
