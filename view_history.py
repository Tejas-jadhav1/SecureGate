from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from conn import create_connection
import os

def fetch_Guard_data():
    conn = create_connection()
    if conn:
        cur = conn.cursor()
        query = f"SELECT * FROM visitor"  
        cur.execute(query) 
        visitor_data = cur.fetchall()  # Fetch all rows from the query
        conn.close()
        return visitor_data
    else:
        return []

def create_pdf(data):
    try:
        pdf_filename = "Total_visitor_history.pdf"  # Ensure the filename is consistent
        
        # Set up the PDF document
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter  # Default size for a letter page is 8.5 x 11 inches
        
        # Title and heading for the PDF
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, height - 50, "Visitor's Information")
        
        # Set font for the table content
        c.setFont("Helvetica", 10)

        # Column headers for the table
        headers = ["Id", "Name", "Total person", "Mob", "Date", "flat_id", "Remark"]
        header_y_position = height - 100
        c.drawString(50, header_y_position, headers[0])
        c.drawString(70, header_y_position, headers[1])
        c.drawString(180, header_y_position, headers[2])
        c.drawString(270, header_y_position, headers[3])
        c.drawString(360, header_y_position, headers[4])
        c.drawString(440, header_y_position, headers[5])
        c.drawString(490, header_y_position, headers[6])
        
        # Draw a line under the headers
        c.line(50, header_y_position - 5, width - 50, header_y_position - 5)
        
        # Add the visitor data in the table format
        y_position = header_y_position - 20
        for row in data:
            # Check if the current y_position is too close to the bottom of the page
            if y_position < 100:
                c.showPage()  # Create a new page
                c.setFont("Helvetica", 10)  # Reset font size for the new page
                # Re-draw headers
                c.drawString(50, height - 50, headers[0])
                c.drawString(70, height - 50, headers[1])
                c.drawString(180, height - 50, headers[2])
                c.drawString(270, height - 50, headers[3])
                c.drawString(360, height - 50, headers[4])
                c.drawString(440, height - 50, headers[5])
                c.drawString(490, height - 50, headers[6])
                c.line(50, height - 55, width - 50, height - 55)
                y_position = height - 70  # Reset position for next row
            
            # Insert the data into the PDF
            c.drawString(50, y_position, str(row[0]))  # Visitor ID
            c.drawString(70, y_position, str(row[1]))  # Name
            c.drawString(180, y_position, str(row[2]))  # Total Persons
            c.drawString(270, y_position, str(row[4]))  # Mobile Number
            c.drawString(360, y_position, str(row[3]))  # Time
            c.drawString(440, y_position, str(row[7]))  # Flat ID
            c.drawString(490, y_position, str(row[6]))  # Remark
            
            # Update y_position for next row
            y_position -= 20

        # Save the PDF file
        c.save()
        os.startfile(pdf_filename)
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Please close the file if it's already open in your system.")

def main():
    # Fetch data from the database
    guard_info = fetch_Guard_data()
    
    # If data exists, create the PDF
    if guard_info:
        create_pdf(guard_info)
    else:
        print("No visitor data found.")

if __name__ == "__main__":
    main()
