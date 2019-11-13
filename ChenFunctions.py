import turtle
bob=turtle.Turtle()

def polygon(distance,sides):
    angle=360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
def star(distance):
    for times in range(5):
        bob.forward(distance)
        bob.right(144)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def explosion(distance,color):
    bob.color(color)
    bob.begin_fill()
    for times in range(8):
        bob.forward(distance)
        bob.right(135)
    bob.end_fill()

def top(sizes):
    bob.left(140)
    bob.forward(100)
    bob.right(140)
    bob.forward(150)
    bob.right(400)
    bob.forward(100)
    bob.left(220)
    bob.forward(150)
    bob.circle(100)
    
def topdown(sizes):
    bob.right(270)
    bob.forward(150)
    bob.left(90)
    bob.forward(150)
    bob.left(90)
    bob.forward(150)
    bob.circle(100)
    
def line(sizes):
    bob.right(1)
    bob.forward(200)
def bgblue(x,y):
    for times in range(100): 
        jump(x-times*10,y)
        bob.color(0,0,25+times)
        polygon(100,5)
def bgpurple(x,y):
    for times in range(100):     
        jump(x-times*10,y)
        bob.color(32,0,32+times)
        polygon(100,5)

