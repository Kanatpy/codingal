import turtle as tr
screen = tr.Screen()
screen.bgcolor("black")
screen.title("Kanats hexagon turtle")
tr.shape("turtle")
tr.pensize(3)
tr.color("white")
tr.speed(0)
size = 0
while True:
    for i in range(6):
        tr.fd(size +1)
        tr.left(60)
        size = size-2
    size = size +1

tr.done()