import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Car Purchase Portal")
root.geometry("500x500")

# Sample data
vehicles = ["Honda Civic", "Toyota Corolla", "Hyundai Creta", "Tata Nexon", "Kia Seltos"]
colors = ["Red", "Blue", "Black", "White", "Silver"]
variants = ["Base", "Mid", "Top"]

payment_methods = ["Credit Card", "Debit Card", "Net Banking", "UPI", "EMI"]

# Variables
selected_vehicle = tk.StringVar(value=vehicles[0])
selected_color = tk.StringVar(value=colors[0])
selected_variant = tk.StringVar(value=variants[0])
selected_payment = tk.StringVar(value=payment_methods[0])

# Title
tk.Label(root, text="Buy a Car", font=("Helvetica", 16, "bold")).pack(pady=10)

# Vehicle List
tk.Label(root, text="Select a Vehicle:", font=("Arial", 12)).pack()
vehicle_menu = tk.OptionMenu(root, selected_vehicle, *vehicles)
vehicle_menu.pack(pady=5)

# Color Options
tk.Label(root, text="Select Color:", font=("Arial", 12)).pack()
for color in colors:
    tk.Radiobutton(root, text=color, variable=selected_color, value=color).pack(anchor='w')

# Variant Options
tk.Label(root, text="Select Variant:", font=("Arial", 12)).pack(pady=5)
variant_menu = tk.OptionMenu(root, selected_variant, *variants)
variant_menu.pack(pady=5)

# Payment Options
tk.Label(root, text="Select Payment Method:", font=("Arial", 12)).pack(pady=5)
for method in payment_methods:
    tk.Radiobutton(root, text=method, variable=selected_payment, value=method).pack(anchor='w')

# Submit Function
def submit():
    summary = f"""
    Vehicle: {selected_vehicle.get()}
    Color: {selected_color.get()}
    Variant: {selected_variant.get()}
    Payment Method: {selected_payment.get()}
    """
    messagebox.showinfo("Purchase Summary", summary.strip())

# Submit Button
tk.Button(root, text="Buy Now", command=submit, bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

# Run the GUI
root.mainloop()


