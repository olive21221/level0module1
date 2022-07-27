import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    oliver = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    user = simpledialog.askstring('title', 'What shape do you want to draw? A square, triangle, or hexagon?')
    # Draw the shape requested by the user using if-elif-else statements
    if user=='square':
        for i in range (4):
            oliver.forward(100)
            oliver.left(90)
    elif user=='triangle':
        for i in range (3):
            oliver.forward(100)
            oliver.left(120)
    elif user=='hexagon':
        for i in range (6):
            oliver.forward(100)
            oliver.left(60)

    # Call the turtle .done() method
    turtle.done()
