import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from conn import create_connection  # Importing the connection function from conn.py
import subprocess


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

        self.flat_code_entry.bind("<Return>", self.on_enter_pressed)

        check_by_name_button = tk.Button(emp_frame,text="Search by Name",font=("Arial", 12, "bold"),fg="white",bg="#2980b9",relief="raised",             
                                 width=15, height=1,command=self.chk)  

        check_by_name_button.place(x=290, y=40)  # Position the button


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

        
# ----------------------------------------------Visitor Panel--------------------------------------------------------

        self.leave_frame = tk.LabelFrame(root, text="VISITOR FORM ENTRY", bg="#ffffff", font=("Arial", 12, "bold"))
        self.leave_frame.place(x=300, y=400, width=600, height=230)

        tk.Label(self.leave_frame, text="Visitor Name :", font=("Arial", 12), bg="#ffffff").place(x=10, y=20)
        self.visitor_name_entry = tk.Entry(self.leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.visitor_name_entry.place(x=150, y=20, width=150)

        tk.Label(self.leave_frame, text="Date :", font=("Arial", 12), bg="#ffffff").place(x=10, y=60)
        current_date = datetime.now()
        self.date_from_entry = DateEntry(
            self.leave_frame,
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

        tk.Label(self.leave_frame, text="Remark:", font=("Arial", 12), bg="#ffffff").place(x=310, y=60)
        self.remark_combo = ttk.Combobox(self.leave_frame, values=["Friends", "Relativies", "E-services"], font=("Arial", 12), state="readonly")
        self.remark_combo.place(x=420, y=60, width=150)

        tk.Label(self.leave_frame, text="Mobile Number:", font=("Arial", 12), bg="#ffffff").place(x=10, y=100)
        self.v_mobile_entry = tk.Entry(self.leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.v_mobile_entry.place(x=150, y=100, width=150)

        # Time Entry
        tk.Label(self.leave_frame, text="Select Time:", font=("Arial", 12), bg="#ffffff").place(x=10, y=140)
        self.hour_combo = ttk.Combobox(self.leave_frame, values=[f"{i:02}" for i in range(24)], state="readonly", font=("Arial", 12), width=5)
        self.hour_combo.place(x=150, y=140)
        self.hour_combo.set(datetime.now().strftime("%H"))

        tk.Label(self.leave_frame, text=":", font=("Arial", 12, "bold"), bg="#ffffff").place(x=205, y=140)
        
        self.minute_combo = ttk.Combobox(self.leave_frame, values=[f"{i:02}" for i in range(60)], state="readonly", font=("Arial", 12), width=5)
        self.minute_combo.place(x=220, y=140)
        self.minute_combo.set(datetime.now().strftime("%M"))

        tk.Label(self.leave_frame, text="Total Person:", font=("Arial", 12), bg="#ffffff").place(x=310, y=20)
        self.v_total_per_entry = tk.Entry(self.leave_frame, font=("Arial", 12), bd=2, relief="groove")
        self.v_total_per_entry.place(x=420, y=20, width=130)

 #-----------------------------------------Search Panel------------------------------------------------------#       

        # Search Panel
        self.search_panel = tk.LabelFrame(root, text="SEARCH", font=("Arial", 12), bg="#FFFFF0")
        #self.search_panel.place(x=30, y=260, width=550, height=200)

        # Search Option
        self.search_label = tk.Label(self.search_panel, text="  SEARCH OWNER'S", font=("Arial", 14))
        self.search_label.place(x=90, y=20)

        
        # Back Button
        self.search_back_button = tk.Button(self.search_panel, text="BACK", font=("Arial", 12),command=self.go_back)
        self.search_back_button.place(x=390, y=20)

        # Search Text Field
        self.search_text = tk.Entry(self.search_panel, font=("Arial", 12))
        self.search_text.place(x=30, y=60, width=460, height=30)

        self.search_text.bind("<Return>", self.on_enter_pressed_name)

        # Listbox to show search results
        self.search_listbox = tk.Listbox(self.search_panel, font=("Arial", 12), height=5)
        self.search_listbox.place(x=30, y=95, width=460, height=80)

        # Bind listbox selection to a function that fills the form
        self.search_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        


#----------------------------------------Operation panel----------------------------------------------------#

        # Operations Panel
        operations_frame = tk.LabelFrame(root, text="Operations", bg="#2980b9", font=("Arial", 12, "bold"))
        operations_frame.place(x=1000, y=130, width=250, height=500)

        tk.Button(operations_frame, text="CLEAR", font=("Arial", 12), bg="#27ae60", fg="white", command=self.clear_form).place(x=30, y=30, width=180, height=40)
        tk.Button(operations_frame, text="SAVE", font=("Arial", 12), bg="#27ae60", fg="white", command=self.save_data).place(x=30, y=90, width=180, height=40)
        tk.Button(operations_frame, text="TODAY_ENTRY", font=("Arial", 12), bg="#27ae60", fg="white",command=self.today_entry).place(x=30, y=150, width=180, height=40)
        tk.Button(operations_frame, text="UPDATE", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=210, width=180, height=40)
        tk.Button(operations_frame, text="DELETE", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=270, width=180, height=40)
        tk.Button(operations_frame, text="HISTORY", font=("Arial", 12), bg="#27ae60", fg="white", command=self.history_form).place(x=30, y=330, width=180, height=40)
        tk.Button(operations_frame, text="BACK", font=("Arial", 12), bg="#27ae60", fg="white").place(x=30, y=390, width=180, height=40)
        tk.Button(operations_frame, text="EXIT", font=("Arial", 12), bg="#27ae60", fg="white", command=root.quit).place(x=30, y=450, width=180, height=40)


    def chk(self):
        self.leave_frame.place_forget() 
        self.search_panel.place(x=300, y=400, width=600, height=230)

    def go_back(self):
        self.search_panel.place_forget()
        self.leave_frame.place(x=300, y=400, width=600, height=230)

    def today_entry(self):
        try:
            subprocess.Popen(["python", "view_today.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Owner.py: {e}")

    def history_form(self):
        try:
            subprocess.Popen(["python", "view_history.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Owner.py: {e}")













        

    def clear_form(self):
        self.flat_code_entry.delete(0, tk.END)
        self.members_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.v_mobile_entry.delete(0, tk.END)
        self.v_total_per_entry.delete(0, tk.END)
        self.visitor_name_entry.delete(0, tk.END)
        self.name_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)

    def save_data(self):
        connection = create_connection()

        try:
            flat_code = self.flat_code_entry.get()  
            visitor_name = self.visitor_name_entry.get()
            date = self.date_from_entry.get_date()
            mobile=self.v_mobile_entry.get()
            hour = self.hour_combo.get()
            minute = self.minute_combo.get()
            time = hour + ":" + minute 
            remark = self.remark_combo.get()
            total_person = self.v_total_per_entry.get()

            cursor = connection.cursor()
            query = """
                INSERT INTO visitor (name, tot_person, date, mob_num, time, remark, flat_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (visitor_name, total_person, date, mobile, time, remark, flat_code))
            connection.commit()

        except Exception as e:
            print(f"Error saving data: {e}")
        finally:
            connection.close()
        messagebox.showinfo("Save", "Data saved successfully!")
        self.clear_form()

    def on_enter_pressed(self,event):
        try:
            db_conn = create_connection()
        except Exception as e:
            print(e)
        cur = db_conn.cursor()
        flat_no=self.flat_code_entry.get()

        try:
            cur.execute("SELECT * FROM flat_owner WHERE flat_id=?", (flat_no,))
            row = cur.fetchone()
            self.clear_form()
            if row:
                self.flat_code_entry.delete(0,tk.END)
                self.flat_code_entry.insert(0, row[0])

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, row[1])

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, row[2])

                self.mobile_entry.delete(0, tk.END)
                self.mobile_entry.insert(0, row[3])

                self.members_entry.delete(0, tk.END)
                self.members_entry.insert(0, row[4])

        except Exception as e:
            print(e)
        finally:
            db_conn.close()

    def on_enter_pressed_name(self,event):
        db_conn = create_connection()
        cur = db_conn.cursor()
        query = "SELECT * FROM flat_owner WHERE name LIKE ?"
        s1=self.search_text.get()
        try:
            cur.execute(query, ('%' + s1+ '%',))
            results = cur.fetchall()
            self.search_listbox.delete(0, tk.END)
            for row in results:
                self.search_listbox.insert(tk.END, f"{row[0]} - {row[1]}")  
        except Exception as e:
            print(e)
        finally:
            db_conn.close()

    def on_listbox_select(self, event):
        selected_index = self.search_listbox.curselection()
        if selected_index:
            selected_item = self.search_listbox.get(selected_index)
            flat_id = selected_item.split(" - ")[0]  
            self.fill_form_with_data(flat_id)
            self.search_panel.place_forget()
            self.leave_frame.place(x=300, y=400, width=600, height=230)
            self.search_text.delete(0, tk.END)
            self.search_listbox.delete(0,tk.END)

    def fill_form_with_data(self, flat_id):
        db_conn = create_connection()
        cur = db_conn.cursor()

        try:
            cur.execute("SELECT * FROM flat_owner WHERE flat_id=?", (flat_id,))
            row = cur.fetchone()
            if row:
                self.flat_code_entry.delete(0,tk.END)
                self.flat_code_entry.insert(0, row[0])

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, row[1])

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, row[2])

                self.mobile_entry.delete(0, tk.END)
                self.mobile_entry.insert(0, row[3])

                self.members_entry.delete(0, tk.END)
                self.members_entry.insert(0, row[4])

        except Exception as e:
            print(e)
        finally:
            db_conn.close()








if __name__ == "__main__":
    root = tk.Tk()
    app = LeaveEntryForm(root)
    root.mainloop()
