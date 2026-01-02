import turtle as tr
tr.Screen().bgcolor("black")
pen = tr.Turtle()
pen.color("white")
pen.shape("turtle")
pen.forward(100)

for i in range(2):
    pen.left(120)
    pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

tr.done()