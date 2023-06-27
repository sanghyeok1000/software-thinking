import turtle

turtle.color('red', 'yellow')


for _ in range(5):
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(360 / 5 * 2)

turtle.end_fill()
