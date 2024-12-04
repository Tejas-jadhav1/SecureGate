import tkinter as tk
from tkinter import messagebox
import subprocess

def submit_flat_id():
    flat_id = entry_flat_id.get()
    try:
        subprocess.Popen(["python", "view_flate_wise.py"])  
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Owner.py: {e}")

root = tk.Tk()
root.title("Flat Wise Report")

window_width = 400
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

label_flat_id = tk.Label(root, text="Enter Flat ID:", font=("Arial", 14))
label_flat_id.pack(pady=10)

entry_flat_id = tk.Entry(root, font=("Arial", 14), width=20)
entry_flat_id.pack(pady=5)

# Create and place the Submit button
submit_button = tk.Button(
    root, 
    text="Submit", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#4CAF50", 
    activebackground="#45a049", 
    activeforeground="white", 
    cursor="hand2", 
    command=submit_flat_id
)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
