from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import sqlite3
from tkinter import messagebox


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1295x550")


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
            room_no = entry_rm.get()
            name = entry_cname.get()
            contact_no = entry_cont.get()
            address = entry_address.get()
            phone_no = entry_pphone.get()
            gender = entry_gender.get()
            parents_name = entry_parent_name.get()
            
            if room_no and name:
                cursor.execute("INSERT INTO students (room_no, name, contact_no, address, phone_no, gender, parents_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (room_no, name, contact_no, address, phone_no, gender, parents_name))
                connection.commit()
                view_students()
                clear_entries()


        def search_students():
            search_value = entry_rm.get()
            for row in self.Room_Detail_table.get_children():
                self.Room_Detail_table.delete(row)
            cursor.execute("SELECT * FROM students WHERE id=? OR room_no=? OR name LIKE ?", (search_value, search_value, '%' + search_value + '%'))
            rows = cursor.fetchall()
            for row in rows:
                self.Room_Detail_table.insert('', 'end', values=row)
            clear_entries()



        def view_students():
            for row in self.Room_Detail_table.get_children():
                self.Room_Detail_table.delete(row)
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            for row in rows:
                self.Room_Detail_table.insert('', 'end', values=row)


        
        def on_select(event):
            item = self.Room_Detail_table.selection()
            if item:
                edit_btn.grid(row=9, columnspan=2, pady=10)  # Grid edit button
                del_btn.grid(row=10, columnspan=2, pady=10)   # Grid delete button
                add_btn.grid_forget()  # Forget add button when item is selected
                
                selected_item = self.Room_Detail_table.item(item, 'values')
                entry_rm.set(selected_item[1])
                entry_cname.delete(0, tk.END)
                entry_cont.delete(0, tk.END)
                entry_address.delete(0, tk.END)
                entry_pphone.delete(0, tk.END)
                entry_parent_name.delete(0, tk.END)
                entry_cname.insert(tk.END, selected_item[2])
                entry_cont.insert(tk.END, selected_item[3])
                entry_address.insert(tk.END, selected_item[4])
                entry_pphone.insert(tk.END, selected_item[5])
                entry_gender.set(selected_item[6])
                entry_parent_name.insert(tk.END, selected_item[7])
            else:
                add_btn.grid(row=9, columnspan=2, pady=10)  # Grid add button if no item is selected
                edit_btn.grid_forget()  # Forget edit button
                del_btn.grid_forget()   # Forget delete button
                clear_entries()


        def edit_student():
            item = self.Room_Detail_table.selection()[0]
            selected_id = self.Room_Detail_table.item(item, 'values')[0]
            room_no = entry_rm.get()
            contact_no = entry_cont.get()
            name = entry_cname.get()
            address = entry_address.get()
            phone_no = entry_pphone.get()
            gender = entry_gender.get()
            parents_name = entry_parent_name.get()
            cursor.execute("UPDATE students SET room_no=?, name=?, contact_no=?, address=?, phone_no=?, gender=?, parents_name=? WHERE id=?",
                        (room_no, name, contact_no, address, phone_no, gender, parents_name, selected_id))
            connection.commit()
            view_students()
            clear_entries()


        def delete_student():
            item = self.Room_Detail_table.selection()[0]
            selected_id = self.Room_Detail_table.item(item, 'values')[0]
            cursor.execute("DELETE FROM students WHERE id=?", (selected_id,))
            connection.commit()
            view_students()
            clear_entries()

        def clear_entries():
            entry_rm.set('')
            entry_cname.delete(0, tk.END)
            entry_cont.delete(0, tk.END)
            entry_address.delete(0, tk.END)
            entry_pphone.delete(0, tk.END)
            entry_parent_name.delete(0,tk.END)
            entry_gender.set('')




        #title
        lbl_title=Label(self.root,text="Room Booking",font=("Times New Roman",40,"bold"),bg="sky blue")
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #labelFrame
        labelframelleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',font=("Times New Roman",16,"bold"))
        labelframelleft.place(x=5,y=50,width=425,height=490)

        #vairables
        self.var_numberroom=StringVar()
        self.var_custid=StringVar()
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_parentname=StringVar()
        self.var_pphone=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        




        #ROom Number
        lbl_room_no=Label(labelframelleft,text="Room No",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=0,column=0,sticky=W)

        entry_rm=ttk.Entry(labelframelleft,textvariable=self.var_numberroom,width=15,font=("Times New Roman",16,"bold"))
        entry_rm.grid(row=0,column=1,sticky=W)


        #customer ID
        lbl_customer_id=Label(labelframelleft,text="Customer ID",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_customer_id.grid(row=1,column=0,sticky=W)

        entry_cid=ttk.Entry(labelframelleft,textvariable=self.var_custid,width=25,font=("Times New Roman",16,"bold"))
        entry_cid.grid(row=1,column=1,sticky=W)


        #customer name
        lbl_customer_name=Label(labelframelleft,text="Name",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_customer_name.grid(row=2,column=0,sticky=W)

        entry_cname=ttk.Entry(labelframelleft,textvariable=self.var_cname,width=25,font=("Times New Roman",16,"bold"))
        entry_cname.grid(row=2,column=1,sticky=W)


        #customer contact
        lbl_customer_cont=Label(labelframelleft,text="Customer Contact",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_customer_cont.grid(row=3,column=0,sticky=W)

        entry_cont=ttk.Entry(labelframelleft,textvariable=self.var_contact,width=25,font=("Times New Roman",16,"bold"))
        entry_cont.grid(row=3,column=1,sticky=W)


        #Fetch data button
        btn_Fetch_data=Button(labelframelleft,text="Fetch Data",font=("Times New Roman",16,"bold"),width=10,command=search_students)
        btn_Fetch_data.place(x=290,y=5)


        #email
        lbl_email=Label(labelframelleft,text="Email",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_email.grid(row=4,column=0,sticky=W)

        entry_cont=ttk.Entry(labelframelleft,textvariable=self.var_email,width=25,font=("Times New Roman",16,"bold"))
        entry_cont.grid(row=4,column=1,sticky=W)


        #Address
        lbl_address=Label(labelframelleft,text="Address",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_address.grid(row=5,column=0,sticky=W)

        entry_address=ttk.Entry(labelframelleft,textvariable=self.var_address,width=25,font=("Times New Roman",16,"bold"))
        entry_address.grid(row=5,column=1,sticky=W)


        #Gender
        lbl_gender=Label(labelframelleft,text="Gender",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=6,column=0,sticky=W)

        entry_gender=ttk.Entry(labelframelleft,textvariable=self.var_gender,width=25,font=("Times New Roman",16,"bold"))
        entry_gender.grid(row=6,column=1,sticky=W)


        #Parent Name
        lbl_parent_name=Label(labelframelleft,text="Parent's Name",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_parent_name.grid(row=7,column=0,sticky=W)

        entry_parent_name=ttk.Entry(labelframelleft,textvariable=self.var_parentname,width=25,font=("Times New Roman",16,"bold"))
        entry_parent_name.grid(row=7,column=1,sticky=W)


        #parent phone
        lbl_parent_phone=Label(labelframelleft,text="Parent's Phone No.",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_parent_phone.grid(row=8,column=0,sticky=W)

        entry_pphone=ttk.Entry(labelframelleft,textvariable=self.var_pphone,width=25,font=("Times New Roman",16,"bold"))
        entry_pphone.grid(row=8,column=1,sticky=W)


        #check in date
        lbl_checkin_date=Label(labelframelleft,text="Check-In-Date",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_checkin_date.grid(row=9,column=0,sticky=W)

        entry_checkin=ttk.Entry(labelframelleft,textvariable=self.var_checkin,width=25,font=("Times New Roman",16,"bold"))
        entry_checkin.grid(row=9,column=1,sticky=W)
        

        #check out date
        lbl_checkout_date=Label(labelframelleft,text="Check-Out-Date",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_checkout_date.grid(row=10,column=0,sticky=W)

        entry_checkout=ttk.Entry(labelframelleft,textvariable=self.var_checkout,width=25,font=("Times New Roman",16,"bold"))
        entry_checkout.grid(row=10,column=1,sticky=W)
        

        #add button
        add_btn = Button(labelframelleft, text="Add Student", command=add_student, bg="lightgreen", fg="white", bd=5)
        add_btn.grid(row=11, column=0, pady=10)


        #Edit button
        edit_btn = Button(labelframelleft, text="Edit Student", command=edit_student, bg="lightgreen", fg="white", bd=5)
        #edit_btn.grid(row=7, columnspan=2, pady=10)


        #delete button
        del_btn = Button(labelframelleft, text="Delete Student", command=delete_student, bg="lightgreen", fg="white", bd=5)
        #del_btn.grid(row=8, columnspan=2, pady=10)
        

        

        
        









        #table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("Times New Roman",16,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)


        #SCROLL
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)



        self.Room_Detail_table = ttk.Treeview(table_frame,column=("ID", 
                                "Room No.", "Name", "Contact No.","Email","Address","Gender","Parent's Name","Phone No."),show="headings",xscrollcommand=scroll_x.set,
                                yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Detail_table.xview)
        scroll_y.config(command=self.Room_Detail_table.yview)


        self.Room_Detail_table.heading("ID",text="Customer ID")
        self.Room_Detail_table.heading("Room No.",text="Room No.")
        self.Room_Detail_table.heading("Name",text="Name")
        self.Room_Detail_table.heading("Contact No.",text="Contact No.")
        self.Room_Detail_table.heading("Email",text="Email")
        self.Room_Detail_table.heading("Address",text="Address")
        self.Room_Detail_table.heading("Gender",text="Gender")
        self.Room_Detail_table.heading("Parent's Name",text="Parent's Name")
        self.Room_Detail_table.heading("Phone No.",text="Phone No.")
        self.Room_Detail_table.pack(fill='both',expand=True)

        self.Room_Detail_table.bind('<<TreeviewSelect>>', on_select)



        connection, cursor = connect_db()

        view_students()


        close_db(connection)



















if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
