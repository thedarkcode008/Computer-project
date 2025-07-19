import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()
import customtkinter as ctk #importing everything from tkinter
from customtkinter import *
#creating main window
root=ctk.CTk()
root.title("Sign Up")
root.after(0,lambda: root.state('zoom'))
ctk.set_appearance_mode("dark") #setiing window to dark mode
ctk.set_default_color_theme("green")
#creating frame for a clean layoutg 
fre=CTkFrame(root,width=500,height=200)
fre.pack_propagate(False) #frame will not shrink to the size of inner widgets
fre.place(relx=0.5,rely=0.3,anchor='center')
#transparent frame created to make the inner widgets into one unit
fr=CTkFrame(fre,width=400,height=200,fg_color="transparent")
fr.pack(pady=20)
f=font=('MT',20, "bold")

def sub(): #function for receiving phno and pass
     a=e1.get()
     b=e2.get()
     
     if a=="00" and b=="admin":
          adminwin=ctk.CTkToplevel(root)
          adminwin.state("zoomed")
          adminwin.title("Admin Window")
     
     else:
   #Destroys all widgets in a given frame
          for widget in fr.winfo_children():
               widget.destroy()
               signup.destroy()
def destroy(): #cancelling window fnc
     root.destroy()
def creation(): #new registering window for new comers
     root.withdraw()
     window1=ctk.CTkToplevel(root)
     window1.state('zoomed')
     window1.title("Create An Account")
     
     def destroy1(): #cancelling window fnc
          root.deiconify()      # Show the root window again
          root.state('zoomed')
          window1.destroy()
     
     def go_back():
          x1=ephno.get()
          x2=epasswd.get()
          x3=efname.get()
          x4=elname.get()
          x5=eaddress.get()
          x6=esec_phno.get()
          x7=eemail.get()
          x='insert into user(phno,passwd,First_Name,Last_Name,address,sec_phno,email) values("{}","{}","{}","{}","{}","{}","{}")'.format(x1,x2,x3,x4,x5,x6,x7)
          mycur.execute(x)
          mycon.commit()
          window1.destroy()     # Close the new window
          root.deiconify()      # Show the root window again
          root.state('zoomed')
     
     tframe=CTkFrame(window1,width=400,height=200,fg_color="transparent") #transparent frame created to make the inner widgets into one unit
     tframe.place(relx=0.5,rely=0.3,anchor="center")
     
     btn_back=CTkButton(tframe,text="Submit",command=go_back).grid(column=1,row=7,sticky='n')
     btn_cancel=CTkButton(tframe,text="Cancel",command=destroy1).grid(column=2,row=7,sticky='wn')
     
     lphno=CTkLabel(tframe,text="Phone Number:",font=f)
     lphno.grid(column=0,row=0,padx=5,pady=5,sticky='e')
     ephno=CTkEntry(tframe)
     ephno.grid(column=1,row=0,columnspan=2,padx=5,pady=5,sticky='we')
     
     lpasswd=CTkLabel(tframe,text="Password:",font=f)
     lpasswd.grid(column=0,row=1,padx=5,pady=5,sticky='e')
     epasswd=CTkEntry(tframe)
     epasswd.grid(column=1,row=1,columnspan=2,padx=5,pady=5,sticky='we')
     
     lfname=CTkLabel(tframe,text="First Name:",font=f)
     lfname.grid(column=0,row=2,padx=5,pady=5,sticky='e')
     efname=CTkEntry(tframe)
     efname.grid(column=1,row=2,columnspan=2,padx=5,pady=5,sticky='we')
     
     llname=CTkLabel(tframe,text="Last Name:",font=f)
     llname.grid(column=0,row=3,padx=5,pady=5,sticky='e')
     elname=CTkEntry(tframe)
     elname.grid(column=1,row=3,columnspan=2,padx=5,pady=5,sticky='we')
     
     laddress=CTkLabel(tframe,text="Address:",font=f)
     laddress.grid(column=0,row=4,padx=5,pady=5,sticky='e')
     eaddress=CTkEntry(tframe)
     eaddress.grid(column=1,row=4,columnspan=2,padx=5,pady=5,sticky='we')
     
     lemail=CTkLabel(tframe,text="email:",font=f)
     lemail.grid(column=0,row=5,padx=5,pady=5,sticky='e')
     eemail=CTkEntry(tframe)
     eemail.grid(column=1,row=5,columnspan=2,padx=5,pady=5,sticky='we')
     
     lsec_phno=CTkLabel(tframe,text="Secondary Phno:",font=f)
     lsec_phno.grid(column=0,row=6,padx=5,pady=5,sticky='e')
     esec_phno=CTkEntry(tframe)
     esec_phno.grid(column=1,row=6,columnspan=2,padx=5,pady=5,sticky='we')
     
     

l1=CTkLabel(fr,text="Phone Number:",font=f)
l1.grid(column=0,row=0,padx=5,pady=5,sticky='es')
e1=CTkEntry(fr)
e1.grid(column=1,row=0,columnspan=2,padx=5,pady=5,sticky='wse')

l2=CTkLabel(fr,text="Password:",font=f)
l2.grid(column=0,row=1,padx=5,pady=5,sticky='wn')
e2=CTkEntry(fr,show='*')
e2.grid(column=1,row=1,columnspan=2,padx=5,pady=5,sticky='wne')

b1=CTkButton(fr,text="Submit",command=sub).grid(column=1,row=2,sticky='n')
b2=CTkButton(fr,text="Cancel",command=destroy).grid(column=2,row=2,sticky='wn')

signup=CTkButton(root,text="Create an Account",command=creation,fg_color="transparent",font=('segoe ui',13,'underline'))
signup.place(rely=0.5,relx=0.5,anchor="center")

root.mainloop()
mycon.close()
