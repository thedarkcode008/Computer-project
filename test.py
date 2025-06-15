import tkinter as tk
from tkinter import *
window=tk.Tk()
window.state('zoomed')
window.configure(bg='#2e2e2e')
label1=Label(window,text='hi hows this',bg='#2e2e2e',fg='white',font=("Ariel",16))
label1.pack()
#creating function for stoping
def des():
    label1.destroy()
    btn.destroy()
    label2=Label(window,text='Bro I Told Dont',bg='#2e2e2e',fg='white',font=("Ariel",16))
    label2.pack()
btn=Button(window,text="click me",bg='#2e2e2e',fg="white",command=des,font=("Ariel",16))
btn.pack(pady="20")
def boom():
    window.destroy()
btn2=Button(window,text='booom',bg='#2e2e2e',fg="white",command=boom,font=("Ariel",60))
btn2.pack(pady=50)
window.mainloop()
