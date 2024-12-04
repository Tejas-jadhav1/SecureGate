import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
import subprocess  # Import subprocess to run external scripts

class MainApp:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("Admin Section")
        self.root.geometry("1600x900")
        
        # Main frame and panel setup
        self.main_frame = tk.Frame(self.root, bg="#e0e0e0", bd=2, relief="solid")
        self.main_frame.pack(fill="both", expand=True)

        self.panel = tk.Frame(self.main_frame, bg="white", bd=2, relief="ridge")
        self.panel.place(relx=0, rely=0, width=1600, height=900)

        # Background Image
        self.image = Image.open("admin.jpg")
        self.image = self.image.resize((1600, 900))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.panel, image=self.photo)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create the menu bar
        self.create_menubar()

    def create_menubar(self):
        # Initialize menu bar
        menubar = Menu(self.root)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Manage Owner", command=self.Manage_owner)
        file_menu.add_command(label="View Owner", command=self.open_action)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Owner Info", menu=file_menu)

        # Edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="manage Guard", command=self.manage_guard)
        edit_menu.add_command(label="view Guard", command=self.view_guard)
        menubar.add_cascade(label="Guard Info", menu=edit_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Date_Wise")
        help_menu.add_command(label="Flat_Wise",command=self.flat_report)
        help_menu.add_command(label="Month_Wise")

        menubar.add_cascade(label="Report", menu=help_menu)

        # Attach the menu to the root window
        self.root.config(menu=menubar)


    def flat_report(self):
        try:
            subprocess.Popen(["python", "flat_rep.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Owner.py: {e}")


    def Manage_owner(self):
        try:
            subprocess.Popen(["python", "Owner.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Owner.py: {e}")

    
    def open_action(self):
        try:
            subprocess.Popen(["python", "view_owner.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open view_owner.py: {e}")

    def manage_guard(self):
        try:
            subprocess.Popen(["python", "guard.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open Owner.py: {e}")

    def view_guard(self):
        try:
            subprocess.Popen(["python", "view_guard.py"])  
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open view_owner.py: {e}")

    def date_action(self):
        
        messagebox.showinfo("About", "This is an admin section application with a custom menubar.")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
