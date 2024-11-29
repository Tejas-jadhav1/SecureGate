import tkinter as tk

root = tk.Tk()
root.title("Login page")
root.geometry("1300x900")  # Set the size of the window


panel = tk.Frame(root, bg="lightblue", bd=2, relief="solid")
panel.pack(padx=0, pady=0, fill="both", expand=True)

# Add some widgets to the panel
label = tk.Label(panel, text="Come to Our ", bg="lightblue")
label.pack(pady=20)

button = tk.Button(panel, text="Click Me")
button.pack(pady=10)

# Run the application
root.mainloop()



# keep in mind i am trying to cretae desktop application for secureGate in which i am trying to create login and sign up page in above panel i provided some panel code add another panel in above panel in middle give creative way for login and sign up in 