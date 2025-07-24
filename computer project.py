import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()
import customtkinter as ctk #importing everything from tkinter
from customtkinter import *
from tkinter import messagebox
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

def buycar():
     root.withdraw()
     root1=ctk.CTkToplevel(root)
     root1.title("Car Buying Portal")
     root1.state("zoomed")
     
     # Sample data
     Tata = ["Nexon","Altroz","Harrier","Safari","Punch","Tiago","Tigor","Harrier.ev","Punch.ev","Nexon.ev","Tiago.ev","Tigor.ev","Curvv.ev"]
     Suzuki = ["Ignis","Swift","Dzire","Fronx","Brezza","Grand Vitara","Espresso","Celerio","Alto","Baleno","Ertiga","XL6","Invicto","Eeco","WagonR","Jimny"]
     Mahindra = ["BE 6","XEV 9e","XUV 400","XUV 3XO","XUV 700","Bolero","Scorpio","Thar","Thar Roxx","Bolero neo","Scorpio N"]
     Hyundai = ["Alcazar","Creta","Eon","Exter","Ioniq 5","Verna","Venue","Tucson","Aura","i10","i20"]
     Kia = ["Carnival","Seltos","Sonet","Carens","EV 6","EV 9","Carens Clavis"]
     Citroen = ["C3","C5","Aircross","Basalt","eC3"]
     Volkswagen = ["Virtus", "Taigun", "Golf GTI","Tiguan"]
     Skoda = ["Kushaq", "Slavia", "Kodiaq", "Kylaq"]
     Honda = ["City", "Amaze", "Elevate"]
     Toyota = ["Urban Cruiser Hyryder", "Innova Hycross", "Fortuner", "Fortuner Legender", "Glanza", "Vellfire", "Hilux"]


     colors = ["Red", "Blue", "Black", "White", "Silver"]
     variants = ["Base", "Mid", "Top"]

     payment_methods = ["Credit Card", "Debit Card", "Net Banking", "UPI", "EMI"]

     # Variables
     selected_vehicle = ctk.StringVar(value=Tata[0])
     selected_color = ctk.StringVar(value=colors[0])
     selected_variant = ctk.StringVar(value=variants[0])
     selected_payment = ctk.StringVar(value=payment_methods[0])

     # Title
     ctk.CTkLabel(root1, text="Buy a Car", font=("Helvetica", 50, "bold")).pack(pady=10)

     #creating a transparent frame to arrange vehices,colors and variant
     tframe1=CTkFrame(root1,width=400,height=100,fg_color="transparent")
     tframe1.place(relx=0.5,rely=0.3,anchor='center')

     #creating a transparent frame to arrange payment
     tframe2=CTkFrame(root1,width=400,height=100,fg_color="transparent")
     tframe2.place(relx=0.5,rely=0.8,anchor='center')


     # Vehicle List
     ctk.CTkLabel(tframe1, text="Select a Vehicle:", font=("Arial", 16)).grid(row=0,column=2)

     a=ctk.CTkLabel(tframe1, text="Tata", font=("Arial", 12,"bold"))
     a.grid(row=1,column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Tata,variable=selected_vehicle)
     vehicle_menu.grid(row=2,column=0,padx=8)

     b=ctk.CTkLabel(tframe1, text="Suzuki", font=("Arial", 12,"bold"))
     b.grid(row=1,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Suzuki,variable=selected_vehicle)
     vehicle_menu.grid(row=2,column=1,padx=8)

     c=ctk.CTkLabel(tframe1, text="Mahindra", font=("Arial", 12,"bold"))
     c.grid(row=1,column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Mahindra,variable=selected_vehicle)
     vehicle_menu.grid(row=2,column=2,padx=8)

     d=ctk.CTkLabel(tframe1, text="Hyundai", font=("Arial", 12,"bold"))
     d.grid(row=1,column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Hyundai,variable=selected_vehicle)
     vehicle_menu.grid(row=2,column=3,padx=8)

     e=ctk.CTkLabel(tframe1, text="Kia", font=("Arial", 12,"bold"))
     e.grid(row=1,column=4)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Kia,variable=selected_vehicle)
     vehicle_menu.grid(row=2,column=4,padx=8)

     f = ctk.CTkLabel(tframe1, text="Citroen", font=("Arial", 12, "bold"))
     f.grid(row=3, column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Citroen, variable=selected_vehicle)
     vehicle_menu.grid(row=4, column=0, padx=8)

     g = ctk.CTkLabel(tframe1, text="Volkswagen", font=("Arial", 12, "bold"))
     g.grid(row=3,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Volkswagen, variable=selected_vehicle)
     vehicle_menu.grid(row=4, column=1, padx=8)

     h = ctk.CTkLabel(tframe1, text="Skoda", font=("Arial", 12, "bold"))
     h.grid(row=3, column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Skoda, variable=selected_vehicle)
     vehicle_menu.grid(row=4, column=2, padx=8)

     i = ctk.CTkLabel(tframe1, text="Honda", font=("Arial", 12, "bold"))
     i.grid(row=3, column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Honda, variable=selected_vehicle)
     vehicle_menu.grid(row=4, column=3, padx=8)

     j = ctk.CTkLabel(tframe1, text="Toyota", font=("Arial", 12, "bold"))
     j.grid(row=3, column=4)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Toyota, variable=selected_vehicle)
     vehicle_menu.grid(row=4, column=4, padx=8)

     #creating a transparent label
     ctk.CTkLabel(tframe1, text="   ").grid(row=5,column=2)


     # Color Options
     ctk.CTkLabel(tframe1, text="Select Color:", font=("Arial", 16)).grid(row=6,column=2)
     n=0
     for color in colors:
          clr=ctk.CTkRadioButton(tframe1, text=color, variable=selected_color, value=color)
          clr.grid(row=7,column=n,pady=10)
          n=n+1

     #creating a transparent label
     ctk.CTkLabel(tframe1, text="   ").grid(row=8,column=2)

     # Variant Options
     ctk.CTkLabel(tframe1, text="Select Variant:", font=("Arial", 16)).grid(row=9,column=2)
     variant_menu = ctk.CTkOptionMenu(tframe1,values=variants,variable=selected_variant)
     variant_menu.grid(row=10,column=2,pady=10)

     # Payment Options
     ctk.CTkLabel(tframe2, text="Select Payment Method:", font=("Arial", 16)).grid(row=0,column=2,pady=10)
     m=0
     for method in payment_methods:
          var=ctk.CTkRadioButton(tframe2, text=method, variable=selected_payment, value=method)
          var.grid(column=m,row=1,padx=5)
          m=m+1

     # Submit Function
     def submit():
          summary = f"""
          Vehicle: {selected_vehicle.get()}
          Color: {selected_color.get()}
          Variant: {selected_variant.get()}
          Payment Method: {selected_payment.get()}
          """
          messagebox.showinfo("Purchase Summary", summary)
          
          root.deiconify()      # Show the root window again
          root.state('zoomed')
          root1.destroy()

     # Submit Button
     ctk.CTkButton(tframe2, text="Place Order", command=submit,font=("Arial", 16,"bold")).grid(row=2,column=2,pady=40)

     # Run the GUI
     root.mainloop()



def sub(): #function for receiving phno and pass
     a=e1.get()
     b=e2.get()
     select='SELECT * FROM user WHERE phno="{}" AND passwd="{}"'.format(a,b)
     mycur.execute(select)
     login=mycur.fetchone()
     
     if a=="00" and b=="admin":
          root.withdraw()
          adminwin=ctk.CTkToplevel(root)
          adminwin.state("zoomed")
          adminwin.title("Admin Window")
     elif login!=None:
          print("successfull")
   #Destroys all widgets in a given frame
          for widget in fre.winfo_children():
               widget.destroy()
          signup.destroy()
          fre.destroy()
          root.title("Selection")
          #creating a transparent frame to arrange vehices,colors and variant
          tfra=CTkFrame(root,width=400,height=100,fg_color="transparent")
          tfra.place(relx=0.5,rely=0.2,anchor='center')
          CTkLabel(tfra,text="Select An Option",font=("Arial", 20,"bold")).grid(row=0,column=0)
          carbuy=CTkButton(tfra,text="Buy a Car",command=buycar,font=("Arial", 15,"bold")).grid(row=1,column=0)
     else:
          incorrect=CTkLabel(fr,text="incorrect phone nunber or password")
          incorrect.grid(column=0,row=3,columnspan=2,sticky='e')
          
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
