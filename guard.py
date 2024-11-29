import tkinter as tk
import tkinter.messagebox as messagebox
import conn


class MasterEntryForm(tk.Tk):
    flag = 1

    def __init__(self):
        super().__init__()

        self.title("Master Entry Form")
        # Window size
        window_width = 700
        window_height = 600

        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position to center the window
        x_offset = (screen_width - window_width) // 2
        y_offset = (screen_height - window_height) // 2

        # Set geometry with calculated position
        self.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
        
        self.configure(bg="#F5FFFA")  # Light blue background
            


        # Title Label
        self.title_label = tk.Label(
            self, text="Guard Information Panel",
            font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#4b0082"
        )
        self.title_label.pack(pady=20)

        # Employee Info Panel
        self.emp_info_panel = tk.LabelFrame(
            self, text="Guard Information",
            font=("Arial", 14, "bold"), bg="#ffffff", fg="#000000", relief=tk.GROOVE, bd=3
        )
        self.emp_info_panel.place(x=50, y=80, width=600, height=150)

        # Guard No
        self.bid_code_label = tk.Label(
            self.emp_info_panel, text="Guard No:",
            font=("Arial", 12), bg="#ffffff"
        )
        self.bid_code_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.bid_code_entry = tk.Entry(self.emp_info_panel, font=("Arial", 14), width=20, relief=tk.SUNKEN, bd=2)
        self.bid_code_entry.grid(row=0, column=1, padx=10, pady=10)

        # Guard Name
        self.name_label = tk.Label(
            self.emp_info_panel, text="Name:",
            font=("Arial", 12), bg="#ffffff"
        )#02
        self.name_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.emp_info_panel, font=("Arial", 14), width=20, relief=tk.SUNKEN, bd=2)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)

        # Email
        self.email_label = tk.Label(
            self.emp_info_panel, text="Email:",
            font=("Arial", 12), bg="#ffffff"
        )#10
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.email_entry = tk.Entry(self.emp_info_panel, font=("Arial", 14), width=20, relief=tk.SUNKEN, bd=2)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        # Password
        self.pass_label = tk.Label(
            self.emp_info_panel, text="Password:",
            font=("Arial", 12), bg="#ffffff"
        )
        self.pass_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.pass_entry = tk.Entry(self.emp_info_panel, font=("Arial", 14), show="*", width=20, relief=tk.SUNKEN, bd=2)
        self.pass_entry.grid(row=1, column=3, padx=10, pady=10)

        # Operations Panel
        self.operations_panel = tk.LabelFrame(
            self, text="Operations",
            font=("Arial", 14, "bold"), bg="#ffffff", fg="#000000", relief=tk.GROOVE, bd=3
        )
        self.operations_panel.place(x=50, y=300, width=600, height=150)

        # Buttons
        button_bg = "#4b0082"
        button_fg = "#ffffff"

        self.clear_button = tk.Button(
            self.operations_panel, text="CLEAR", font=("Arial", 12, "bold"),
            width=12, bg=button_bg, fg=button_fg, command=self.clear_fields
        )
        self.clear_button.place(x=30, y=30)

        self.update_button = tk.Button(
            self.operations_panel, text="UPDATE", font=("Arial", 12, "bold"),
            width=12, bg=button_bg, fg=button_fg, command=self.update_data
        )
        self.update_button.place(x=170, y=30)

        self.delete_button = tk.Button(
            self.operations_panel, text="DELETE", font=("Arial", 12, "bold"),
            width=12, bg=button_bg, fg=button_fg, command=self.delete_data
        )
        self.delete_button.place(x=310, y=30)

        self.exit_button = tk.Button(
            self.operations_panel, text="EXIT", font=("Arial", 12, "bold"),
            width=12, bg=button_bg, fg=button_fg, command=self.exit_program
        )
        self.exit_button.place(x=450, y=30)

        # Search Panel
        self.search_panel = tk.LabelFrame(
            self, text="Search",
            font=("Arial", 14, "bold"), bg="#ffebcd", fg="#000000", relief=tk.GROOVE, bd=3
        )

        
        

        # Search Option
        self.search_label = tk.Label(
            self.search_panel, text="Select option to search:",
            font=("Arial", 12), bg="#ffebcd"
        )
        self.search_label.place(x=10, y=10)

        self.search_var = tk.IntVar()
        self.search_by_bid_radio = tk.Radiobutton(
            self.search_panel, text="Guard No", font=("Arial", 12),
            value=1, variable=self.search_var, bg="#ffebcd"
        )
        self.search_by_bid_radio.place(x=200, y=10)

        self.search_by_name_radio = tk.Radiobutton(
            self.search_panel, text="Name", font=("Arial", 12),
            value=2, variable=self.search_var, bg="#ffebcd"
        )
        self.search_by_name_radio.place(x=300, y=10)

        self.search_text = tk.Entry(self.search_panel, font=("Arial", 12), relief=tk.SUNKEN, bd=2)
        self.search_text.place(x=10, y=40, width=500)

        self.search_text.bind("<Return>", self.on_enter_pressed)

        # Listbox to show search results
        self.search_listbox = tk.Listbox(self.search_panel, font=("Arial", 12), height=5)
        self.search_listbox.place(x=10, y=65, width=500, height=80)

        # Bind listbox selection to a function that fills the form
        self.search_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.search_back_button = tk.Button(
            self.search_panel, text="BACK", font=("Arial", 10, "bold"),
            bg=button_bg, fg=button_fg, command=self.back_from_search
        )
        self.search_back_button.place(x=520, y=40)
        #self.operations_panel.place_forget()


        #self.search_panel.place(x=50, y=280, width=600, height=200)










    def back_from_search(self):
        self.search_panel.place_forget()
        self.operations_panel.place(x=50, y=300, width=600, height=150)
        self.flag=1
        self.clear_button.config(state=tk.NORMAL)
        self.update_button.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.NORMAL)
        self.delete_button.config(state=tk.NORMAL)
        
    
    def on_enter_pressed(self,event):
        selected_value = self.search_var.get()
        if selected_value == 1:
            Guard_no = self.search_text.get()
            self.search_database("Guard_no", Guard_no)
        elif selected_value == 2:
            name = self.search_text.get()
            self.search_database("name", name)
        else:
            print("No option selected")

    def search_database(self, search_type, search_value):
        db_conn = conn.create_connection()
        cur = db_conn.cursor()
        query = ""
        if search_type == "Guard_no":
            query = "SELECT * FROM SignUp WHERE id LIKE ?"
        elif search_type == "name":
            query = "SELECT * FROM SignUp WHERE username LIKE ?"

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

            self.operations_panel.place(x=50, y=300, width=600, height=150)
            self.search_text.delete(0, tk.END)
            self.search_listbox.delete(0,tk.END)

    def fill_form_with_data(self, guard_id):
        db_conn = conn.create_connection()
        cur = db_conn.cursor()

        try:
            cur.execute("SELECT * FROM SignUp WHERE id=?", (guard_id,))
            row = cur.fetchone()
            if row:
                # Fill form with the fetched data
                self.bid_code_entry.delete(0, tk.END)
                self.bid_code_entry.insert(0, row[0])

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, row[1])

                self.email_entry.delete(0, tk.END)
                self.email_entry.insert(0, row[2])

                self.pass_entry.delete(0, tk.END)
                self.pass_entry.insert(0, row[3])
                print(row[4])

                

        except Exception as e:
            print(e)
        finally:
            db_conn.close()




    def clear_fields(self):
       
        self.bid_code_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)

    def update_data(self):
        if self.flag==1:
            messagebox.showinfo("info", "Firest search data from database..!")
            self.operations_panel.place_forget()
            self.search_panel.place(x=50, y=280, width=600, height=200)
            self.flag=0


            self.clear_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.exit_button.config(state=tk.DISABLED)
            
        else:
            guard_no = self.bid_code_entry.get()
            name = self.name_entry.get()
            email = self.email_entry.get()
            password = self.pass_entry.get()

            if not all([guard_no, name, email, password]):
                messagebox.showwarning("Warning", "All fields are required!")
                return

            db_conn = conn.create_connection()
            cur = db_conn.cursor()
            try:
                query = """
                    UPDATE SignUp SET username = ?, mail = ?, password = ?
                    WHERE id = ?
                """
                cur.execute(query, (name, email, password, guard_no))
                db_conn.commit()
                messagebox.showinfo("Success", "Data updated successfully!")
                self.flag = 1
                self.clear_fields()

               
                self.clear_button.config(state=tk.NORMAL)
                self.delete_button.config(state=tk.NORMAL)
                self.exit_button.config(state=tk.NORMAL)
                



            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db_conn.close()


        

    def delete_data(self):
        if self.flag==1:
            messagebox.showinfo("info", "Firest search data from database..!")
            self.operations_panel.place_forget()
            self.search_panel.place(x=50, y=280, width=600, height=200)
            self.flag=0


            self.clear_button.config(state=tk.DISABLED)
            self.update_button.config(state=tk.DISABLED)
            self.exit_button.config(state=tk.DISABLED)
            
        else:
            guard_no = self.bid_code_entry.get()

            db_conn = conn.create_connection()
            cur = db_conn.cursor()
            try:
                cur.execute("DELETE FROM SignUp WHERE id = ?", (guard_no,))
                db_conn.commit()
                messagebox.showinfo("Success", "Data deleted successfully!")
                self.clear_fields()
                self.flag=1
                self.clear_button.config(state=tk.NORMAL)
                self.update_button.config(state=tk.NORMAL)
                self.exit_button.config(state=tk.NORMAL)
                



            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                db_conn.close()

        
        

        
        

    def exit_program(self):
        """Exits the program."""
        self.quit()


if __name__ == "__main__":
    app = MasterEntryForm()
    app.mainloop()
