import turtle as tr
screen = tr.Screen()
screen.bgcolor("lime")
screen.title("Kanats turtle")
tr.shape("turtle")
tr.pensize(3)
tr.color("red")
size = 0
while True:
    for i in range(4):
        tr.fd(size +1)
        tr.left(90)
        size = size-5
    size = size +1

tr.done()