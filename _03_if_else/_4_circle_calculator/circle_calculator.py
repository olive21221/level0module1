# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
import math
import turtle
from tkinter import simpledialog

if __name__ == '__main__':

    oliver = turtle.Turtle()
    user = simpledialog.askinteger('title', 'What is the radius of the circle?')
    player = simpledialog.askstring('title', 'Would you like to calculate the area or circumference of the circle?')
    area = (math.pi * (user**2))
    circumference = (2 * math.pi * user)
    oliver.circle(user)
    if player == 'area':
        oliver.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 32, 'normal'))
    if player == 'circumference':
        oliver.write(arg="area = " + str(circumference), move=True, align='left', font=('Arial', 32, 'normal'))
