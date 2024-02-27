import tkinter as tk
from tkinter import ttk
import sqlite3

def connect_db():
    connection = sqlite3.connect('hostelers.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        room_no INTEGER,
                        name TEXT,
                        contact_no TEXT,
                        address TEXT,
                        phone_no TEXT,
                        gender TEXT,
                        parents_name TEXT)''')
    connection.commit()
    return connection, cursor

def close_db(connection):
    connection.close()

def add_student():
    room_no = roomno_combobox.get()
    name = name_ent.get()
    contact_no = contact_ent.get()
    address = address_ent.get()
    phone_no = phone_ent.get()
    gender = gender_combobox.get()
    parents_name = parents_ent.get()
    
    if room_no and name:
        cursor.execute("INSERT INTO students (room_no, name, contact_no, address, phone_no, gender, parents_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (room_no, name, contact_no, address, phone_no, gender, parents_name))
        connection.commit()
        view_students()
        clear_entries()

def view_students():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)

def search_students():
    search_value = search_entry.get()
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students WHERE id=? OR room_no=? OR name LIKE ?", (search_value, search_value, '%' + search_value + '%'))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', 'end', values=row)
    clear_entries()
    
def on_select(event):
    item = tree.selection()
    if item:
        edit_btn.grid(row=9, columnspan=2, pady=10)  # Grid edit button
        del_btn.grid(row=10, columnspan=2, pady=10)   # Grid delete button
        add_btn.grid_forget()  # Forget add button when item is selected
        
        selected_item = tree.item(item, 'values')
        roomno_combobox.set(selected_item[1])
        name_ent.delete(0, tk.END)
        contact_ent.delete(0, tk.END)
        address_ent.delete(0, tk.END)
        phone_ent.delete(0, tk.END)
        parents_ent.delete(0, tk.END)
        name_ent.insert(tk.END, selected_item[2])
        contact_ent.insert(tk.END, selected_item[3])
        address_ent.insert(tk.END, selected_item[4])
        phone_ent.insert(tk.END, selected_item[5])
        gender_combobox.set(selected_item[6])
        parents_ent.insert(tk.END, selected_item[7])
    else:
        add_btn.grid(row=9, columnspan=2, pady=10)  # Grid add button if no item is selected
        edit_btn.grid_forget()  # Forget edit button
        del_btn.grid_forget()   # Forget delete button
        clear_entries()

def clear_entries():
    roomno_combobox.set('')
    name_ent.delete(0, tk.END)
    contact_ent.delete(0, tk.END)
    address_ent.delete(0, tk.END)
    phone_ent.delete(0, tk.END)
    parents_ent.delete(0, tk.END)
    gender_combobox.set('')

def edit_student():
    item = tree.selection()[0]
    selected_id = tree.item(item, 'values')[0]
    room_no = roomno_combobox.get()
    name = name_ent.get()
    contact_no = contact_ent.get()
    address = address_ent.get()
    phone_no = phone_ent.get()
    gender = gender_combobox.get()
    parents_name = parents_ent.get()
    cursor.execute("UPDATE students SET room_no=?, name=?, contact_no=?, address=?, phone_no=?, gender=?, parents_name=? WHERE id=?",
                   (room_no, name, contact_no, address, phone_no, gender, parents_name, selected_id))
    connection.commit()
    view_students()
    clear_entries()

def delete_student():
    item = tree.selection()[0]
    selected_id = tree.item(item, 'values')[0]
    cursor.execute("DELETE FROM students WHERE id=?", (selected_id,))
    connection.commit()
    view_students()
    clear_entries()

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Hostel Management System")
win.configure(bg="lightblue")

title_label = tk.Label(win, text="Hostel Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE,
                       bg="lightblue", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

search_frame = tk.LabelFrame(win, text="Search", font=("Arial,20"), bd=12, relief=tk.GROOVE, bg="lightgrey")
search_frame.pack(side=tk.TOP, fill=tk.X)

placeholder_text = "Enter student ID or room no or student name"

search_entry = tk.Entry(search_frame, bd=7, font=("Arial", 10), fg='grey', width=60)
search_entry.insert(0, placeholder_text)
search_entry.bind('<FocusIn>', lambda event: search_entry.delete(0, tk.END) if search_entry.get() == placeholder_text else None)
search_entry.bind('<FocusOut>', lambda event: search_entry.insert(0, placeholder_text) if search_entry.get() == '' else None)
search_entry.grid(row=0, column=0, padx=10, pady=10)

search_btn = tk.Button(search_frame, text="Search", command=search_students, bg="lightgreen", fg="white", bd=5)
search_btn.grid(row=0, column=1, padx=10, pady=5)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

detail_frame = tk.LabelFrame(data_frame, text="Enter Details", font=("Arial,20"), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

roomno_lbl = tk.Label(detail_frame, text="Room No", font=("Arial", 15), bg="lightgrey")
roomno_lbl.grid(row=0, column=0, padx=2, pady=2)

roomno_combobox = ttk.Combobox(detail_frame, values=["101", "102","103"], state="readonly", font=("Arial", 15))
roomno_combobox.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)

name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
name_ent.grid(row=1, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact No", font=("Arial", 15), bg="lightgrey")
contact_lbl.grid(row=2, column=0, padx=2, pady=2)

contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
contact_ent.grid(row=2, column=1, padx=2, pady=2)

email_lbl = tk.Label(detail_frame, text="Email", font=("Arial", 15), bg="lightgrey")
email_lbl.grid(row=3, column=0, padx=2, pady=2)

email_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
email_ent.grid(row=3, column=1, padx=2, pady=2)

gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 15), bg="lightgrey")
gender_lbl.grid(row=4, column=0, padx=2, pady=2)

gender_combobox = ttk.Combobox(detail_frame, values=["Male", "Female","Others"], state="readonly", font=("Arial", 15))
gender_combobox.grid(row=4, column=1, padx=2, pady=2)

parents_lbl = tk.Label(detail_frame, text="Parent's Name", font=("Arial", 15), bg="lightgrey")
parents_lbl.grid(row=5, column=0, padx=2, pady=2)

parents_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
parents_ent.grid(row=5, column=1, padx=2, pady=2)

phone_lbl = tk.Label(detail_frame, text="Parent's Phone No", font=("Arial", 15), bg="lightgrey")
phone_lbl.grid(row=6, column=0, padx=2, pady=2)

phone_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
phone_ent.grid(row=6, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgrey")
address_lbl.grid(row=7, column=0, padx=2, pady=2)

address_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
address_ent.grid(row=7, column=1, padx=2, pady=2)

add_btn = tk.Button(detail_frame, text="Add Student", command=add_student, bg="lightgreen", fg="white", bd=5)
add_btn.grid(row=8, columnspan=2, pady=10)

edit_btn = tk.Button(detail_frame, text="Edit Student", command=edit_student, bg="lightgreen", fg="white", bd=5)
#edit_btn.grid(row=7, columnspan=2, pady=10)

del_btn = tk.Button(detail_frame, text="Delete Student", command=delete_student, bg="lightgreen", fg="white", bd=5)
#del_btn.grid(row=8, columnspan=2, pady=10)

tree = ttk.Treeview(data_frame, columns=('ID', 'Room No', 'Name', 'Contact No', 'Email', 'Phone No', 'Gender', "Parent's Name", 'Address'), show='headings')
tree.heading('ID', text='Customer ID')
tree.heading('Room No', text='Room No')
tree.heading('Name', text='Name')
tree.heading('Contact No', text='Contact No')
tree.heading('Email', text='Email')
tree.heading('Phone No', text='Phone No')
tree.heading('Gender', text='Gender')
tree.heading("Parent's Name", text="Parent's Name")
tree.heading('Address', text='Address')
tree.pack(fill='both', expand=True)

tree.bind('<<TreeviewSelect>>', on_select)

scroll_x=ttk.Scrollbar(data_frame,orient=tk.HORIZONTAL)
scroll_y=ttk.Scrollbar(data_frame,orient=tk.VERTICAL)

scroll_x.configure(command=tree.xview)
scroll_y.configure(command=tree.yview)

tree.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

connection, cursor = connect_db()

view_students()

win.mainloop()

close_db(connection)