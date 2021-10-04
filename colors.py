#Initialize Turtle
import turtle
import random
JackMcCord = turtle.Turtle()
JackMcCord.left(90)

#Functions

def randomDot():
    JackMcCord.color("magenta")
    JackMcCord.begin_fill()
    JackMcCord.circle(150)
    JackMcCord.color("pink")
    JackMcCord.end_fill()
    
#Main
randomDot()
