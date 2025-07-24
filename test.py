f = ctk.CTkLabel(tframe, text="Citroen", font=("Arial", 12, "bold"))
f.grid(row=0, column=5)
vehicle_menu = ctk.CTkOptionMenu(tframe, values=Citroen, variable=selected_vehicle)
vehicle_menu.grid(row=1, column=5, padx=8)

g = ctk.CTkLabel(tframe, text="Volkswagen", font=("Arial", 12, "bold"))
g.grid(row=0, column=6)
vehicle_menu = ctk.CTkOptionMenu(tframe, values=Volkswagen, variable=selected_vehicle)
vehicle_menu.grid(row=1, column=6, padx=8)

h = ctk.CTkLabel(tframe, text="Skoda", font=("Arial", 12, "bold"))
h.grid(row=0, column=7)
vehicle_menu = ctk.CTkOptionMenu(tframe, values=Skoda, variable=selected_vehicle)
vehicle_menu.grid(row=1, column=7, padx=8)

i = ctk.CTkLabel(tframe, text="Honda", font=("Arial", 12, "bold"))
i.grid(row=0, column=8)
vehicle_menu = ctk.CTkOptionMenu(tframe, values=Honda, variable=selected_vehicle)
vehicle_menu.grid(row=1, column=8, padx=8)

j = ctk.CTkLabel(tframe, text="Toyota", font=("Arial", 12, "bold"))
j.grid(row=0, column=9)
vehicle_menu = ctk.CTkOptionMenu(tframe, values=Toyota, variable=selected_vehicle)
vehicle_menu.grid(row=1, column=9, padx=8)