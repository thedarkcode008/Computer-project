import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

# Sample vehicle list
vehicles = [
    "Toyota Corolla",
    "Honda Civic",
    "Ford Mustang",
    "Tesla Model 3",
    "BMW 3 Series"
]

root = ctk.CTk()
root.title("Test Drive Booking System")
root.after(0, lambda: root.state('zoomed'))


def generate_times():
    times = []
    start = datetime.datetime.strptime("09:00", "%H:%M")
    for i in range(17):
        times.append((start + datetime.timedelta(minutes=30 * i)).strftime("%H:%M"))
    return times


def confirm_booking():
    vehicle = vehicle_var.get()
    date = date_entry.get_date()
    time = time_var.get()
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
ctk.CTkLabel(root, text="Book a Test Drive",
             font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

# Vehicle selection
ctk.CTkLabel(root, text="Select a Vehicle:",
             font=ctk.CTkFont(size=16)).pack(pady=(10, 5))
vehicle_var = tk.StringVar(value=vehicles[0])
ctk.CTkOptionMenu(root, variable=vehicle_var, values=vehicles).pack(pady=5)

# Date selection
ctk.CTkLabel(root, text="Select Pickup Date:",
             font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
date_entry = DateEntry(root, width=18,
                       background='darkblue',
                       foreground='white',
                       borderwidth=2,
                       date_pattern='yyyy-mm-dd')
date_entry.pack(pady=5)

# Time selection (segmented button)
ctk.CTkLabel(root, text="Select Pickup Time:",
             font=ctk.CTkFont(size=16)).pack(pady=(20, 5))
time_var = tk.StringVar(value=generate_times()[0])
ctk.CTkSegmentedButton(
    root,
    values=generate_times(),
    variable=time_var,
    selected_color="#28a745",
    unselected_color="#e0e0e0",
    text_color="#333333",
    corner_radius=8
).pack(fill="x", padx=20, pady=5)

# Confirm Button
ctk.CTkButton(root,
              text="Confirm Booking",
              command=confirm_booking,
              fg_color="#1f6aa5",
              hover_color="#155a96",
              text_color="white",
              width=200,
              height=50,
              corner_radius=8).pack(pady=30)

root.mainloop()