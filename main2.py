from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","Stop!Virus found")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40,y=80)
def display():
    label=Label(text="hello i am madiha",bg="red",fg="yellow")
    
    label.place(x=50,y=50)
button1=Button(root,text="Click me",command=display)
button1.place(x=40,y=100)

root.mainloop()