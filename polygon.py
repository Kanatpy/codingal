import turtle as  tr
tr.Screen().bgcolor("orange")
tr.screensize(300,400)
tr.shape("turtle")
tr.pensize(4)
num_sides = 6
side_length = 70
angle = 360/num_sides
for i in range(num_sides):
    tr.forward(side_length)
    tr.right(angle)

tr.done()