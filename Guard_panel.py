import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

class LeaveEntryForm:
    def __init__(self, root):
        root.title("Visitor Entry Form")
        root.geometry("1600x900")
        root.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(root, text="Leave Entry Form", font=("Arial", 24, "bold"), bg="#2C3E50", fg="white", pady=20)
        header.pack(fill="x")

        # Owner Info Panel
        emp_frame = tk.LabelFrame(root, text="Owner Info", bg="#ffffff", font=("Arial", 12, "bold"))
        emp_frame.place(x=300, y=130, width=600, height=240)

        # Input fields for Employee Info
        tk.Label(emp_frame, text="Flat_code:", font=("Arial", 12), bg="#ffffff").place(x=10, y=40)
        self.flat_code_entry = tk.Entry(emp_frame, font=("Arial", 12), bd=2, relief="groove")
        self.flat_code_entry.place(x=130, y=40, width=150)

        tk.Checkbutton(emp_frame, text="Search by name", bg="#ffffff").place(x=290, y=40)

        tk.Label(emp_frame, text="Name:", font=("Arial", 12), bg="#ffffff").place(x=10, y=80)
        self.name_entry = tk.Entry(emp_frame, font=("Arial", 12), bd=2, relief="groove")
        self.name_entry.place(x=130, y=80, width=150)

        tk.Label(emp_frame, text="Email:", font=("Arial", 12), bg="#ffffff").place(x=10, y=120)
        self.email_entry = tk.Entry(emp_frame, font=("Arial", 12), bd=2, relief="groove")
        self.email_entry.place(x=130, y=120, width=150)

        tk.Label(emp_frame, text="Mobile Number:", font=("Arial", 12), bg="#ffffff").place(x=320, y=80)
        self.mobile_entry = tk.Entry(emp_frame, font=("Arial", 12), bd=2, relief="groove")
        self.mobile_entry.place(x=440, y=80, width=150)

        tk.Label(emp_frame, text="Members:", font=("Arial", 12), bg="#ffffff").place(x=320, y=120)
        self.members_entry = tk.Entry(emp_frame, font=("Arial", 12), bd=2, relief="groove")
        self.members_entry.place(x=440, y=120, width=150)

        # Leave Entry Panel
        leave_frame = tk.LabelFrame(root, text="Leave Entry", bg="#ffffff", font=("Arial", 12, "bold"))
        leave_frame.place(x=300, y=400, width=600, height=300)

        tk.Label(leave_frame, text="Visitor Name :", font=("Arial", 12), bg="#ffffff").place(x=10, y=20)
        self.visitor_name_entry = tk.Entry(leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.visitor_name_entry.place(x=150, y=20, width=150)

        tk.Label(leave_frame, text="Date :", font=("Arial", 12), bg="#ffffff").place(x=10, y=60)
        current_date = datetime.now()
        self.date_from_entry = DateEntry(
            leave_frame,
            font=("Arial", 12),
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            year=current_date.year,
            month=current_date.month,
            day=current_date.day,
        )
        self.date_from_entry.place(x=150, y=60, width=150)

        tk.Label(leave_frame, text="Remark:", font=("Arial", 12), bg="#ffffff").place(x=310, y=60)
        self.remark_combo = ttk.Combobox(leave_frame, values=["Sanctioned", "Non-Sanctioned", "Cancel"], font=("Arial", 12), state="readonly")
        self.remark_combo.place(x=420, y=60, width=150)

        tk.Label(leave_frame, text="Mobile Number:", font=("Arial", 12), bg="#ffffff").place(x=10, y=100)
        self.v_mobile_entry = tk.Entry(leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.v_mobile_entry.place(x=150, y=100, width=150)

        # Time Entry
        tk.Label(leave_frame, text="Select Time:", font=("Arial", 12), bg="#ffffff").place(x=10, y=140)
        self.hour_combo = ttk.Combobox(leave_frame, values=[f"{i:02}" for i in range(24)], state="readonly", font=("Arial", 12), width=5)
        self.hour_combo.place(x=150, y=140)
        self.hour_combo.set(datetime.now().strftime("%H"))

        tk.Label(leave_frame, text=":", font=("Arial", 12, "bold"), bg="#ffffff").place(x=205, y=140)
        
        self.minute_combo = ttk.Combobox(leave_frame, values=[f"{i:02}" for i in range(60)], state="readonly", font=("Arial", 12), width=5)
        self.minute_combo.place(x=220, y=140)
        self.minute_combo.set(datetime.now().strftime("%M"))

        tk.Label(leave_frame, text="Total Person:", font=("Arial", 12), bg="#ffffff").place(x=310, y=20)
        self.v_total_per_entry = tk.Entry(leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.v_total_per_entry.place(x=420, y=20, width=130)

        

        

        # Operations Panel
        operations_frame = tk.LabelFrame(root, text="Operations", bg="#2980b9", font=("Arial", 12, "bold"))
        operations_frame.place(x=1000, y=130, width=250, height=500)

        tk.Button(operations_frame, text="CLEAR", font=("Arial", 12), bg="#27ae60", fg="white", command=self.clear_form).place(x=30, y=30, width=180, height=40)
        tk.Button(operations_frame, text="SAVE", font=("Arial", 12), bg="#27ae60", fg="white", command=self.save_data).place(x=30, y=90, width=180, height=40)
        tk.Button(operations_frame, text="SEARCH", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=150, width=180, height=40)
        tk.Button(operations_frame, text="UPDATE", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=210, width=180, height=40)
        tk.Button(operations_frame, text="DELETE", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=270, width=180, height=40)
        tk.Button(operations_frame, text="HISTORY", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=330, width=180, height=40)
        tk.Button(operations_frame, text="BACK", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=390, width=180, height=40)
        tk.Button(operations_frame, text="EXIT", font=("Arial", 12), bg="#27ae60", fg="white", command=root.quit).place(x=30, y=450, width=180, height=40)

    def clear_form(self):
        messagebox.showinfo("Clear", "Form cleared!")

    def save_data(self):
        messagebox.showinfo("Save", "Data saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LeaveEntryForm(root)
    root.mainloop()
