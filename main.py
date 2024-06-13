import tkinter
from tkinter import *

root=Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]

#icon
Image_icon = PhotoImage(file="image\pencil.png")
root.iconphoto(False,Image_icon)


root.mainloop()

#Hello World