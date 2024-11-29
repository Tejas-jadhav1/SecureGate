import tkinter as tk
import tkinter.messagebox as messagebox

import conn
from conn import owner_database


class MasterEntryForm(tk.Tk):
    flag=1
    def __init__(self):
        super().__init__()

        self.title("Master Entry Form")
        self.geometry("600x500")

        # Main Frame
        self.main_frame = tk.Frame(self, bg="pink")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = tk.Label(self.main_frame, text="OWNER MASTER ENTRY FORM", font=("Arial", 20, "bold"), bg="pink")
        self.title_label.place(x=130, y=20)

        # Employee Info Panel
        self.emp_info_panel = tk.LabelFrame(self.main_frame, text="Owner Info", font=("Arial", 12), bg="white")
        self.emp_info_panel.place(x=30, y=80, width=550, height=160)

        # Flat No (Bid Code)
        self.bid_code_label = tk.Label(self.emp_info_panel, text="Flat No:", font=("Arial", 12), bg="white")
        self.bid_code_label.place(x=20, y=20)
        self.bid_code_entry = tk.Entry(self.emp_info_panel, font=("Arial", 12))
        self.bid_code_entry.place(x=90, y=20)

        # Name
        self.name_label = tk.Label(self.emp_info_panel, text="Name:", font=("Arial", 12), bg="white")
        self.name_label.place(x=30, y=60)
        self.name_entry = tk.Entry(self.emp_info_panel, font=("Arial", 12))
        self.name_entry.place(x=90, y=60)

        # Members (Designation)
        self.designation_label = tk.Label(self.emp_info_panel, text="Members:", font=("Arial", 12), bg="white")
        self.designation_label.place(x=15, y=100)
        self.members_entry = tk.Entry(self.emp_info_panel, font=("Arial", 12))  # New Entry for Members
        self.members_entry.place(x=90, y=100)

        # Mobile Number
        self.mob_label = tk.Label(self.emp_info_panel, text="Mob No:", font=("Arial", 12), bg="white")
        self.mob_label.place(x=260, y=20)

        # Function to allow only numeric input and limit the size to 10 digits
        def on_validate_mobile_number(input_value):
            if input_value.isdigit() or input_value == "":  # Only digits allowed
                if len(input_value) <= 10:  # Limit input to 10 digits
                    return True
                else:
                    return False
            else:
                return False

        # Register validation function for mobile number entry
        validate_mobile = self.register(on_validate_mobile_number)
        self.mob_entry = tk.Entry(self.emp_info_panel, font=("Arial", 12), validate="key", validatecommand=(validate_mobile, '%P'))
        self.mob_entry.place(x=320, y=20)

        # Email
        self.email_label = tk.Label(self.emp_info_panel, text="Email:", font=("Arial", 12), bg="white")
        self.email_label.place(x=260, y=60)
        self.email_entry = tk.Entry(self.emp_info_panel, font=("Arial", 12))
        self.email_entry.place(x=320, y=60)

        # Operations Panel
        self.operations_panel = tk.LabelFrame(self.main_frame, text="Operations", font=("Arial", 12), bg="white")
        self.operations_panel.place(x=30, y=260, width=550, height=150)

        # Buttons
        self.clear_button = tk.Button(self.operations_panel, text="CLEAR", font=("Arial", 12), width=12, command=self.clear_fields)
        self.clear_button.place(x=80, y=30)

        self.save_button = tk.Button(self.operations_panel, text="SAVE", font=("Arial", 12), width=12, command=self.save_data)
        self.save_button.place(x=200, y=30)

        self.back_button = tk.Button(self.operations_panel, text="BACK", font=("Arial", 12), width=12, command=self.go_back)
        self.back_button.place(x=320, y=30)

        self.update_button = tk.Button(self.operations_panel, text="UPDATE", font=("Arial", 12), width=12, command=self.update_data)
        self.update_button.place(x=80, y=70)

        self.delete_button = tk.Button(self.operations_panel, text="DELETE", font=("Arial", 12), width=12, command=self.delete_data)
        self.delete_button.place(x=200, y=70)

        self.exit_button = tk.Button(self.operations_panel, text="EXIT", font=("Arial", 12), width=12, command=self.exit_program)
        self.exit_button.place(x=320, y=70)

        self.operations_panel.place_forget()  # Hides the widget

        # Search Panel
        self.search_panel = tk.LabelFrame(self.main_frame, text="SEARCH", font=("Arial", 12), bg="yellow")
        self.search_panel.place(x=30, y=260, width=550, height=200)

        # Search Option
        self.search_label = tk.Label(self.search_panel, text="SELECT OPTION TO SEARCH:", font=("Arial", 12), bg="yellow")
        self.search_label.place(x=30, y=20)

        self.search_var = tk.IntVar()

        # Create the "Bid No" radio button and associate it with the variable
        self.search_by_bid_radio = tk.Radiobutton(self.search_panel, text="Bid No", font=("Arial", 12), value=1, variable=self.search_var)
        self.search_by_bid_radio.place(x=210, y=20)

        # Create the "Name" radio button and associate it with the same variable
        self.search_by_name_radio = tk.Radiobutton(self.search_panel, text="Name", font=("Arial", 12), value=2, variable=self.search_var)
        self.search_by_name_radio.place(x=300, y=20)

        # Back Button
        self.search_back_button = tk.Button(self.search_panel, text="BACK", font=("Arial", 12), command=self.back_from_search)
        self.search_back_button.place(x=390, y=20)

        # Search Text Field
        self.search_text = tk.Entry(self.search_panel, font=("Arial", 12))
        self.search_text.place(x=30, y=60, width=460, height=30)

        self.search_text.bind("<Return>", self.on_enter_pressed)

        # Listbox to show search results
        self.search_listbox = tk.Listbox(self.search_panel, font=("Arial", 12), height=5)
        self.search_listbox.place(x=30, y=95, width=460, height=80)

        # Bind listbox selection to a function that fills the form
        self.search_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.search_panel.place_forget()
        self.operations_panel.place(x=30, y=260, width=550, height=210)

    # Placeholder Functions for Buttons
    def save_data(self):
        db_conn = conn.create_connection()
        cur = db_conn.cursor()

        try:
            owner_database()  # Ensure database and table creation
        except Exception as e:
            print(e)

        flat = self.bid_code_entry.get()
        name = self.name_entry.get()
        mail = self.email_entry.get()
        mob = self.mob_entry.get()
        member = self.members_entry.get()

        if flat and name and mail and mob and member:
            try:
                cur.execute("INSERT INTO flat_owner (flat_id,name,email,mobile,member) VALUES (?, ?, ?, ?, ?)", 
                            (flat, name, mail, mob, member))
                db_conn.commit()
                messagebox.showinfo("Success", "Information saved Successfully !")
                self.clear_fields()
            except Exception as ee:
                messagebox.showinfo("Error", "Duplicate Flat_number Found")
            finally:
                db_conn.close()
        else:
            messagebox.showinfo("Error", "All fields are required")

    def clear_fields(self):
        self.bid_code_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.mob_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.members_entry.delete(0, tk.END)

    def go_back(self):
        pass

    def update_data(self):
        if self.flag==1:
            messagebox.showinfo("info", "Firest search data from database..!")
            self.operations_panel.place_forget()
            self.search_panel.place(x=30, y=260, width=550, height=210)
            self.flag=0

            self.save_button.config(state=tk.DISABLED)
            self.clear_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.exit_button.config(state=tk.DISABLED)
            self.back_button.config(state=tk.DISABLED)
            
        else:
            flat = self.bid_code_entry.get()    
            name = self.name_entry.get()        
            mail = self.email_entry.get()       
            mob = self.mob_entry.get()          
            member = self.members_entry.get()   
            db_conn = conn.create_connection()
            cur = db_conn.cursor()
            try:
                query = """
                    UPDATE flat_owner
                    SET name = ?, email = ?, mobile = ?, member = ?
                    WHERE flat_id = ?
                """
                
                # Execute the query with the values from the entry fields
                cur.execute(query, (name, mail, mob, member, flat))
                
                # Commit the transaction
                db_conn.commit()
                
                # Provide feedback to the user
                messagebox.showinfo("Success", f"Data updated successfully for flat {name} and it's flat number {flat}!")
                self.flag=1
                self.clear_fields()

                self.save_button.config(state=tk.NORMAL)
                self.clear_button.config(state=tk.NORMAL)
                self.delete_button.config(state=tk.NORMAL)
                self.exit_button.config(state=tk.NORMAL)
                self.back_button.config(state=tk.NORMAL)
                
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred while updating: {str(e)}")

    def on_enter_pressed(self,event):
        selected_value = self.search_var.get()
        if selected_value == 1:
            bid = self.search_text.get()
            self.search_database("bid", bid)
        elif selected_value == 2:
            name = self.search_text.get()
            self.search_database("name", name)
        else:
            print("No option selected")

    def search_database(self, search_type, search_value):
        db_conn = conn.create_connection()
        cur = db_conn.cursor()
        query = ""
        if search_type == "bid":
            query = "SELECT * FROM flat_owner WHERE flat_id LIKE ?"
        elif search_type == "name":
            query = "SELECT * FROM flat_owner WHERE name LIKE ?"

        try:
            cur.execute(query, ('%' + search_value + '%',))
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
            self.operations_panel.place(x=30, y=260, width=550, height=210)
            self.search_text.delete(0, tk.END)
            self.search_listbox.delete(0,tk.END)

    def fill_form_with_data(self, flat_id):
        db_conn = conn.create_connection()
        cur = db_conn.cursor()

        try:
            cur.execute("SELECT * FROM flat_owner WHERE flat_id=?", (flat_id,))
            row = cur.fetchone()
            if row:
                # Fill form with the fetched data
                self.bid_code_entry.delete(0, tk.END)
                self.bid_code_entry.insert(0, row[0])

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, row[1])

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, row[2])

                self.mob_entry.delete(0, tk.END)
                self.mob_entry.insert(0, row[3])

                self.members_entry.delete(0, tk.END)
                self.members_entry.insert(0, row[4])

        except Exception as e:
            print(e)
        finally:
            db_conn.close()

    def delete_data(self):
        if self.flag==1:
            messagebox.showinfo("info", "Firest search data from database..!")
            self.operations_panel.place_forget()
            self.search_panel.place(x=30, y=260, width=550, height=210)
            self.flag=0

            self.save_button.config(state=tk.DISABLED)
            self.clear_button.config(state=tk.DISABLED)
            self.update_button.config(state=tk.DISABLED)
            self.exit_button.config(state=tk.DISABLED)
            self.back_button.config(state=tk.DISABLED)
            
        else:
            flat = self.bid_code_entry.get()    
            
            db_conn = conn.create_connection()
            cur = db_conn.cursor()

            try:
        
                cur.execute("DELETE FROM flat_owner WHERE flat_id = ?", (flat,))
                
                
                # Commit the transaction
                db_conn.commit()
                
                # Provide feedback to the user
                messagebox.showinfo("Success", f"Data Deleted successfully for flat number {flat}!")
                self.flag=1
                self.clear_fields()

                self.save_button.config(state=tk.NORMAL)
                self.clear_button.config(state=tk.NORMAL)
                self.update_button.config(state=tk.NORMAL)
                self.exit_button.config(state=tk.NORMAL)
                self.back_button.config(state=tk.NORMAL)
                
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred while deleting: {str(e)}")

    def exit_program(self):
        self.quit()

    def back_from_search(self):
        self.search_panel.place_forget()
        self.operations_panel.place(x=30, y=260, width=550, height=210)
       




if __name__ == "__main__":
    app = MasterEntryForm()
    app.mainloop()
