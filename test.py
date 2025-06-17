import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("Test")
root.state('zoomed')
fre=Frame(root,width=400,height=200,bg="#2e2e2e")
fre.pack_propagate(False)
fre.place(relx=0.5,rely=0.3,anchor='center')
fr=Frame(fre,width=400,height=200,bg='#2e2e2e')
fr.pack(pady=20)
def phno():
     a=e1.get()
     b=e2.get()
     print(a,b)
def destroy():
     root.destroy()
     
fr.columnconfigure(0,weight=2)
fr.columnconfigure(1,weight=1)
fr.columnconfigure(2,weight=1)
fr.columnconfigure(3,weight=2)

fr.rowconfigure(0,weight=2)
fr.rowconfigure(1,weight=1)
fr.rowconfigure(2,weight=2)

l1=Label(fr,text="phone number:")
l1.grid(column=0,row=0,padx=5,pady=5,sticky='es')
l2=Label(fr,text="password:")
l2.grid(column=0,row=1,padx=5,pady=5,sticky='wn')
e1=Entry(fr)
e1.grid(column=1,row=0,columnspan=2,padx=5,pady=5,sticky='es')
e2=Entry(fr,show='*')
e2.grid(column=1,row=1,columnspan=2,padx=5,pady=5,sticky='en')
b1=Button(fr,text="submit",command=phno).grid(column=1,row=2,sticky='n')
b2=Button(fr,text="cancel",command=destroy).grid(column=2,row=2,sticky='wn')
root.mainloop()