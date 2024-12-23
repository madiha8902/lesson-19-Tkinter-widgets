from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.title("image ofnature")
root.geometry("5000x500")

upload=Image.open("nature.jpg")

image=ImageTk.PhotoImage(upload)

label=Label(root,image=image,height=350,width=500)
label.place(x=50,y=50)

label=Label(root,text="this is a nature image")
label.place(x=50,y=200)
root.mainloop()