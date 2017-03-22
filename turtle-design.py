from teardrop import *
import turtle

#the background turns to the color black
turtle.bgcolor("black")
bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

bob.penup()
#Creates a spiral that looks like the sun
bob.goto(0,0)
spiral(bob)
bob.penup()

#Creates a bunch of circle that gets smaller and smaller
circle(bob,40)

#creates a snowflake 
bob.color("white")
snowflake(bob,16,(-200,200),135)
snowflake(bob,16,(-200,-200),135)
snowflake(bob,16,(200,-200),135)
snowflake(bob,16,(200,200),135)
bob.penup()

#creates a teardrop and the color start out as green and turns to white
for times in range(8):
    bob.goto(0,0)
    teardrop(bob,10)
    bob.left(36)
    
