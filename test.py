import customtkinter as ctk
from tkinter import messagebox

# Set default appearance
ctk.set_appearance_mode("dark")  # Optional: dark/light/system
ctk.set_default_color_theme("blue")  # Can also be "green", "dark-blue", etc.

# Main App Class
class CarServiceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Car Service Facility")
        self.geometry("600x500")
        self.configure(bg="black")

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="CAR SERVICE FACILITY", font=("Arial", 24, "bold"), text_color="white")
        self.title_label.pack(pady=20)

        # Frame for input fields
        self.form_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.form_frame.pack(pady=10, padx=20, fill="x")

        # Name Entry
        self.name_entry = self._add_entry("Customer Name")
        # Contact Entry
        self.contact_entry = self._add_entry("Contact Number")
        # Car Model Entry
        self.model_entry = self._add_entry("Car Model")
        # Service Type Dropdown
        self.service_type = ctk.StringVar(value="Oil Change")
        self.service_dropdown = ctk.CTkOptionMenu(self.form_frame, values=["Oil Change", "Brake Check", "Full Service", "Engine Repair"], variable=self.service_type)
        self._add_widget("Service Type", self.service_dropdown)

        # Submit Button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=20)

        # Footer
        self.footer_label = ctk.CTkLabel(self, text="© 2025 Magnus Motors", font=("Arial", 10), text_color="gray")
        self.footer_label.pack(side="bottom", pady=10)

    def _add_entry(self, label_text):
        label = ctk.CTkLabel(self.form_frame, text=label_text, text_color="white")
        label.pack(pady=(10, 0))
        entry = ctk.CTkEntry(self.form_frame, width=400)
        entry.pack(pady=5)
        return entry

    def _add_widget(self, label_text, widget):
        label = ctk.CTkLabel(self.form_frame, text=label_text, text_color="white")
        label.pack(pady=(10, 0))
        widget.pack(pady=5)

    def submit_form(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        model = self.model_entry.get()
        service = self.service_type.get()

        if not all([name, contact, model]):
            messagebox.showwarning("Missing Info", "Please fill in all fields.")
            return

        summary = f"Customer: {name}\nContact: {contact}\nCar Model: {model}\nService: {service}"
        messagebox.showinfo("Booking Confirmed", summary)
        self._clear_form()

    def _clear_form(self):
        self.name_entry.delete(0, 'end')
        self.contact_entry.delete(0, 'end')
        self.model_entry.delete(0, 'end')
        self.service_type.set("Oil Change")

# Run the App
if __name__ == "__main__":
    app = CarServiceApp()
    app.mainloop()
