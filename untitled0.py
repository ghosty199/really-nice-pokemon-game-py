from tkinter import *
import random
from PIL import Image, ImageTk
root=Tk()
root.geometry("600x500")
root.title("endless dice game")
root.config(bg="yellow")
img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))






label1=Label(root,text="Player 1", bg="blue", fg="white")
label1.place(relx=0.1, rely=0.4, anchor=CENTER)

label2=Label(root,text="", bg="blue", fg="white")
label2.place(relx=0.1, rely=0.5, anchor=CENTER)

label3=Label(root,text="Player 2", bg="blue", fg="white" )
label3.place(relx=0.9, rely=0.4, anchor=CENTER)

label4=Label(root,text="", bg="blue", fg="white")
label4.place(relx=0.9, rely=0.5, anchor=CENTER)

label5=Label(root,text="", bg="red", fg="white")
label5.place(relx=0.5, rely=0.6, anchor=CENTER)



button1=Button(root,image=img)
button1.place(relx=0.1, rely=0.7, anchor=CENTER)

button2=Button(root,image=img)
button2.place(relx=0.9, rely=0.7, anchor=CENTER)


























root.mainloop()