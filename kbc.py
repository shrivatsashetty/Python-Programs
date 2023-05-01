from tkinter import *
root = Tk() #Tk is a class inside tkinter module and root is an object of Tk class
root.geometry('1500x900+0+0') #for setting height & width of panel arg passed as strings
root.title('Who Wants to be a Millionaire') #for changing panel heading
root.config(bg='black') #to add some background

leftFrame=Frame(root)
leftFrame.grid(row=0, column=0)

topFrame=Frame(leftFrame)
topFrame.grid()

centerFrame=Frame(root)
centerFrame.grid(row=1, column=0)

bottomFrame=Frame(root)
bottomFrame.grid(row=2, column=0)

rightframe=Frame(root)
rightframe.grid(row=0, column=1)
root.mainloop() #to keep the window from closing