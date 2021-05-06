#Practice Chapter 5 - Modules + Turtle

print("Jedi Turtle")

import turtle


turtle.forward(20)
turtle. speed(50000000000000000)

from turtle import *
color('red', 'yellow')
begin_fill()
pensize(2)
while True:
        forward(200)
        left(230)
        right(300)
        if abs(pos()) < 1:
            break
end_fill()

turtle.penup()
turtle.left(23)
turtle.pendown()

color('Blue', 'Green')
begin_fill()
while True:
        forward(300)
        left(190)
        right(86)
        if abs(pos()) < 1:
            break

done()


#Conditionals

a = 100
b = 50

if a > b:
    print("a is greater than b")
    
if a < b:
    print("a is less than b")
    
if a == b:
    print("a is equal to b")

# Practicing lists - 04.28.21
# When using lists, one must use "[ , ]""

l1 = ["5", "2", "3", "3.4", "Banana", "Horse"]

if "Banana" in l1:
    print("Fruit in list.")

if "Banana" not in l1:
    print("No fruit found.")
