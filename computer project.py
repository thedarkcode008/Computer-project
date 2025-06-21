import customtkinter as ctk #importing everything from tkinter
from customtkinter import *
#creating main window
root=ctk.CTk()
root.title("Test")
root.after(0,lambda:
root.state('zoom'))
ctk.set_appearance_mode("dark") #setiing window to dark mode
ctk.set_default_color_theme("green")
#creating frame for a clean layout
fre=CTkFrame(root,width=400,height=200)
fre.pack_propagate(False) #frame will not shrink to the size of inner widgets
fre.place(relx=0.5,rely=0.3,anchor='center')
#transparent frame created to make the inner widgets into one unit
fr=CTkFrame(fre,width=400,height=200,fg_color="transparent")
fr.pack(pady=20)

def phno(): #function for receiving phno and pass
     a=e1.get()
     b=e2.get()
     print(a,b)
def destroy(): #cancelling window fnc
     root.destroy()
def creation():
     root.withdraw()
     window1=ctk.CTkToplevel(root)
     window1.state('zoomed')
     window1.title("Create An Account")
     def go_back():
          window1.destroy()     # Close the new window
          root.deiconify()      # Show the root window again
          root.state('zoomed')
     
     tframe=CTkFrame(window1,width=400,height=200,fg_color="transparent") #transparent frame created to make the inner widgets into one unit
     tframe.place(relx=0.5,rely=0.4,anchor="center")
     btn_back = ctk.CTkButton(window1, text="Submit", command=go_back)
     btn_back.place(relx=0.5,rely=0.5,anchor="center")

l1=CTkLabel(fr,text="phone number:")
l1.grid(column=0,row=0,padx=5,pady=5,sticky='es')

l2=CTkLabel(fr,text="password:")
l2.grid(column=0,row=1,padx=5,pady=5,sticky='wn')
e1=CTkEntry(fr)
e1.grid(column=1,row=0,columnspan=2,padx=5,pady=5,sticky='wse')

e2=CTkEntry(fr,show='*')
e2.grid(column=1,row=1,columnspan=2,padx=5,pady=5,sticky='wne')

b1=CTkButton(fr,text="submit",command=phno).grid(column=1,row=2,sticky='n')
b2=CTkButton(fr,text="cancel",command=destroy).grid(column=2,row=2,sticky='wn')

signup=CTkButton(root,text="Create an Account",command=creation,fg_color="transparent",font=('segoe ui',13,'underline'))
signup.place(rely=0.5,relx=0.5,anchor="center")

root.mainloop()