from tkinter import * 
import random
from PIL import ImageTk, Image

def switch_to_frame(frame):
    frame.tkraise()


root = Tk()
root.title("Math Quiz")
root.config(bg="White")
root.geometry('400x400')
root.resizable(0,0)


frame1 = Frame(root,bg='#542367')
frame2 = Frame(root,bg='#542367')
frame3 = Frame(root,bg='#542367')

label1 = Label(frame1, text='Select Your Difficulty', font=('Roboto', 16), bg='#542367', fg='white')
label1.pack(pady=5)

button1 = Button(frame1, text='Easy', bg="#542367", fg='white',
command=lambda: switch_to_frame(frame1), width=20, font=('Robot', 12))
button1.pack(pady=5)


button2 = Button(frame2, text='Medium', bg='#542367', fg='white',
command=lambda: switch_to_frame(frame2), width=20, font=('Robot', 12))
button2.pack(pady=5)


button3 = Button(frame3, text='Hard', bg='#542367', fg='white',
command=lambda: switch_to_frame(frame2), width=20, font=('Robot', 12))
button3.pack(pady=5)


frame1.place(x=0, y=0, width=400,height=400)
frame2.place(x=0, y=90, width=400,height=400)
frame3.place(x=0, y=140, width=400,height=400)






root.mainloop()
