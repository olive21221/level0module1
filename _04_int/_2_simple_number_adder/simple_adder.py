
# Write a Python program that asks the user for two numbers.

# Display the sum of the two numbers to the user
from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askstring('title', 'Pick your first number')
    num2 = simpledialog.askstring('title', 'Pick your second number')
    sum = num1 + num2
    print("The sum is:" + sum)
    messagebox.showinfo('title', sum)
    window.mainloop()

