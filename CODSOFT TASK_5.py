import tkinter as tk
from tkinter import messagebox

# Contact book dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Function to display all contacts
def display_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            contact_list.insert(tk.END, f"{name}: {details['phone']}")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0]
        if name in contacts:
            contacts[name] = {"phone": phone_entry.get(), "email": email_entry.get(), "address": address_entry.get()}
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_entries()
            display_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0]
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            display_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Contact Book")

# Labels and entry fields
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, columnspan=2)

# Search field and button
tk.Label(root, text="Search").grid(row=7, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=8, column=0, columnspan=2)

# Listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.grid(row=9, column=0, columnspan=2)

# Display initial contacts
display_contacts()

# Running the GUI
root.mainloop()
