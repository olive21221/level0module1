import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    user=simpledialog.askinteger('title','What is the radius in pixels?')
    # Make a new turtle
    oliver = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    oliver.circle(user)
    # Call the turtle .penup() method
    oliver.penup()
    # Move your turtle to a new x,y position using .goto()
    oliver.goto(-200,-150)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area=(math.pi * (user**2))
    # oliver.circle(math.pi * (user**2))
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + , move=True, align='left', font=('Arial',8,'normal'))
    oliver.write(arg="area = " + str(area), move=True, align='left', font=('Arial',32,'normal'))
    # Hide your turtle
    oliver.hideturtle()
    # Call turtle.done()
    turtle.done()
