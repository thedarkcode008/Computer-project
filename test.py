import customtkinter as ctk

app = ctk.CTk()
app.title("CustomTkinter App")

# Maximize on start
app.after(0, lambda: app.state('zoomed'))

# Add button to close
btn = ctk.CTkButton(app, text="Close", command=app.destroy)
btn.pack(pady=20)

app.mainloop()