import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import messagebox,ttk
from tkcalendar import DateEntry
import datetime

import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()

root = ctk.CTk()
root.title("Test Drive Booking System")
root.after(0,lambda: root.state('zoom'))

#creating a transparent frame to arrange widgets
tframe2=CTkFrame(root,width=400,height=100,fg_color="transparent")
tframe2.place(relx=0.5,rely=0.4,anchor='center')
# Sample vehicle list
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


def generate_times():
    times = []
    start = datetime.datetime.strptime("09:00", "%H:%M")
    for i in range(17):
        times.append((start + datetime.timedelta(minutes=30*i)).strftime("%H:%M"))
    return times

def confirm_booking():
    vehicle = vehicle_var.get()
    date    = date_entry.get_date()
    time    = time_var.get()
    if vehicle and date and time:
        msg = (
            f"Test Drive Booked!\n\n"
            f"Vehicle: {vehicle}\n"
            f"Date: {date.strftime('%Y-%m-%d')}\n"
            f"Time: {time}"
        )
        messagebox.showinfo("Booking Confirmed", msg)
    else:
        messagebox.showwarning("Incomplete", "Please select all options.")

# Title
title = CTkLabel(root, text="Book a Test Drive", font=("Arial", 50, "bold"))
title.pack(pady=10)
   # Vehicle selection
CTkLabel(tframe2, text="Select a Vehicle:", font=("Arial", 20, "bold")).grid(row=0,column=2,pady=10)
vehicle_var = ctk.StringVar(value=Tata[0])

#Tata
ctk.CTkLabel(tframe2, text="Tata", font=("Arial", 12,"bold")).grid(row=1,column=0)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Tata)
Test_menu.grid(row=2,column=0,padx=8)

#Suzuki
ctk.CTkLabel(tframe2, text="Suzuki", font=("Arial", 12,"bold")).grid(row=1,column=1)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Suzuki)
Test_menu.grid(row=2,column=1,padx=8)

#Mahindra
ctk.CTkLabel(tframe2, text="Mahindra", font=("Arial", 12,"bold")).grid(row=1,column=2)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Mahindra)
Test_menu.grid(row=2,column=2,padx=8)

#Hyundai
ctk.CTkLabel(tframe2, text="Hyundai", font=("Arial", 12,"bold")).grid(row=1,column=3)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Hyundai)
Test_menu.grid(row=2,column=3,padx=8)

#Kia
ctk.CTkLabel(tframe2, text="Kia", font=("Arial", 12,"bold")).grid(row=1,column=4)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Kia)
Test_menu.grid(row=2,column=4,padx=8)

#Citroen
ctk.CTkLabel(tframe2, text="Citoren", font=("Arial", 12,"bold")).grid(row=3,column=0)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Citroen)
Test_menu.grid(row=4,column=0,padx=8)

#Volkswagen
ctk.CTkLabel(tframe2, text="Volkswagen", font=("Arial", 12,"bold")).grid(row=3,column=1)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Volkswagen)
Test_menu.grid(row=4,column=1,padx=8)

#Skoda
ctk.CTkLabel(tframe2, text="Skoda", font=("Arial", 12,"bold")).grid(row=3,column=2)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Skoda)
Test_menu.grid(row=4,column=2,padx=8)

#Honda
ctk.CTkLabel(tframe2, text="Honda", font=("Arial", 12,"bold")).grid(row=3,column=3)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Honda)
Test_menu.grid(row=4,column=3,padx=8)

#Toyota
ctk.CTkLabel(tframe2, text="Toyota", font=("Arial",12 ,"bold")).grid(row=3,column=4)
Test_menu = CTkOptionMenu(tframe2, variable=vehicle_var, values=Toyota)
Test_menu.grid(row=4,column=4,padx=8)


# Date selection
CTkLabel(tframe2, text="Select Pickup Date:",font=("Arial",20,"bold")).grid(row=5,column=0,columnspan=2,pady=20)
date_entry = DateEntry(tframe2,width=40)
date_entry.grid(row=6,column=0,columnspan=2)
# Time selection
CTkLabel(tframe2, text="Select Pickup Time:",font=("Arial",20,"bold")).grid(row=5,column=3,columnspan=2,pady=20)
time_var = ctk.StringVar(value=generate_times()[0])
time_combo = CTkOptionMenu(tframe2, variable=time_var, values=generate_times(),width=200,height=20)
time_combo.grid(row=6,column=3,columnspan=2)
# Confirm Button
confirm_btn = CTkButton(tframe2, text="Confirm Booking", command=confirm_booking,font=("Arial",20,"bold"))
confirm_btn.grid(row=9,column=2,pady=50)
root.mainloop()
