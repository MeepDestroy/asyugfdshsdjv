import turtle
t = turtle.Turtle()
x = 0

def squ():
    t.color("green","yellow")
    t.begin_fill()
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.end_fill()



while x < 6:
    x += 1
    squ()
    t.forward(25)

t.color("black","red")
t.begin_fill()
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(75)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.forward(25)
t.left(90)
t.forward(150)
t.color("black","blue")
t.left(90)
t.forward(25)
t.right(90)
t.forward(25)
t.right(90)
t.forward(25)

t.color("black","green")

t.right(90)
t.forward(50)
t.left(90)
t.forward(75)
t.left(90)

t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(150)
t.left(90)

t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)

t.end_fill()


#
#xx      x
#  xxxxxx ^
#   xxxx
#  x    x
#
