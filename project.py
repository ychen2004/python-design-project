#import program
from ChenFunctions import*
turtle.colormode(255)
turtle.bgcolor("black")
bob.speed(0)
for times in range(100):
    jump(-400+times*10,400)
    bob.begin_fill()
    bob.color(0,0,times)
    polygon(100,5)
    bob.end_fill()
for times in range(100):
    jump(400-times*10,250)
    bob.begin_fill()
    bob.color(0,0,times)
    polygon(100,5)
    bob.end_fill()
jump(-300,175)
for times in range(10):
    bob.begin_fill()
    bob.color(0+times*5,0+times*5,0)
    bob.circle(25+times*10)
    bob.end_fill()
for times in range(100):
    jump(-400+times*4,-400)
    bob.color(0,0,times*2)
    polygon(100,4)
    bob.right(50)
for times in range(100):
    jump(0+times*4,-400)
    bob.color(0,times,0)
    polygon(100,4)
    bob.right(50)
for times in range(200):
    jump(100,-400+times*4)
    polygon(25,4)
    bob.left(25)
    bob.color(times,times,0)
