
# Write a python program that asks the user a minimum of 3 riddles.

# You can look at riddles.com if you don't already know any riddles.

# Collect the response of each riddle from the user and compare their answers to the correct answer.
from tkinter import simpledialog, messagebox, Tk

# Use a variable to keep track of the correctly answered riddles

# After all the riddles have been asked, tell the user how many they got correct

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    score = 0
    user = simpledialog.askstring('title', 'What has to be broken before you can use it?')

    if user == "an egg":
        score = score+1
    player = simpledialog.askstring('title', 'What gets wetter as it dries?')

    if player == "a towel":
        score = score+1
    riddle = simpledialog.askstring('title', 'What can full a room but takes up no space?')

    if riddle == "light":
        score = score+1

    score1 = str(score)
    messagebox.showinfo('title', score1)
    window.mainloop()
