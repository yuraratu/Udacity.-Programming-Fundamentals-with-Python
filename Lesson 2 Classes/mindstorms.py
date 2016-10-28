import turtle


window = turtle.Screen()
window.bgcolor('#2b579a')
brad = turtle.Turtle()


def draw_figure(figure, fsize, tshape, tcolor, tspeed):
    brad.shape(tshape)
    brad.color(tcolor)
    brad.speed(tspeed)

    if figure == 'square':
        for i in range(4):
            brad.forward(fsize)
            brad.right(90)
    elif figure == 'circle':
        brad.circle(fsize)
    elif figure == 'triangle':
        for i in range(3):
            brad.forward(fsize)
            brad.left(120)
    elif figure == 'ruby':
        brad.forward(fsize)
        brad.right(60)
        brad.forward(fsize)
        brad.right(120)
        brad.forward(fsize)
        brad.right(60)
        brad.forward(fsize)
        brad.right(120)


# draw_figure('square', 125, 'circle', 'black', 2)
# draw_figure('circle', 75, 'turtle', 'blue', 2)
# draw_figure('triangle', 125, 'arrow', 'green', 2)

for i in range(45):
    draw_figure('ruby', 100, 'turtle', 'white', 40)
    brad.right(8)
brad.right(90)
brad.forward(400)

window.exitonclick()
