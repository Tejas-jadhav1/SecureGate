import tkinter as tk
from tkinter import messagebox

def submit_flat_id():
    flat_id = entry_flat_id.get().strip()
    if flat_id:
        messagebox.showinfo("Success", f"Flat ID {flat_id} submitted successfully!")
    else:
        messagebox.showerror("Error", "Please enter a Flat ID.")

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
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=submit_flat_id)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
