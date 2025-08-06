import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox

# Set default appearance
ctk.set_appearance_mode("dark")  # Optional: dark/light/system
ctk.set_default_color_theme("blue")  # Can also be "green", "dark-blue", etc.

root=ctk.CTk()

def _add_entry(label_text):
    label = ctk.CTkLabel(form_frame, text=label_text, text_color="white")
    label.pack(pady=(10, 0))
    entry = ctk.CTkEntry(form_frame, width=400)
    entry.pack(pady=5)
    return entry

def _add_widget(label_text, widget):
    label = ctk.CTkLabel(form_frame, text=label_text, text_color="white")
    label.pack(pady=(10, 0))
    widget.pack(pady=5)
    
def submit_form():
    model = model_entry.get()
    prob= problem.get()
    company=company_type.get()
    service=service_type.get()
    if not all([model,prob]):
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return
    summary = f"Car model: {model}\nCompany: {company}\nService: {service}"
    messagebox.showinfo("Booking Confirmed", summary)

# Title Label
title_label = CTkLabel(root, text="CAR SERVICE FACILITY", font=("Arial", 24, "bold"))
title_label.pack(pady=20)
# Frame for input fields
form_frame = CTkFrame(root,height=400,width=600)
form_frame.pack(pady=10, padx=20,)
form_frame.pack_propagate("False")
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
problem = _add_entry("Describe The Problem In Less Than 30 words")

# Submit Button
submit_button = CTkButton(form_frame,text="Submit", command=submit_form)
submit_button.pack(pady=20)
root.mainloop()

