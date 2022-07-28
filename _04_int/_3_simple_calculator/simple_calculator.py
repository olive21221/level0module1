
# Write a Python program that asks the user for two numbers.

# Then ask the user if the would like to add, subtract, multiply, or divide.

# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    number1 = simpledialog.askinteger('title', 'Pick your first number')
    number2 = simpledialog.askinteger('title', 'Pick your second number')
    choice = simpledialog.askstring('title', 'Would you like to add, subtract, multiply, or divide these numbers?')

    if choice == "add":
        messagebox.showinfo('title', number1 + number2)

    if choice =="subtract":
        messagebox.showinfo('title', number1 - number2)

    if choice =="multiply":
        messagebox.showinfo('title', number1 * number2)

    if choice =="divide":
        messagebox.showinfo('title', number1/number2)

    window.mainloop()
