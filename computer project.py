import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()
import customtkinter as ctk #importing everything from tkinter
from customtkinter import *
from tkinter import messagebox
import random
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
     
     #sample data of list of cars
     
     #1.Tata
     mycur.execute("SELECT Car FROM tata")
     z1 = mycur.fetchall()
     # Extract car names as a flat list
     Tata = [row[0] for row in z1]
     
     #2.Suzuki
     mycur.execute("SELECT Car FROM suzuki")
     z2 = mycur.fetchall()
     # Extract car names as a flat list
     Suzuki = [row[0] for row in z2]
     
     #3.Mahindra
     mycur.execute("SELECT Car FROM mahindra")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Mahindra = [row[0] for row in z3]
     
     #4.Hyundai
     mycur.execute("SELECT Car FROM hyundai")
     z4 = mycur.fetchall()
     # Extract car names as a flat list
     Hyundai = [row[0] for row in z4]
     
     #5.Kia
     mycur.execute("SELECT Car FROM kia")
     z5 = mycur.fetchall()
     # Extract car names as a flat list
     Kia = [row[0] for row in z5]
     
     #6.Citroen
     mycur.execute("SELECT Car FROM citroen")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Citroen = [row[0] for row in z3]
     
     #7.Volkswagen
     mycur.execute("SELECT Car FROM volkswagen")
     z7 = mycur.fetchall()
     # Extract car names as a flat list
     Volkswagen = [row[0] for row in z7]
     
     #8.Skoda
     mycur.execute("SELECT Car FROM skoda")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Skoda = [row[0] for row in z8]
     
     #9.Honda
     mycur.execute("SELECT Car FROM honda")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Honda = [row[0] for row in z8]
     
     #10.Toyota
     mycur.execute("SELECT Car FROM toyota")
     z10 = mycur.fetchall()
     # Extract car names as a flat list
     Toyota = [row[0] for row in z10]
     
     selected_company = ctk.StringVar(value="Tata")
     companychange=0
     def select_from_tata(car):
          selected_company.set("tata")

     def select_from_suzuki(car):
          selected_company.set("suzuki")

     def select_from_mahindra(car):
          selected_company.set("mahindra")

     def select_from_hyundai(car):
          selected_company.set("hyundai")

     def select_from_kia(car):
          selected_company.set("kia")

     def select_from_citroen(car):
          selected_company.set("citroen")

     def select_from_volkswagen(car):
          selected_company.set("volkswagen")

     def select_from_skoda(car):
          selected_company.set("skoda")

     def select_from_honda(car):
          selected_company.set("honda")

     def select_from_toyota(car):
          selected_company.set("toyota")

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
     tframe1.place(relx=0.5,rely=0.4,anchor='center')

     #creating a transparent frame to arrange payment
     tframe2=CTkFrame(root1,width=400,height=100,fg_color="transparent")
     tframe2.place(relx=0.5,rely=0.8,anchor='center')


     # Vehicle List
     ctk.CTkLabel(tframe1, text="Select a Vehicle:", font=("Arial", 16)).grid(row=0,column=2)

     a=ctk.CTkLabel(tframe1, text="Tata", font=("Arial", 12,"bold"))
     a.grid(row=1,column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Tata,variable=selected_vehicle,command=select_from_tata)
     vehicle_menu.grid(row=2,column=0,padx=8)

     b=ctk.CTkLabel(tframe1, text="Suzuki", font=("Arial", 12,"bold"))
     b.grid(row=1,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Suzuki,variable=selected_vehicle,command=select_from_suzuki)
     vehicle_menu.grid(row=2,column=1,padx=8)

     c=ctk.CTkLabel(tframe1, text="Mahindra", font=("Arial", 12,"bold"))
     c.grid(row=1,column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Mahindra,variable=selected_vehicle,command=select_from_mahindra)
     vehicle_menu.grid(row=2,column=2,padx=8)

     d=ctk.CTkLabel(tframe1, text="Hyundai", font=("Arial", 12,"bold"))
     d.grid(row=1,column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Hyundai,variable=selected_vehicle,command=select_from_hyundai)
     vehicle_menu.grid(row=2,column=3,padx=8)

     e=ctk.CTkLabel(tframe1, text="Kia", font=("Arial", 12,"bold"))
     e.grid(row=1,column=4)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Kia,variable=selected_vehicle,command=select_from_kia)
     vehicle_menu.grid(row=2,column=4,padx=8)

     f = ctk.CTkLabel(tframe1, text="Citroen", font=("Arial", 12, "bold"))
     f.grid(row=3, column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Citroen, variable=selected_vehicle,command=select_from_citroen)
     vehicle_menu.grid(row=4, column=0, padx=8)

     g = ctk.CTkLabel(tframe1, text="Volkswagen", font=("Arial", 12, "bold"))
     g.grid(row=3,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Volkswagen, variable=selected_vehicle,command=select_from_volkswagen)
     vehicle_menu.grid(row=4, column=1, padx=8)

     h = ctk.CTkLabel(tframe1, text="Skoda", font=("Arial", 12, "bold"))
     h.grid(row=3, column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Skoda, variable=selected_vehicle,command=select_from_skoda)
     vehicle_menu.grid(row=4, column=2, padx=8)

     i = ctk.CTkLabel(tframe1, text="Honda", font=("Arial", 12, "bold"))
     i.grid(row=3, column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Honda, variable=selected_vehicle,command=select_from_honda)
     vehicle_menu.grid(row=4, column=3, padx=8)

     j = ctk.CTkLabel(tframe1, text="Toyota", font=("Arial", 12, "bold"))
     j.grid(row=3, column=4)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Toyota, variable=selected_vehicle,command=select_from_toyota)
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
     
     #Final Price
     def price():
          variant=selected_variant.get()
          company=selected_company.get()
          vehicle=selected_vehicle.get()
          if variant=="Base":
               price_column="Price1"
          elif variant=="Mid":
               price_column="Price2"
          elif variant=="Top":
               price_column="Price3"
          
          sql = f"SELECT {price_column} FROM {company} WHERE Car = %s"
          mycur.execute(sql,(vehicle,))
          row = mycur.fetchone()
          global price_value
          price_value = row[0] if row else "N/A"
          price_label.configure(text=f"Price: ₹{price_value}")
     obtain_price=CTkButton(tframe1,text="Obtain Price",command=price)
     obtain_price.grid(row=11,column=2,pady=10)
     price_box=CTkFrame(tframe1,border_width=2,border_color="green",height=35,width=200)
     price_box.grid(row=12,column=2,pady=10)
     price_label=CTkLabel(price_box,text=" ",font=("Arial", 16))
     price_label.place(anchor="center",relx=0.5,rely=0.5)
          

     # Payment Options
     ctk.CTkLabel(tframe2, text="Select Payment Method:", font=("Arial", 16)).grid(row=0,column=2,pady=10)
     m=0
     for method in payment_methods:
          payment_=ctk.CTkRadioButton(tframe2, text=method, variable=selected_payment, value=method)
          payment_.grid(column=m,row=1,padx=5)
          m=m+1
     
     #cancel function
     def cancellation():
          root.deiconify()      # Show the root window again
          root.state('zoomed')
          root1.destroy()
          
     mycur.execute("SELECT Purchase_no FROM car_purchase ORDER BY Purchase_no DESC LIMIT 1")
     last_row = mycur.fetchone()
     a=int(last_row[0])+1
          
     # Submit Function
     def submit():
          summary = f"""
          Vehicle: {selected_vehicle.get()}
          Color: {selected_color.get()}
          Variant: {selected_variant.get()}
          Payment Method: {selected_payment.get()}
          Price: ₹{price_value}
          Purchase number: {a}
          """
          messagebox.showinfo("Purchase Summary", summary)
          x=a
          x1=my_var.get()
          x2=selected_vehicle.get()
          x3=selected_color.get()
          x4=selected_variant.get()
          x5=selected_payment.get()
          x6=price_value
          insert = "INSERT INTO car_purchase (Purchase_no,phno, car_name, color, variant, payment,Price) VALUES({},'{}','{}','{}','{}','{}',{})".format(x,x1,x2,x3,x4,x5,x6)
          mycur.execute(insert)
          root.deiconify()      # Show the root window again
          root.state('zoomed')
          root1.destroy() 

     # Submit Button
     ctk.CTkButton(tframe2, text="Place Order", command=submit,font=("Arial", 16,"bold")).grid(row=2,column=2,pady=10)
     
     #cancel button
     ctk.CTkButton(tframe2, text="Cancel", command=cancellation,font=("Arial", 16,"bold")).grid(row=3,column=2,pady=10)
     


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
     
     
my_var=ctk.StringVar()
l1=CTkLabel(fr,text="Phone Number:",font=f)
l1.grid(column=0,row=0,padx=5,pady=5,sticky='es')
e1=CTkEntry(fr,textvariable=my_var)
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
mycon.commit()
mycon.close()
