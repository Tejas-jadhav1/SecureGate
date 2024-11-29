import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from main import * # Import MainApp from main.py


import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog, ttk

import random
import sqlite3
import conn  # Import the conn module for database operations
import re

class SecureGate:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureGate - Login and Sign Up")
        self.root.geometry("1600x1200")

        # Email setup (initialize once)
        self.sender_email = 'dhirajsalunke7350@gmail.com'
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.sender_password = 'cyba jydk cujw swpw'

        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.starttls()
            self.server.login(self.sender_email, self.sender_password)
            print("Email server connected successfully!")
        except Exception as e:
            print(f"Failed to connect to email server: {e}")
            self.server = None  # If connection fails, set server to None for safety

        # Main panel
        self.main_panel = tk.Frame(self.root, bg="#f0f0f0", bd=2, relief="solid")
        self.main_panel.pack(padx=0, pady=0, fill="both", expand=True)

        # Background Image
        self.image = Image.open("login.webp")
        self.image = self.image.resize((1600, 900))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.main_panel, image=self.photo)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Header
        self.header_label = tk.Label(self.main_panel, text="Welcome to SecureGate", bg="#f0f0f0", font=("Arial", 30))
        self.header_label.pack(pady=20)

        # Panel for Login/Sign-Up Forms
        self.panel = tk.Frame(self.main_panel, bg="white", bd=2, relief="ridge")
        self.panel.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

        # Show the login form by default
        self.show_login()

    def show_login(self):
        self.clear_panel()

        login_label = tk.Label(self.panel, text="Login", bg="#ffffff", font=("Arial", 24, "bold"))
        login_label.pack(pady=(30, 10))

        # Username label and entry for login
        login_username_label = tk.Label(self.panel, text="Mail:", bg="#ffffff", font=("Arial", 14))
        login_username_label.pack(anchor="w", padx=20)
        self.login_username_entry = tk.Entry(self.panel, font=("Arial", 14), bd=2, relief="groove")
        self.login_username_entry.pack(padx=20, pady=(0, 20), fill='x')

        # Password label and entry for login
        login_password_label = tk.Label(self.panel, text="Password:", bg="#ffffff", font=("Arial", 14))
        login_password_label.pack(anchor="w", padx=20)
        self.login_password_entry = tk.Entry(self.panel, show="*", font=("Arial", 14), bd=2, relief="groove")
        self.login_password_entry.pack(padx=20, pady=(0, 20), fill='x')

        # Type label and dropdown for login
        login_type_label = tk.Label(self.panel, text="Type:", bg="#ffffff", font=("Arial", 14))
        login_type_label.pack(anchor="w", padx=20)
        self.login_type_combobox = ttk.Combobox(self.panel, values=["Admin", "Guard"], font=("Arial", 14))
        self.login_type_combobox.pack(padx=20, pady=(0, 20), fill='x')

        # Login button
        login_button = tk.Button(self.panel, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.login_action)
        login_button.pack(pady=20, padx=20, fill='x')

        # Switch to Sign Up
        switch_to_signup = tk.Button(self.panel, text="Don't have an account? Sign Up", font=("Arial", 12), bg="#ffffff", fg="#4CAF50", command=self.show_signup)
        switch_to_signup.pack(pady=(10, 30))

    def show_signup(self):
        self.clear_panel()

        signup_label = tk.Label(self.panel, text="Sign Up", bg="#ffffff", font=("Arial", 24, "bold"))
        signup_label.pack(pady=(30, 10))

        # Username label and entry for sign-up
        signup_username_label = tk.Label(self.panel, text="Username:", bg="#ffffff", font=("Arial", 14))
        signup_username_label.pack(anchor="w", padx=20)
        self.signup_username_entry = tk.Entry(self.panel, font=("Arial", 14), bd=2, relief="groove")
        self.signup_username_entry.pack(padx=20, pady=(0, 10), fill='x')

        # Email label and entry for sign-up
        signup_email_label = tk.Label(self.panel, text="Email:", bg="#ffffff", font=("Arial", 14))
        signup_email_label.pack(anchor="w", padx=20)
        self.signup_email_entry = tk.Entry(self.panel, font=("Arial", 14), bd=2, relief="groove")
        self.signup_email_entry.pack(padx=20, pady=(0, 10), fill='x')

        # Password label and entry for sign-up
        signup_password_label = tk.Label(self.panel, text="Password:", bg="#ffffff", font=("Arial", 14))
        signup_password_label.pack(anchor="w", padx=20)
        self.signup_password_entry = tk.Entry(self.panel, show="*", font=("Arial", 14), bd=2, relief="groove")
        self.signup_password_entry.pack(padx=20, pady=(0, 10), fill='x')

        # Type label and dropdown for sign-up
        signup_type_label = tk.Label(self.panel, text="Type:", bg="#ffffff", font=("Arial", 14))
        signup_type_label.pack(anchor="w", padx=20)
        self.signup_type_combobox = ttk.Combobox(self.panel, values=["Admin", "Guard"], font=("Arial", 14))
        self.signup_type_combobox.pack(padx=20, pady=(0, 20), fill='x')

        # Sign Up button
        signup_button = tk.Button(self.panel, text="Sign Up", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.signup_action)
        signup_button.pack(pady=20, padx=20, fill='x')

        # Switch to Login
        switch_to_login = tk.Button(self.panel, text="Already have an account? Login", font=("Arial", 12), bg="#ffffff", fg="#4CAF50", command=self.show_login)
        switch_to_login.pack(pady=(10, 30))

    def clear_panel(self):
        for widget in self.panel.winfo_children():
            widget.destroy()

    def login_action(self):
        email = self.login_username_entry.get()
        password = self.login_password_entry.get()
        user_type = self.login_type_combobox.get()

        g_patt=r"^\w+[@][a-z]+[.][a-z]{2,3}$"
        pass_patt = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"

        if   not email or not password or not user_type:
            messagebox.showerror("REQUIRED","All Field Required..")

        elif not re.match(g_patt, email):
            messagebox.showerror("Validation Result", "Invalid Email Address")
        elif not re.match(pass_patt,password):
            messagebox.showwarning("passward Mismatch","Passward Contain at least one CAPITAL,one SPECIAL SYMBOL,one DIGIT and LENGTH>6")
        else:
            db_conn = conn.create_connection()
            cur = db_conn.cursor()
            cur.execute("SELECT * FROM SignUp WHERE mail = ? AND password = ? AND type = ?", (email, password, user_type))
            user = cur.fetchone()
            db_conn.close()

            if user:
                messagebox.showinfo("Success", f"Welcome, {user_type} {email}!")
                self.root.destroy()
                main_root = tk.Tk()
                MainApp(main_root)
            else:
                messagebox.showinfo("Error", "Invalid credentials or user type!")
            
    def send_email(self, receiver_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            self.server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")





    def signup_action(self):
        

        # Get the email entered by the user
        receiver_email = self.signup_email_entry.get()
        

        db_conn = conn.create_connection()
        cur = db_conn.cursor()
        cur.execute("SELECT mail FROM SignUp WHERE mail = ?", (receiver_email,))
        user = cur.fetchone()
        db_conn.close()

        if user:
            messagebox.showinfo("Error", f"Already, {receiver_email} is available!")
        else:
            if self.server:
                username = self.signup_username_entry.get()
                email = self.signup_email_entry.get()
                password = self.signup_password_entry.get()
                user_type = self.signup_type_combobox.get()

                g_patt=r"^\w+[@][a-z]+[.][a-z]{2,3}$"
                pass_patt = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"

                if not username or not email or not password or not user_type:
                    messagebox.showerror("REQUIRED","All Field Required..")

                elif not re.match(g_patt, email):
                    messagebox.showerror("Validation Result", "Invalid Email Address")
                elif not re.match(pass_patt,password):
                    messagebox.showwarning("passward Mismatch","Passward Contain at least one CAPITAL,one SPECIAL SYMBOL,one DIGIT and LENGTH>6")
                
                else:
                    random_otp = random.randint(1000, 9999)
                    print(f"Generated OTP: {random_otp}")

                    subject = 'OTP Verification for SecureGate Signup'
                    message = f'Your OTP for signup at SecureGate is: {random_otp}'
                    
                    self.send_email(receiver_email, subject, message)
                    # Ask the user to enter the OTP
                    entered_otp = simpledialog.askstring("Input", "Enter your OTP:", parent=self.root)
                    # Validate the OTP
                    if entered_otp == str(random_otp):
                        # OTP is correct, proceed to save user
                        db_conn = conn.create_connection()
                        cur = db_conn.cursor()

                        
                        
                        if user_type == "Admin":
                            Owner_otp= simpledialog.askstring("Input", "Enter your OTP for Admin Login:", parent=self.root)
                            if Owner_otp=="7032":
                                try:
                                    cur.execute("INSERT INTO SignUp (username, mail, password, type) VALUES (?, ?, ?, ?)", 
                                                (username, email, password, user_type))
                                    db_conn.commit()
                                    messagebox.showinfo("Success", "Account created successfully!")
                                    self.show_login()
                                except sqlite3.IntegrityError:
                                    messagebox.showinfo("Error", "Email already registered!")
                                finally:
                                    db_conn.close()
                            else:
                                messagebox.showinfo("Error", "ADMIN OTP WRONG !!")
                        else:
                            try:
                                cur.execute("INSERT INTO SignUp (username, mail, password, type) VALUES (?, ?, ?, ?)", 
                                            (username, email, password, user_type))
                                db_conn.commit()
                                messagebox.showinfo("Success", "Account created successfully!")
                                self.show_login()
                            except sqlite3.IntegrityError:
                                messagebox.showinfo("Error", "Email already registered!")
                            finally:
                                db_conn.close()
                    else:
                        messagebox.showinfo("Error", "OTP not matched")
            else:
                messagebox.showinfo("Error", "Server Down!")
   
       

        


# Initialize the database
conn.initialize_database()

# Main execution
root = tk.Tk()
app = SecureGate(root)
root.mainloop()
