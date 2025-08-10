import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

# Create main window
root = ctk.CTk()
root.title("Car Purchase Portal")
root.after(0,lambda: root.state('zoom'))
ctk.set_appearance_mode("dark") #setiing window to dark mode
ctk.set_default_color_theme("green")

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
ctk.CTkLabel(root, text="Buy a Car", font=("Helvetica", 50, "bold")).pack(pady=10)

#creating a transparent frame to arrange vehices,colors and variant
tframe1=CTkFrame(root,width=400,height=100,fg_color="transparent")
tframe1.place(relx=0.5,rely=0.3,anchor='center')

#creating a transparent frame to arrange payment
tframe2=CTkFrame(root,width=400,height=100,fg_color="transparent")
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

# Submit Button
ctk.CTkButton(tframe2, text="Place Order", command=submit,font=("Arial", 16,"bold")).grid(row=2,column=2,pady=40)

# Run the GUI
root.mainloop()


