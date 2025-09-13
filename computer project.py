import customtkinter as ctk
import tkinter as tk
from customtkinter import *
from tkinter import messagebox,ttk
from tkcalendar import DateEntry
import datetime
from PIL import Image

import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='asher123',database='dealer_service')
mycur=mycon.cursor()

#creating main window
root=ctk.CTk()
root.after(0,lambda: root.state('zoomed'))
ctk.set_appearance_mode("dark") #setiing window to dark mode
ctk.set_default_color_theme("dark-blue")
#creating frame for a clean layout

logo=Image.open("C:\\Users\\hp\\Downloads\\MagnusMotorsLogo.png")
logo = CTkImage(light_image=logo, dark_image=logo, size=(200, 200))

namelogo_img=Image.open("C:\\Users\\hp\\Downloads\\namelogo.png")
namelogo_img = CTkImage(light_image=namelogo_img, dark_image=namelogo_img, size=(200, 100))

f=font=('MT',20, "bold")
def cancellation(x):
     root.deiconify()
     root.state("zoomed")
     x.destroy()
     
def destroy(): #cancelling main window fnc
     root.destroy()

def admin():
     adminwindow=CTkToplevel(root)
     adminwindow.state("zoomed")
     adminwindow.title("Admin Access Terminal")
     
     style = ttk.Style(root)
     style.theme_use("clam")  # Use a theme that supports fieldbackground

     # Configure Treeview style for dark theme
     style.configure("Treeview",
                     background="#2d2d2d",  # Dark gray background for rows
                     fieldbackground="#2d2d2d",  # Dark gray background for empty area
                     foreground="white",  # White text color
                     rowheight=25,
                     font=("Calibri", 12))

     style.configure("Treeview.Heading",
                     background="#444444",  # Slightly lighter gray for header
                     foreground="white",
                     font=("Calibri", 13, "bold"))

     # Optional: map selected row colors
     style.map("Treeview",
          background=[("selected", "#0078d7")],  # Blue selection
          foreground=[("selected", "white")])
     
     def carbooking():

          def delete_booking():
               if delivered.get():
                    a=delivered.get()
                    delivered.delete(0, 'end')
               elif cancel_booking.get():
                    a=cancel_booking.get()
                    cancel_booking.delete(0, 'end')
               mycur.execute("DELETE FROM car_purchase where Purchase_no={}".format(a))
               fetch_data_and_populate()#calling function to populate data in treeview
               
          for widget in adminwindow.winfo_children():
               widget.destroy()
          def fetch_data_and_populate():  #Fetches data from MySQL and populates the Treeview
               # 1. Execute query and fetch data
               mycur.execute("SELECT * FROM car_purchase")
               rows = mycur.fetchall()

               # 2. Clear existing data in the treeview
               for item in tree.get_children():
                    tree.delete(item)

               # 3. Populate the treeview with new data
               for row in rows:
                    tree.insert('', tk.END, values=row)
          tframe5=CTkFrame(adminwindow,width=400,height=100,fg_color="transparent")
          tframe5.place(relx=0.5,rely=0.7,anchor='center') 
          
          # --- Frame for Treeview and Scrollbar ---
          tree_frame = CTkFrame(adminwindow)
          tree_frame.place(anchor='center',relx=0.5,rely=0.2)

          # --- Scrollbar ---
          tree_scroll = ttk.Scrollbar(tree_frame)
          tree_scroll.pack(side="right", fill="y")

          # --- Treeview Widget ---
          columns = ('Purchase_no','phno', 'car_name', 'color', 'variant', 'payment','Price')
          tree = ttk.Treeview(
          tree_frame,height=15,
          columns=columns,
          show='headings',
          yscrollcommand=tree_scroll.set)

          # Define headings
          tree.heading('Purchase_no', text='Purchase Number')
          tree.heading('phno', text='Phone number')
          tree.heading('car_name', text='Car Name')
          tree.heading('color', text='Colour')
          tree.heading('variant', text='Variant')
          tree.heading('payment', text='Payment Method')
          tree.heading('Price', text='Price')

          tree.pack(fill="both", expand=True)
          tree_scroll.config(command=tree.yview)

          # --- Load Data Button ---
          load_button = CTkButton(tframe5, text="Load/Refresh Data", command=fetch_data_and_populate)
          load_button.grid(row=0,column=1)
          exit_btn=CTkButton(adminwindow,text="<--",command=admin_widgets)
          exit_btn.grid(row=0,column=0)
          
          CTkLabel(tframe5,text=" ").grid(row=1,column=1,rowspan=2,pady=20)
          CTkLabel(tframe5,text="Car Delivery Complete",font=("Arial", 20, "bold")).grid(row=3,column=0,pady=20)
          delivered=CTkEntry(tframe5,placeholder_text="Purchase Number")
          delivered.grid(row=4,column=0)
          CTkButton(tframe5,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=0,pady=10)
          CTkLabel(tframe5,text="Car Booking Cancel",font=("Arial", 20, "bold")).grid(row=3,column=2,pady=20)
          cancel_booking=CTkEntry(tframe5,placeholder_text="Purchase Number")
          cancel_booking.grid(row=4,column=2)
          CTkButton(tframe5,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=2,pady=10)
          fetch_data_and_populate()
     
     def carlist():
          for widget in adminwindow.winfo_children():
               widget.destroy()
               
          def deletecar():
               company_name=company_name_variable.get()
               carno=deletion.get()
               delete_query=f"DELETE FROM cars WHERE Car_no=%s"
               mycur.execute(delete_query,(carno,))
               deletion.delete(0,'end')
               fetch_data_and_populate()#calling function to populate data in treeview
               
          def addcar():
               company_name=company_name_variable.get()
               Car_no_query=f"SELECT Car_no FROM cars ORDER BY Car_no DESC LIMIT 1"
               mycur.execute(Car_no_query)
               last_row = mycur.fetchone()
               if last_row:
                    a=last_row[0]+1
               else:
                    a=1
               name=car_name.get()
               p1=price1.get()
               p2=price2.get()
               p3=price3.get()
               addition_query=f"INSERT INTO cars (Car_no,company,car,price1,price2,price3) VALUES(%s,%s,%s,%s,%s,%s)"
               mycur.execute(addition_query,(a,company_name,name,p1,p2,p3))
               car_name.delete(0,'end')
               price1.delete(0,'end')
               price2.delete(0,'end')
               price3.delete(0,'end')
               fetch_data_and_populate()#calling function to populate data in treeview    
          def editcar():
               company_name=company_name_variable.get()
               price=price_variable.get()
               car_no=edit_car_no.get()
               new_price=edit_price.get()
               edit_query=f"UPDATE cars SET {price}=%s where Car_no=%s"
               mycur.execute(edit_query,(new_price,car_no))
               edit_car_no.delete(0,'end')
               edit_price.delete(0,'end')
               fetch_data_and_populate()#calling function to populate data in treeview
               
               
          def fetch_data_and_populate():  #Fetches data from MySQL and populates the Treeview
               company_name=company_name_variable.get()
               # 1. Execute query and fetch data
               display="SELECT Car_no,car,price1,price2,price3 FROM cars WHERE company=%s"
               mycur.execute(display,(company_name,))
               rows = mycur.fetchall()      
               # 2. Clear existing data in the treeview
               for item in tree.get_children():
                    tree.delete(item)       
               # 3. Populate the treeview with new data
               for row in rows:
                    tree.insert('', tk.END, values=row) 
                    
          tframe6=CTkFrame(adminwindow,width=400,height=100,fg_color="transparent")
          tframe6.place(relx=0.5,rely=0.7,anchor='center') 
          
          # --- Frame for Treeview and Scrollbar ---
          tree_frame = CTkFrame(adminwindow)
          tree_frame.place(anchor='center',relx=0.5,rely=0.2)

          # --- Scrollbar ---
          tree_scroll = ttk.Scrollbar(tree_frame)
          tree_scroll.pack(side="right", fill="y")

          # --- Treeview Widget ---
          columns = ('Car_no','car', 'price1', 'price2', 'price3')
          tree = ttk.Treeview(
          tree_frame,height=15,
          columns=columns,
          show='headings',
          yscrollcommand=tree_scroll.set)

          # Define headings
          tree.heading('Car_no', text='Car Number')
          tree.heading('car', text='Car Name')
          tree.heading('price1', text='Price 1')
          tree.heading('price2', text='Price 2')
          tree.heading('price3', text='Price 3')

          tree.pack(fill="both", expand=True)
          tree_scroll.config(command=tree.yview)
          
          company=['Tata','Suzuki','Mahindra','Hyundai','Kia','Citroen','Volkswagen','Skoda','Honda','Toyota']
          company_name_variable=ctk.StringVar(value="Select a Company")
          # --- Load Data Button ---
          company_name_entry=CTkOptionMenu(tframe6, variable=company_name_variable, values=company)
          company_name_entry.grid(row=0,column=1,pady=5)
          load_button = CTkButton(tframe6, text="Load/Refresh Data", command=fetch_data_and_populate)
          load_button.grid(row=1,column=1,pady=5)
          exit_btn=CTkButton(adminwindow,text="<--",command=admin_widgets)
          exit_btn.grid(row=0,column=0)
          
          CTkLabel(tframe6,text=" ").grid(row=2,column=1,rowspan=2,pady=20)
          
          CTkLabel(tframe6,text="Delete Car",font=("Arial", 20, "bold")).grid(row=3,column=0,pady=20)
          deletion=CTkEntry(tframe6,placeholder_text="Car Number")
          deletion.grid(row=4,column=0,padx=5)
          CTkButton(tframe6,text='confirm',font=("Arial", 20, "bold"),command=deletecar).grid(row=5,column=0,pady=10,padx=5)
          
          CTkLabel(tframe6,text="Add Car",font=("Arial", 20, "bold")).grid(row=3,column=1,pady=15)
          car_name=CTkEntry(tframe6,placeholder_text="Car Name")
          car_name.grid(row=4,column=1,pady=5,padx=5)
          price1=CTkEntry(tframe6,placeholder_text="price 1")
          price1.grid(row=5,column=1,pady=5,padx=5)
          price2=CTkEntry(tframe6,placeholder_text="price 2")
          price2.grid(row=6,column=1,pady=5,padx=5)
          price3=CTkEntry(tframe6,placeholder_text="price 3")
          price3.grid(row=7,column=1,pady=5,padx=5)
          CTkButton(tframe6,text='confirm',font=("Arial", 20, "bold"),command=addcar).grid(row=8,column=1,pady=5,padx=5)
          
          CTkLabel(tframe6,text="Edit Price",font=("Arial", 20, "bold")).grid(row=3,column=2,pady=20)
          edit_car_no=CTkEntry(tframe6,placeholder_text="Car Number")
          edit_car_no.grid(row=4,column=2,padx=5)
          price_variable=ctk.StringVar(value="Choose Which Price")
          price_type=CTkOptionMenu(tframe6,variable=price_variable ,values=['Price1','Price2','Price3'])
          price_type.grid(row=5,column=2,padx=5)
          edit_price=CTkEntry(tframe6,placeholder_text="Enter Price")
          edit_price.grid(row=6,column=2,padx=5)
          CTkButton(tframe6,text='confirm',font=("Arial", 20, "bold"),command=editcar).grid(row=7,column=2,pady=10,padx=5)
          
     def cartest():
          def delete_booking():
               if test_finished.get():
                    a=test_finished.get()
                    test_finished.delete(0, 'end')
               elif cancel_booking.get():
                    a=cancel_booking.get()
                    cancel_booking.delete(0, 'end')
               mycur.execute("DELETE FROM car_Test where Test_id={}".format(a))
               fetch_data_and_populate()#calling function to populate data in treeview
          
          for widget in adminwindow.winfo_children():
               widget.destroy()
          def fetch_data_and_populate():  #Fetches data from MySQL and populates the Treeview
               # 1. Execute query and fetch data
               mycur.execute("SELECT * FROM car_test")
               rows = mycur.fetchall()

               # 2. Clear existing data in the treeview
               for item in tree.get_children():
                    tree.delete(item)

               # 3. Populate the treeview with new data
               for row in rows:
                    tree.insert('', tk.END, values=row)
          tframe7=CTkFrame(adminwindow,width=400,height=100,fg_color="transparent")
          tframe7.place(relx=0.5,rely=0.7,anchor='center') 
          
          # --- Frame for Treeview and Scrollbar ---
          tree_frame = CTkFrame(adminwindow)
          tree_frame.place(anchor='center',relx=0.5,rely=0.2)

          # --- Scrollbar ---
          tree_scroll = ttk.Scrollbar(tree_frame)
          tree_scroll.pack(side="right", fill="y")

          # --- Treeview Widget ---
          columns = ('Test_id','phno', 'car_name', 'company', 'time', 'date')
          tree = ttk.Treeview(
          tree_frame,height=15,
          columns=columns,
          show='headings',
          yscrollcommand=tree_scroll.set)

          # Define headings
          tree.heading('Test_id', text='Test ID')
          tree.heading('phno', text='Phone number')
          tree.heading('car_name', text='Car Name')
          tree.heading('company', text='Comapny')
          tree.heading('time', text='Time')
          tree.heading('date', text='Date')

          tree.pack(fill="both", expand=True)
          tree_scroll.config(command=tree.yview)

          # --- Load Data Button ---
          load_button = CTkButton(tframe7, text="Load/Refresh Data", command=fetch_data_and_populate)
          load_button.grid(row=0,column=1)
          exit_btn=CTkButton(adminwindow,text="<--",command=admin_widgets)
          exit_btn.grid(row=0,column=0)
          
          CTkLabel(tframe7,text=" ").grid(row=1,column=1,rowspan=2,pady=20)
          CTkLabel(tframe7,text="Test Drive complete",font=("Arial", 20, "bold")).grid(row=3,column=0,pady=20)
          test_finished=CTkEntry(tframe7,placeholder_text="Test ID")
          test_finished.grid(row=4,column=0)
          CTkButton(tframe7,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=0,pady=10)
          CTkLabel(tframe7,text="Cancel Test Drive Booking",font=("Arial", 20, "bold")).grid(row=3,column=2,pady=20)
          cancel_booking=CTkEntry(tframe7,placeholder_text="Test ID")
          cancel_booking.grid(row=4,column=2)
          CTkButton(tframe7,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=2,pady=10)
          fetch_data_and_populate()
     
     def servicebooking():

          def delete_booking():
               if serviced.get():
                    a=serviced.get()
                    serviced.delete(0, 'end')
               elif cancel_booking.get():
                    a=cancel_booking.get()
                    cancel_booking.delete(0, 'end')
               mycur.execute("DELETE FROM car_service where service_id={}".format(a))
               fetch_data_and_populate()#calling function to populate data in treeview
               
          for widget in adminwindow.winfo_children():
               widget.destroy()
          def fetch_data_and_populate():  #Fetches data from MySQL and populates the Treeview
               # 1. Execute query and fetch data
               mycur.execute("SELECT * FROM car_service")
               rows = mycur.fetchall()

               # 2. Clear existing data in the treeview
               for item in tree.get_children():
                    tree.delete(item)

               # 3. Populate the treeview with new data
               for row in rows:
                    tree.insert('', tk.END, values=row)
          tframe8=CTkFrame(adminwindow,width=400,height=100,fg_color="transparent")
          tframe8.place(relx=0.5,rely=0.7,anchor='center') 
          
          # --- Frame for Treeview and Scrollbar ---
          tree_frame = CTkFrame(adminwindow)
          tree_frame.place(anchor='center',relx=0.5,rely=0.2)

          # --- Scrollbar ---
          tree_scroll = ttk.Scrollbar(tree_frame)
          tree_scroll.pack(side="right", fill="y")

          # --- Treeview Widget ---
          columns = ('service_id','phno', 'car_name', 'company', 'service_type', 'problem','date')
          tree = ttk.Treeview(
          tree_frame,height=15,
          columns=columns,
          show='headings',
          yscrollcommand=tree_scroll.set)

          # Define headings
          tree.heading('service_id', text='Service ID')
          tree.heading('phno', text='Phone number')
          tree.heading('car_name', text='Car Name')
          tree.heading('company', text='Company')
          tree.heading('service_type', text='Service Type')
          tree.heading('problem', text='Problem')
          tree.heading('date', text='Date')

          tree.pack(fill="both", expand=True)
          tree_scroll.config(command=tree.yview)

          # --- Load Data Button ---
          load_button = CTkButton(tframe8, text="Load/Refresh Data", command=fetch_data_and_populate)
          load_button.grid(row=0,column=1)
          exit_btn=CTkButton(adminwindow,text="<--",command=admin_widgets)
          exit_btn.grid(row=0,column=0)
          
          CTkLabel(tframe8,text=" ").grid(row=1,column=1,rowspan=2,pady=20)
          CTkLabel(tframe8,text="Car Service Complete",font=("Arial", 20, "bold")).grid(row=3,column=0,pady=20)
          serviced=CTkEntry(tframe8,placeholder_text="Service ID")
          serviced.grid(row=4,column=0)
          CTkButton(tframe8,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=0,pady=10)
          CTkLabel(tframe8,text="Car Service Cancel",font=("Arial", 20, "bold")).grid(row=3,column=2,pady=20)
          cancel_booking=CTkEntry(tframe8,placeholder_text="Service ID")
          cancel_booking.grid(row=4,column=2)
          CTkButton(tframe8,text='confirm',font=("Arial", 20, "bold"),command=delete_booking).grid(row=5,column=2,pady=10)
          fetch_data_and_populate()
          
     def admin_widgets():
          for widget in adminwindow.winfo_children():
               widget.destroy()
          tframe4=CTkFrame(adminwindow,width=400,height=400,border_width=5,border_color="#FFFFFF")
          tframe4.place(relx=0.5,rely=0.4,anchor='center') 
          innerframe=CTkFrame(tframe4,width=400,height=100,fg_color="transparent")
          innerframe.place(relx=0.5,rely=0.5,anchor='center')   
          CTkButton(innerframe,text="Access Carbooking",command=carbooking,font=("Arial", 16, "bold")).grid(row=0,column=0,pady=5)
          CTkButton(innerframe,text="Acces Car List",command=carlist,font=("Arial", 16, "bold")).grid(row=1,column=0,pady=5)
          CTkButton(innerframe,text="Access Test Drive Booking",command=cartest,font=("Arial", 16, "bold")).grid(row=2,column=0,pady=5)
          CTkButton(innerframe,text="Access Service Booking",command=servicebooking,font=("Arial", 16, "bold")).grid(row=3,column=0,pady=5)
          CTkButton(innerframe,text="Exit",command=lambda: cancellation(adminwindow),font=("Arial", 16, "bold"),fg_color='#990000',hover_color="#670101").grid(row=4,column=0,pady=5)
          CTkLabel(adminwindow,text='',image=namelogo_img).pack(side='bottom') 
     admin_widgets()
          
     
     
def testcar():
     root.withdraw()
     root2=ctk.CTkToplevel(root)
     root2.state("zoomed")
     root2.title("Test Drive Booking Portal")
     #creating a transparent frame to arrange widgets
     tframe3=CTkFrame(root2,width=400,height=100,fg_color="transparent")
     tframe3.place(relx=0.5,rely=0.4,anchor='center')
     #sample data of list of cars

     #1.Tata
     mycur.execute("SELECT Car FROM cars WHERE company='Tata'")
     z1 = mycur.fetchall()
     # Extract car names as a flat list
     Tata = [row[0] for row in z1]

     #2.Suzuki
     mycur.execute("SELECT Car FROM cars WHERE company='Suzuki'")
     z2 = mycur.fetchall()
     # Extract car names as a flat list
     Suzuki = [row[0] for row in z2]

     #3.Mahindra
     mycur.execute("SELECT Car FROM cars WHERE company='Mahindra'")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Mahindra = [row[0] for row in z3]

     #4.Hyundai
     mycur.execute("SELECT Car FROM cars WHERE company='Hyundai'")
     z4 = mycur.fetchall()
     # Extract car names as a flat list
     Hyundai = [row[0] for row in z4]

     #5.Kia
     mycur.execute("SELECT Car FROM cars WHERE company='Kia'")
     z5 = mycur.fetchall()
     # Extract car names as a flat list
     Kia = [row[0] for row in z5]

     #6.Citroen
     mycur.execute("SELECT Car FROM cars WHERE company='Citroen'")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Citroen = [row[0] for row in z3]

     #7.Volkswagen
     mycur.execute("SELECT Car FROM cars WHERE company='Volkswagen'")
     z7 = mycur.fetchall()
     # Extract car names as a flat list
     Volkswagen = [row[0] for row in z7]

     #8.Skoda
     mycur.execute("SELECT Car FROM cars WHERE company='Skoda'")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Skoda = [row[0] for row in z8]

     #9.Honda
     mycur.execute("SELECT Car FROM cars WHERE company='Honda'")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Honda = [row[0] for row in z8]

     #10.Toyota
     mycur.execute("SELECT Car FROM cars WHERE company='Toyota'")
     z10 = mycur.fetchall()
     # Extract car names as a flat list
     Toyota = [row[0] for row in z10]

     selected_company = ctk.StringVar(value="Tata")
     companychange=0
     def select_from_tata(car):
         selected_company.set("Tata")
     def select_from_suzuki(car):
         selected_company.set("Suzuki")
     def select_from_mahindra(car):
         selected_company.set("Mahindra")
     def select_from_hyundai(car):
         selected_company.set("Hyundai")
     def select_from_kia(car):
         selected_company.set("Kia")
     def select_from_citroen(car):
         selected_company.set("Citroen")
     def select_from_volkswagen(car):
         selected_company.set("Volkswagen")
     def select_from_skoda(car):
         selected_company.set("Skoda")
     def select_from_honda(car):
         selected_company.set("Honda")
     def select_from_toyota(car):
         selected_company.set("Toyota")
     
     mycur.execute("SELECT Test_id FROM car_test ORDER BY Test_id DESC LIMIT 1")
     last_row = mycur.fetchone()
     if last_row:
          a=last_row[0]+1
     else:
          a=1

     def generate_times():
         times = []
         start = datetime.datetime.strptime("09:00", "%H:%M")
         for i in range(17):
             times.append((start + datetime.timedelta(minutes=30*i)).strftime("%H:%M"))
         return times

     def confirm_booking():
          phno=my_var.get()
          vehicle = vehicle_var.get()
          date    = date_entry.get_date()
          time    = time_var.get()
          company = selected_company.get()
          if vehicle and date and time:
               msg = (
               f"Test Drive Booked!\n\n"
               f"Vehicle: {vehicle}\n"
               f"Date: {date.strftime('%Y-%m-%d')}\n"
               f"Time: {time}\n"
               f"Company: {company}\n"
               f"Test ID: {a}\n"
               "Kindly Remember the Test ID"
             )
               messagebox.showinfo("Booking Confirmed", msg)
          else:
               messagebox.showwarning("Incomplete", "Please select all options.")
          mycur.execute("INSERT INTO car_test (Test_id,phno,car_name,company,time,date) VALUES({},'{}','{}','{}','{}','{}')".format(a,phno,vehicle,company,time,date))
          root.deiconify()      # Show the root window again
          root.state('zoomed')
          root2.destroy()

     # Title
     title = CTkLabel(root2, text="TEST DRIVE BOOKING FACILITY", font=("Arial", 50, "bold"))
     title.pack(pady=10)
        # Vehicle selection
     CTkLabel(tframe3, text="Select a Vehicle:", font=("Arial", 20, "bold")).grid(row=0,column=2,pady=10)
     vehicle_var = ctk.StringVar(value=" ")

     #Tata
     ctk.CTkLabel(tframe3, text="Tata", font=("Arial", 12,"bold")).grid(row=1,column=0)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Tata,command=select_from_tata)
     Test_menu.grid(row=2,column=0,padx=8)

     #Suzuki
     ctk.CTkLabel(tframe3, text="Suzuki", font=("Arial", 12,"bold")).grid(row=1,column=1)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Suzuki,command=select_from_suzuki)
     Test_menu.grid(row=2,column=1,padx=8)

     #Mahindra
     ctk.CTkLabel(tframe3, text="Mahindra", font=("Arial", 12,"bold")).grid(row=1,column=2)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Mahindra,command=select_from_mahindra)
     Test_menu.grid(row=2,column=2,padx=8)

     #Hyundai
     ctk.CTkLabel(tframe3, text="Hyundai", font=("Arial", 12,"bold")).grid(row=1,column=3)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Hyundai,command=select_from_hyundai)
     Test_menu.grid(row=2,column=3,padx=8)

     #Kia
     ctk.CTkLabel(tframe3, text="Kia", font=("Arial", 12,"bold")).grid(row=1,column=4)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Kia,command=select_from_kia)
     Test_menu.grid(row=2,column=4,padx=8)

     #Citroen
     ctk.CTkLabel(tframe3, text="Citoren", font=("Arial", 12,"bold")).grid(row=3,column=0)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Citroen,command=select_from_citroen)
     Test_menu.grid(row=4,column=0,padx=8)

     #Volkswagen
     ctk.CTkLabel(tframe3, text="Volkswagen", font=("Arial", 12,"bold")).grid(row=3,column=1)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Volkswagen,command=select_from_volkswagen)
     Test_menu.grid(row=4,column=1,padx=8)

     #Skoda
     ctk.CTkLabel(tframe3, text="Skoda", font=("Arial", 12,"bold")).grid(row=3,column=2)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Skoda,command=select_from_skoda)
     Test_menu.grid(row=4,column=2,padx=8)

     #Honda
     ctk.CTkLabel(tframe3, text="Honda", font=("Arial", 12,"bold")).grid(row=3,column=3)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Honda,command=select_from_honda)
     Test_menu.grid(row=4,column=3,padx=8)

     #Toyota
     ctk.CTkLabel(tframe3, text="Toyota", font=("Arial",12 ,"bold")).grid(row=3,column=4)
     Test_menu = CTkOptionMenu(tframe3, variable=vehicle_var, values=Toyota,command=select_from_toyota)
     Test_menu.grid(row=4,column=4,padx=8)


     # Date selection
     CTkLabel(tframe3, text="Select Pickup Date:",font=("Arial",20,"bold")).grid(row=5,column=0,columnspan=2,pady=20)
     date_entry = DateEntry(tframe3,width=40)
     date_entry.grid(row=6,column=0,columnspan=2)
     # Time selection
     CTkLabel(tframe3, text="Select Pickup Time:",font=("Arial",20,"bold")).grid(row=5,column=3,columnspan=2,pady=20)
     time_var = ctk.StringVar(value=generate_times()[0])
     time_combo = CTkOptionMenu(tframe3, variable=time_var, values=generate_times(),width=200,height=20)
     time_combo.grid(row=6,column=3,columnspan=2)
     # Confirm Button
     confirm_btn = CTkButton(tframe3, text="Confirm Booking", command=confirm_booking,font=("Arial",20,"bold"))
     confirm_btn.grid(row=9,column=2,pady=50)
     #cancel button
     ctk.CTkButton(tframe3, text="Cancel", command=lambda: cancellation(root2),font=("Arial", 16,"bold")).grid(row=10,column=2,pady=10)

def buycar():
     root.withdraw()
     root1=ctk.CTkToplevel(root)
     root1.title("Car Buying Portal")
     root1.state("zoomed")
     
     #sample data of list of cars
     
     #1.Tata
     mycur.execute("SELECT Car FROM cars WHERE company='Tata'")
     z1 = mycur.fetchall()
     # Extract car names as a flat list
     Tata = [row[0] for row in z1]
     
     #2.Suzuki
     mycur.execute("SELECT Car FROM cars WHERE company='Suzuki'")
     z2 = mycur.fetchall()
     # Extract car names as a flat list
     Suzuki = [row[0] for row in z2]
     
     #3.Mahindra
     mycur.execute("SELECT Car FROM cars WHERE company='Mahindra'")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Mahindra = [row[0] for row in z3]
     
     #4.Hyundai
     mycur.execute("SELECT Car FROM cars WHERE company='Hyundai'")
     z4 = mycur.fetchall()
     # Extract car names as a flat list
     Hyundai = [row[0] for row in z4]
     
     #5.Kia
     mycur.execute("SELECT Car FROM cars WHERE company='Kia'")
     z5 = mycur.fetchall()
     # Extract car names as a flat list
     Kia = [row[0] for row in z5]
     
     #6.Citroen
     mycur.execute("SELECT Car FROM cars WHERE company='Citroen'")
     z3 = mycur.fetchall()
     # Extract car names as a flat list
     Citroen = [row[0] for row in z3]
     
     #7.Volkswagen
     mycur.execute("SELECT Car FROM cars WHERE company='Volkswagen'")
     z7 = mycur.fetchall()
     # Extract car names as a flat list
     Volkswagen = [row[0] for row in z7]
     
     #8.Skoda
     mycur.execute("SELECT Car FROM cars WHERE company='Skoda'")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Skoda = [row[0] for row in z8]
     
     #9.Honda
     mycur.execute("SELECT Car FROM cars WHERE company='Honda'")
     z8 = mycur.fetchall()
     # Extract car names as a flat list
     Honda = [row[0] for row in z8]
     
     #10.Toyota
     mycur.execute("SELECT Car FROM cars WHERE company='Toyota'")
     z10 = mycur.fetchall()
     # Extract car names as a flat list
     Toyota = [row[0] for row in z10]
     
     selected_company = ctk.StringVar(value="Tata")
     def select_from_tata(car):
          selected_company.set("Tata")

     def select_from_suzuki(car):
          selected_company.set("Suzuki")

     def select_from_mahindra(car):
          selected_company.set("Mahindra")

     def select_from_hyundai(car):
          selected_company.set("Hyundai")

     def select_from_kia(car):
          selected_company.set("Kia")

     def select_from_citroen(car):
          selected_company.set("Citroen")

     def select_from_volkswagen(car):
          selected_company.set("Volkswagen")

     def select_from_skoda(car):
          selected_company.set("Skoda")

     def select_from_honda(car):
          selected_company.set("Honda")

     def select_from_toyota(car):
          selected_company.set("Toyota")

     colors = ["Red", "Blue", "Black", "White", "Silver"]
     variants = ["Base", "Mid", "Top"]

     payment_methods = ["Credit Card", "Debit Card", "Net Banking", "UPI", "EMI"]

     # Variables
     selected_vehicle = ctk.StringVar(value=" ")
     selected_color = ctk.StringVar(value=colors[0])
     selected_variant = ctk.StringVar(value=variants[0])
     selected_payment = ctk.StringVar(value=payment_methods[0])

     # Title
     ctk.CTkLabel(root1, text="CAR BUYING FACILITY", font=("Helvetica", 50, "bold")).pack(pady=10)

     #creating a transparent frame to arrange vehices,colors and variant
     tframe1=CTkFrame(root1,width=400,height=100,fg_color="transparent")
     tframe1.place(relx=0.5,rely=0.4,anchor='center')

     #creating a transparent frame to arrange payment
     tframe2=CTkFrame(root1,width=400,height=100,fg_color="transparent")
     tframe2.place(relx=0.5,rely=0.8,anchor='center')


     # Vehicle List
     ctk.CTkLabel(tframe1, text="Select a Vehicle:", font=("Arial", 16)).grid(row=0,column=2)

     ctk.CTkLabel(tframe1, text="Tata", font=("Arial", 12,"bold")).grid(row=1,column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Tata,variable=selected_vehicle,command=select_from_tata)
     vehicle_menu.grid(row=2,column=0,padx=8)

     ctk.CTkLabel(tframe1, text="Suzuki", font=("Arial", 12,"bold")).grid(row=1,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Suzuki,variable=selected_vehicle,command=select_from_suzuki)
     vehicle_menu.grid(row=2,column=1,padx=8)

     ctk.CTkLabel(tframe1, text="Mahindra", font=("Arial", 12,"bold")).grid(row=1,column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Mahindra,variable=selected_vehicle,command=select_from_mahindra)
     vehicle_menu.grid(row=2,column=2,padx=8)

     ctk.CTkLabel(tframe1, text="Hyundai", font=("Arial", 12,"bold")).grid(row=1,column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Hyundai,variable=selected_vehicle,command=select_from_hyundai)
     vehicle_menu.grid(row=2,column=3,padx=8)

     ctk.CTkLabel(tframe1, text="Kia", font=("Arial", 12,"bold")).grid(row=1,column=4)
     vehicle_menu = ctk.CTkOptionMenu(tframe1,values=Kia,variable=selected_vehicle,command=select_from_kia)
     vehicle_menu.grid(row=2,column=4,padx=8)

     ctk.CTkLabel(tframe1, text="Citroen", font=("Arial", 12, "bold")).grid(row=3, column=0)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Citroen, variable=selected_vehicle,command=select_from_citroen)
     vehicle_menu.grid(row=4, column=0, padx=8)

     ctk.CTkLabel(tframe1, text="Volkswagen", font=("Arial", 12, "bold")).grid(row=3,column=1)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Volkswagen, variable=selected_vehicle,command=select_from_volkswagen)
     vehicle_menu.grid(row=4, column=1, padx=8)

     ctk.CTkLabel(tframe1, text="Skoda", font=("Arial", 12, "bold")).grid(row=3, column=2)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Skoda, variable=selected_vehicle,command=select_from_skoda)
     vehicle_menu.grid(row=4, column=2, padx=8)

     ctk.CTkLabel(tframe1, text="Honda", font=("Arial", 12, "bold")).grid(row=3, column=3)
     vehicle_menu = ctk.CTkOptionMenu(tframe1, values=Honda, variable=selected_vehicle,command=select_from_honda)
     vehicle_menu.grid(row=4, column=3, padx=8)

     ctk.CTkLabel(tframe1, text="Toyota", font=("Arial", 12, "bold")).grid(row=3, column=4)
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
          
          sql = f"SELECT {price_column} FROM cars WHERE Car = %s and company= %s"
          mycur.execute(sql,(vehicle,company))
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
          
     mycur.execute("SELECT Purchase_no FROM car_purchase ORDER BY Purchase_no DESC LIMIT 1")
     last_row = mycur.fetchone()
     if last_row:
          a=last_row[0]+1
     else:
          a=1
          
     # Submit Function
     def submit():
          summary = f"""
          Vehicle: {selected_vehicle.get()}
          Color: {selected_color.get()}
          Variant: {selected_variant.get()}
          Payment Method: {selected_payment.get()}
          Price: ₹{price_value}
          Purchase number: {a}
          Kindly Remember the purchase number for later clarification
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
     ctk.CTkButton(tframe2, text="Cancel", command=lambda: cancellation(root1),font=("Arial", 16,"bold")).grid(row=3,column=2,pady=10)
     
def carservice():
     root.withdraw()
     root3=CTkToplevel(root)
     root3.state("zoomed")
     root3.title("Service Portal")
     def _add_entry(label_text):
          label = ctk.CTkLabel(form_frame, text=label_text, font=("Arial", 16, "bold"))
          label.pack(pady=(10, 0))
          entry = ctk.CTkEntry(form_frame, width=400)
          entry.pack(pady=5)
          return entry
     
     mycur.execute("SELECT service_id FROM car_service ORDER BY service_id DESC LIMIT 1")
     last_row = mycur.fetchone()
     if last_row:
          a=last_row[0]+1
     else:
          a=1
     
     def _add_widget(label_text, widget):
          label = ctk.CTkLabel(form_frame, text=label_text, font=("Arial", 16, "bold"))
          label.pack(pady=(10, 0))
          widget.pack(pady=5)
    
     def submit_form():
          x=my_var.get()
          model = model_entry.get()
          prob= problem.get()
          company=company_type.get()
          service=service_type.get()
          date=date_entry.get_date()
          if not all([model,prob]):
              messagebox.showwarning("Missing Info", "Please fill in all fields.")
              return
          summary = f"Car model: {model}\nCompany: {company}\nService Type: {service}\nProblem: {prob}\nService ID: {a}\nKindly Remember the Service ID"
          messagebox.showinfo("Booking Confirmed", summary)
          insert="INSERT INTO car_service (service_id,phno,car_name,company,service_type,problem,date) VALUES({},'{}','{}','{}','{}','{}','{}')".format(a,x,model,company,service,prob,date)
          mycur.execute(insert)
          root.deiconify()
          root.state("zoomed")
          root3.destroy()
     
     # Title Label
     title_label = CTkLabel(root3, text="CAR SERVICE FACILITY", font=("Arial", 50, "bold"))
     title_label.pack(pady=20)
     # Frame for input fields
     form_frame = CTkFrame(root3,height=500,width=600)
     form_frame.pack(pady=10, padx=20,)
     form_frame.pack_propagate("False")
     
     def validate_length(P):
          return len(P)<=30
     vcmd=(form_frame.register(validate_length),'%P')
     
     # Car Model Entry
     model_entry = _add_entry("Car Model")
     #car company entry
     company_type=ctk.StringVar(value='Tata')
     company=['Tata','Suzuki','Mahindra','Hyundai','Kia','Citroen','Volkswagen','Skoda','Honda','Toyota']
     company_dropdown=CTkOptionMenu(form_frame,values=company,variable=company_type)
     _add_widget("Choose the company",company_dropdown)


     # Service Type Dropdown
     service_type = ctk.StringVar(value="Oil Change")
     service_dropdown = CTkOptionMenu(form_frame, values=["Oil Change", "Brake Check", "Full Service", "Engine Light ON","Wheel Alignment","Tyre Change","Other"], variable=service_type)
     _add_widget("Service Type",service_dropdown)
     # problem entry
     problem = CTkEntry(form_frame,validate='key',validatecommand=vcmd,width=400)
     _add_widget("Describe Your Problem in Less Than 30 Words",problem)
     # Date selection
     date_entry = DateEntry(form_frame,width=40)
     _add_widget("Select Your Date",date_entry)

     # Submit Button
     submit_button = CTkButton(form_frame,text="Submit", command=submit_form,font=("Arial", 16, "bold"))
     submit_button.pack(pady=20)
     cancel_button = CTkButton(form_frame,text="Cancel", command=lambda: cancellation(root3),font=("Arial", 16, "bold"))
     cancel_button.pack(pady=20)
     root.mainloop()
     


def sub(): #function for receiving phno and pass
     
     a=e1.get()
     b=e2.get()
     select='SELECT * FROM user WHERE phno="{}" OR email="{}" AND passwd="{}"'.format(a,a,b)
     mycur.execute(select)
     login=mycur.fetchone()
     
     if a=="00" and b=="admin":
          root.withdraw()
          admin()
     elif login!=None:
          print("successfull")
          #Destroys all widgets in a given frame
          for widget in root.winfo_children():
               widget.destroy()
          root.title("Selection")
          #if signed in with email obtaining the phone number
          phno_check=0
          d=my_var.get()
          if '@' in d:
               phno_check=1
          if phno_check==1:
               email_query="Select phno from user where email=%s"
               mycur.execute(email_query,(d,))
               row=mycur.fetchone()
               my_var.set(value=row[0])
          
          def msgbox1():
               purchase_no=entry_purchase_no.get()
               mycur.execute("SELECT * FROM car_purchase where Purchase_no={}".format(purchase_no))
               row=mycur.fetchone()
               userphno=my_var.get()
               if row is None:
                    messagebox.showerror("Error","Invalid purchase number")
               else:
                    phno=row[1]
                    if userphno==phno:
                         car_name=row[2]
                         color=row[3]
                         variant=row[4]
                         price=row[6]
                         payment=row[5]
                         summary = f"""
                         Here is the information
                         Vehicle: {car_name}
                         Color: {color}
                         Variant: {variant}
                         Price: ₹{price}
                         Payment Method: {payment}
                         """             
                         messagebox.showinfo("Booking info",summary)
                    else:
                         messagebox.showerror("Error","Invalid purchase number")
               entry_purchase_no.delete(0,'end')
          def msgbox2():
               test_id=entry_test_id.get()
               mycur.execute("SELECT * FROM car_test where Test_id={}".format(test_id))
               row=mycur.fetchone()
               userphno=my_var.get()
               if row is None:
                    messagebox.showerror("Error","Invalid purchase number")
               else:
                    phno=row[1]
                    if userphno==phno:
                         car_name=row[2]
                         company=row[3]
                         time=row[4]
                         date=row[5]
                         summary = f"""
                         Here is the information
                         Vehicle: {car_name}
                         Company: {company}
                         Time: {time}
                         Date: {date}
                         """             
                         messagebox.showinfo("Booking info",summary)
                    else:
                         messagebox.showerror("Error","Invalid Test ID")
               entry_test_id.delete(0,'end')
          
          def cancel_carbuy():
               userphno=my_var.get()
               purchase_no=purchase_no_entry_cancel.get()
               mycur.execute("SELECT phno FROM car_purchase where Purchase_no={}".format(purchase_no))
               row=mycur.fetchone()
               if row is None:
                    messagebox.showerror("Error","Invalid purchase number")
               else:
                    phno=row[0]
                    if phno==userphno:
                         response=messagebox.askokcancel("Cancel purchase?","Are You Sure")
                         if response:
                              mycur.execute("DELETE FROM car_purchase WHERE Purchase_no={}".format(purchase_no))
                         else:
                              messagebox.showerror("Error","Purchase not cancelled")
                         purchase_no_entry_cancel.delete(0,'end')
                    else:
                         messagebox.showerror("Error","Purchase_no not valid")
                    
          def cancel_cartest():
               userphno=my_var.get()
               test_id=test_id_entry_cancel.get()
               mycur.execute("SELECT phno FROM car_test where Test_id={}".format(test_id))
               row=mycur.fetchone()
               if row is None:
                    messagebox.showerror("Error","Invalid purchase number")
               else:
                    phno=row[0]
                    if phno==userphno:
                         response=messagebox.askokcancel("Cancel Test Drive?","Are You Sure")
                         if response:
                              mycur.execute("DELETE FROM car_test WHERE Test_id={}".format(test_id))
                         else:
                              messagebox.showerror("Error","Test Drive not cancelled")
                         test_id_entry_cancel.delete(0,'end')
                    else:
                         messagebox.showerror("Error","Test ID Not Valid")
                    
          def cancel_carservice():
               userphno=my_var.get()
               service_id=service_id_entry_cancel.get()
               mycur.execute("SELECT phno FROM car_service where service_id={}".format(service_id))
               row=mycur.fetchone()
               if row is None:
                    messagebox.showerror("Error","Invalid purchase number")
               else:
                    phno=row[0]
                    if phno==userphno:
                         response=messagebox.askokcancel("Cancel service?","Are You Sure")
                         if response:
                              mycur.execute("DELETE FROM car_service WHERE service_id={}".format(service_id))
                         else:
                              messagebox.showerror("Error","service not cancelled")
                         service_id_entry_cancel.delete(0,'end')
                    else:
                         messagebox.showerror("Error","Service ID Not Valid")
          
          def search():
               car_name=search_price.get()
               car_name=car_name.title()
               mycur.execute("SELECT price1,price2,price3 FROM cars WHERE car='{}'".format(car_name))
               row=mycur.fetchone()
               if row:
                    price_summary=f'Base Price={row[0]}\nMid Price={row[1]}\nTop Price={row[2]}'
                    messagebox.showinfo("Magnus Motors",price_summary)
               else:
                    messagebox.showerror("Error","Car Not Found")
          
          #creating a transparent frame to arrange widgets
          
          tframe3=CTkFrame(root,fg_color="transparent")
          tframe3.place(relx=0.52,rely=0.4,anchor='center')
          
          CTkLabel(tframe3,text="Select An Option",font=("Arial", 50,"bold")).grid(row=0,column=1,pady=50)
          
          carbuy=CTkButton(tframe3,text="Buy a Car",command=buycar,height=40,font=("Arial", 16,"bold")).grid(row=1,column=0)
          CTkLabel(tframe3,text="  ",fg_color="transparent").grid(row=2,column=1)
          seecarbook=CTkButton(tframe3,text="See Booked Cars",command=msgbox1,height=30,font=("Arial", 16,"bold")).grid(row=4,column=0,pady=5)
          entry_purchase_no=CTkEntry(tframe3,placeholder_text="Enter Purchase No.")
          entry_purchase_no.grid(row=3,column=0,pady=5)
          
          cartest=CTkButton(tframe3,text="Book a Test Drive",command=testcar,height=40,font=("Arial", 16,"bold")).grid(row=1,column=2)
          seetestbook=CTkButton(tframe3,text="See Booked Test Drive",command=msgbox2,height=30,font=("Arial", 16,"bold")).grid(row=4,column=2,pady=5)
          entry_test_id=CTkEntry(tframe3,placeholder_text="Enter Test ID")
          entry_test_id.grid(row=3,column=2,pady=5)
          
          car_service=CTkButton(tframe3,text="Book Service",command=carservice,height=40,font=("Arial", 20,"bold")).grid(row=1,column=1,pady=10)
          
          CTkLabel(tframe3,text=" ",fg_color="transparent").grid(row=5,column=1)
          
          CTkLabel(tframe3,text='Cancel Car Booking',font=("Arial", 16,"bold")).grid(row=6,column=0,pady=10)
          purchase_no_entry_cancel=CTkEntry(tframe3,placeholder_text="Enter Purchase No.")
          purchase_no_entry_cancel.grid(row=7,column=0)
          CTkButton(tframe3,text="confirm",command=cancel_carbuy,height=30,font=("Arial", 16,"bold")).grid(row=8,column=0,pady=5)
          
          CTkLabel(tframe3,text='Cancel Test Drive Booking',font=("Arial", 16,"bold")).grid(row=6,column=2,pady=10)
          test_id_entry_cancel=CTkEntry(tframe3,placeholder_text="Enter Test ID")
          test_id_entry_cancel.grid(row=7,column=2)
          CTkButton(tframe3,text="confirm",command=cancel_cartest,height=30,font=("Arial", 16,"bold")).grid(row=8,column=2,pady=5)
          
          CTkLabel(tframe3,text='Cancel Service Booking',font=("Arial", 16,"bold")).grid(row=6,column=1,pady=10)
          service_id_entry_cancel=CTkEntry(tframe3,placeholder_text="Enter Service ID")
          service_id_entry_cancel.grid(row=7,column=1)
          CTkButton(tframe3,text="confirm",command=cancel_carservice,height=30,font=("Arial", 16,"bold")).grid(row=8,column=1,pady=5)
          
          CTkLabel(root,text='',image=namelogo_img).place(relx=0.5, rely=1.0, anchor='s')
          back_btn=CTkButton(root,text="<--",command=signin,font=("Arial", 20,"bold")).place(anchor='nw')
          CTkLabel(tframe3,text=" ",fg_color="transparent").grid(row=9,column=1)
          search_price=CTkEntry(tframe3,placeholder_text="Search a Car's Price",height=40,border_width=2,border_color="green")
          search_price.grid(row=10,column=1,pady=5)
          CTkButton(tframe3,command=search,text="Search").grid(row=11,column=1,pady=5)
          
          exit_btn=CTkButton(tframe3,text="Exit",command=destroy,height=40,font=("Arial", 20,"bold"),fg_color='#990000',hover_color="#670101").grid(row=12,column=1,pady=50)
          
     else:
          messagebox.showinfo("Error","Incorrect Phone Number,Email or Password")
          

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
     
     lphno=CTkLabel(tframe,text="Phone Number",font=f)
     lphno.grid(column=0,row=0,padx=5,pady=5,sticky='e')
     ephno=CTkEntry(tframe)
     ephno.grid(column=1,row=0,columnspan=2,padx=5,pady=5,sticky='we')
     
     lpasswd=CTkLabel(tframe,text="Password",font=f)
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
def signin():
     root.title("Sign Up")
     global my_var
     my_var=ctk.StringVar()
     
     for widget in root.winfo_children():
          widget.destroy()
     
     fre=CTkFrame(root,width=400,height=350)
     fre.place(relx=0.5,rely=0.5,anchor='center')
     #transparent frame created to make the inner widgets into one unit
     fr=CTkFrame(fre,width=400,height=200,fg_color="transparent")
     fr.place(anchor='center',relx=0.5,rely=0.4)
     
     
     logo_img=CTkLabel(root,text=' ',image=logo)
     logo_img.place(anchor='n',relx=0.5)
     
     global e1
     global e2
     l1=CTkLabel(fr,text="Phno or Email:",font=f)
     l1.grid(column=0,row=0,columnspan=2,padx=5,pady=5,sticky='wes')
     e1=CTkEntry(fr,textvariable=my_var)
     e1.grid(column=0,row=1,columnspan=2,padx=5,pady=5,sticky='wse')


     l2=CTkLabel(fr,text="Password:",font=f)
     l2.grid(column=0,row=2,columnspan=2,padx=5,pady=5,sticky='wen')
     e2=CTkEntry(fr,show='*')
     e2.grid(column=0,row=3,columnspan=2,padx=5,pady=5,sticky='wne')

     b1=CTkButton(fr,text="Sign In",command=sub,font=("Arial", 16,"bold")).grid(column=0,row=4,sticky='n',padx=5)
     b2=CTkButton(fr,text="Exit",command=destroy,font=("Arial", 16,"bold"),fg_color='#990000',hover_color="#670101").grid(column=1,row=4,sticky='n',padx=5)
     
     signup=CTkButton(fre,text="Create an Account",command=creation,fg_color="transparent",font=('Arial',13,'underline'))
     signup.place(anchor='center',relx=0.5,rely=0.8)
     
signin()
root.mainloop()
mycon.commit()
mycon.close()