import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3

# Initialize the database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT,
    address TEXT
)
''')
conn.commit()

# Function to add a new contact
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()
    
    if name and phone and email and address:
        c.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)', 
                  (name, phone, email, address))
        conn.commit()
        messagebox.showinfo("Success", "Contact added successfully!", parent=root)
        view_contacts()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "All fields are required!", parent=root)

# Function to view all contacts
def view_contacts():
    for i in tree.get_children():
        tree.delete(i)

    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()
    for contact in contacts:
        tree.insert("", "end", values=(contact[0], contact[1], contact[2], contact[3], contact[4]))

# Function to search for a contact
def search_contact():
    search_term = search_var.get()
    for i in tree.get_children():
        tree.delete(i)
    c.execute('SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?', 
              ('%' + search_term + '%', '%' + search_term + '%'))
    results = c.fetchall()
    if results:
        for result in results:
            tree.insert("", "end", values=(result[0], result[1], result[2], result[3], result[4]))
    else:
        messagebox.showinfo("Search Results", "No contacts found.", parent=root)

# Function to update a contact
def update_contact():
    contact_id = simpledialog.askinteger("Input", "Enter Contact ID to Update:", parent=root)
    if contact_id:
        c.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        contact = c.fetchone()
        if contact:
            name_var.set(contact[1])
            phone_var.set(contact[2])
            email_var.set(contact[3])
            address_var.set(contact[4])
            
            def save_update():
                name = name_var.get()
                phone = phone_var.get()
                email = email_var.get()
                address = address_var.get()
                
                if name and phone and email and address:
                    c.execute('''
                    UPDATE contacts 
                    SET name = ?, phone = ?, email = ?, address = ? 
                    WHERE id = ?
                    ''', (name, phone, email, address, contact_id))
                    conn.commit()
                    messagebox.showinfo("Success", "Contact updated successfully!", parent=root)
                    view_contacts()
                    clear_fields()
                    update_win.destroy()
                else:
                    messagebox.showwarning("Warning", "All fields are required!", parent=root)
            
            update_win = tk.Toplevel(root)
            update_win.title("Update Contact")
            
            tk.Label(update_win, text="Name:").pack(padx=10, pady=5)
            tk.Entry(update_win, textvariable=name_var).pack(padx=10, pady=5)
            
            tk.Label(update_win, text="Phone:").pack(padx=10, pady=5)
            tk.Entry(update_win, textvariable=phone_var).pack(padx=10, pady=5)
            
            tk.Label(update_win, text="Email:").pack(padx=10, pady=5)
            tk.Entry(update_win, textvariable=email_var).pack(padx=10, pady=5)
            
            tk.Label(update_win, text="Address:").pack(padx=10, pady=5)
            tk.Entry(update_win, textvariable=address_var).pack(padx=10, pady=5)
            
            tk.Button(update_win, text="Save", command=save_update).pack(pady=10)
            
        else:
            messagebox.showwarning("Warning", "Contact not found!", parent=root)

# Function to delete a contact
def delete_contact():
    contact_id = simpledialog.askinteger("Input", "Enter Contact ID to Delete:", parent=root)
    if contact_id:
        c.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        conn.commit()
        messagebox.showinfo("Success", "Contact deleted successfully!", parent=root)
        view_contacts()

# Function to clear input fields
def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

# Setup the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("800x600")
root.configure(bg="#e0e0e0")

# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# Create frames
left_frame = tk.Frame(root, bg="#e0e0e0")
left_frame.pack(side="left", fill="y", padx=10, pady=10)

right_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief="sunken")
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Add search field
tk.Label(left_frame, text="Search:", bg="#e0e0e0").pack(padx=5, pady=5)
tk.Entry(left_frame, textvariable=search_var).pack(padx=5, pady=5)
tk.Button(left_frame, text="Search", command=search_contact, bg="#FFC107", fg="white").pack(padx=5, pady=5)

# Add input fields
tk.Label(left_frame, text="Name:", bg="#e0e0e0").pack(padx=5, pady=5)
tk.Entry(left_frame, textvariable=name_var).pack(padx=5, pady=5)

tk.Label(left_frame, text="Phone:", bg="#e0e0e0").pack(padx=5, pady=5)
tk.Entry(left_frame, textvariable=phone_var).pack(padx=5, pady=5)

tk.Label(left_frame, text="Email:", bg="#e0e0e0").pack(padx=5, pady=5)
tk.Entry(left_frame, textvariable=email_var).pack(padx=5, pady=5)

tk.Label(left_frame, text="Address:", bg="#e0e0e0").pack(padx=5, pady=5)
tk.Entry(left_frame, textvariable=address_var).pack(padx=5, pady=5)

# Add buttons in a 2x2 grid
buttons_frame = tk.Frame(left_frame, bg="#e0e0e0")
buttons_frame.pack(padx=5, pady=5)
tk.Button(buttons_frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="View Contacts", command=view_contacts, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5, pady=5)
tk.Button(buttons_frame, text="Update Contact", command=update_contact, bg="#FF5722", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Delete Contact", command=delete_contact, bg="#F44336", fg="white").grid(row=1, column=1, padx=5, pady=5)

# Add Treeview for displaying contacts with adjusted size
columns = ("ID", "Name", "Phone", "Email", "Address")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Address", text="Address")
tree.column("ID", width=30)
tree.column("Name", width=100)
tree.column("Phone", width=100)
tree.column("Email", width=150)
tree.column("Address", width=150)
tree.pack(fill="both", expand=True)

# Initial view of contacts
view_contacts()

# Run the application
root.mainloop()

# Close the database connection when the application is closed
conn.close()