from turtle import *
import random

speed(3)

write("Loop" ,align="center",font=("Arial",60,"bold") )

pencolor("blue")
penup()
goto(-75,-125)
pendown()
width(20)
shapesize(4,4,12)

while True:
    for i in range(8):
        forward(140)
        left(45)
        