#binding a function to a widget 1
from tkinter import*

root =Tk()

def printName():
    print('Hello my name is Px0006 and I\'ll be your host today')

button_1 = Button(root, text='print my name' , command=printName)
button_1.pack()

root.mainloop()
