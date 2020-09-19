import turtle
from random import randint, random	

turtle.shape('turtle')

while True:
    turtle.forward(50*random())
    turtle.left(randint(0, 360))
