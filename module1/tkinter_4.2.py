#binding a function to a widget 2
from tkinter import*

root =Tk()

def printName(event):
    print('Hello my name is Px0006 and I\'ll be your host today')

button_1 = Button(root, text='print my name' )
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()


