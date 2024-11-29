from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from conn import create_connection  # Importing the connection function from conn.py
import os  # for open file Automatically


def fetch_Guard_data():
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM SignUp WHERE type='Guard'")
        flat_owners = cur.fetchall()  # Fetch all rows from the query
        conn.close()
        return flat_owners
    else:
        return []

def create_pdf(data):
    
    try:
        pdf_filename = "Guard_info.pdf"
        
        # Set up the PDF document
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter  # Default size for a letter page is 8.5 x 11 inches
        
        # Title and heading for the PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 50, "Guard's Information")
        
        # Set font for the table content
        c.setFont("Helvetica", 10)

        # Column headers for the table
        headers = ["Guard Number", "Name", "Email", "Passward"]
        header_y_position = height - 100
        c.drawString(50, header_y_position, headers[0])
        c.drawString(150, header_y_position, headers[1])
        c.drawString(250, header_y_position, headers[2])
        c.drawString(420, header_y_position, headers[3])
       
        
        # Draw a line under the headers
        c.line(50, header_y_position - 5, width - 50, header_y_position - 5)
        
        # Add the flat owner data in the table format
        y_position = header_y_position - 20
        for row in data:
            # Flattening each row and inserting into the PDF
            c.drawString(50, y_position, str(row[0]))  # Flat ID
            c.drawString(150, y_position, row[1])      # Name
            c.drawString(250, y_position, row[2])      # Email
            c.drawString(420, y_position, row[3])      # Mobile
           
            # Update y_position for next row
            y_position -= 20
            
            # If we reach the bottom of the page, create a new page
            if y_position < 100:
                c.showPage()  # Creates a new page
                c.setFont("Helvetica", 10)  # Reset the font
                c.drawString(50, height - 50, headers[0])
                c.drawString(150, height - 50, headers[1])
                c.drawString(250, height - 50, headers[2])
                c.drawString(420, height - 50, headers[3])
              
                c.line(50, height - 55, width - 50, height - 55)
                y_position = height - 70  # Reset position for next row

        # Save the PDF file
        c.save()
        os.startfile("Guard_info.pdf")
        print(f"PDF saved as {pdf_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Firest Close file Which is Open in your System")


def main():
    # Fetch data from the database
    guard_info = fetch_Guard_data()
    
    # If data exists, create the PDF
    if guard_info:
        create_pdf(guard_info)
    else:
        print("No flat owner data found.")

if __name__ == "__main__":
    main()
