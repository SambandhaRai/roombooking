from tkinter import *
from tkinter import ttk
import random

from tkinter import messagebox


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1295x550")

                #title
        lbl_title=Label(self.root,text="Room Booking",font=("Times New Roman",40,"bold"),bg="sky blue")
        lbl_title.place(x=0,y=0,width=1295,height=50)


          #labelFrame
        labelframelleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',font=("Times New Roman",16,"bold"))
        labelframelleft.place(x=5,y=50,width=425,height=490)

        #vairables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_numberroom=StringVar()



        #fetch
        def fetch_contact(self):
            if self.var_contact.get()=="":
                messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)



        #customer contact
        lbl_customer_cont=Label(labelframelleft,text="Customer Contact",font=("Times New Roman",16,"bold"),padx=2,pady=6)
        lbl_customer_cont.grid(row=0,column=0,sticky=W)

        entry_cont=ttk.Entry(labelframelleft,textvariable=self.var_contact,width=20,font=("Times New Roman",16,"bold"))
        entry_cont.grid(row=0,column=1,sticky=W)


        #Fetch data button
        btn_Fetch_data=Button(labelframelleft,text="Fetch Data",font=("Times New Roman",16,"bold"),width=10,command=fetch_contact)
        btn_Fetch_data.place(x=320,y=5)


        #check in date
        lbl_checkin_date=Label(labelframelleft,text="Check-In-Date",font=("Times New Roman",16,"bold"))
        lbl_checkin_date.grid(row=1,column=0,sticky=W)

        entry_checkin=ttk.Entry(labelframelleft,textvariable=self.var_checkin,width=25,font=("Times New Roman",16,"bold"))
        entry_checkin.grid(row=1,column=1,sticky=W)
        

        #check out date
        lbl_checkout_date=Label(labelframelleft,text="Check-Out-Date",font=("Times New Roman",16,"bold"))
        lbl_checkout_date.grid(row=2,column=0,sticky=W)

        entry_checkout=ttk.Entry(labelframelleft,textvariable=self.var_checkout,width=25,font=("Times New Roman",16,"bold"))
        entry_checkout.grid(row=2,column=1,sticky=W)
        

        #room number
        lbl_room_no=Label(labelframelleft,text="Room Number",font=("Times New Roman",16,"bold"))
        lbl_room_no.grid(row=3,column=0,sticky=W)

        entry_room_no=ttk.Entry(labelframelleft,textvariable=self.var_numberroom,width=25,font=("Times New Roman",16,"bold"))
        entry_room_no.grid(row=3,column=1,sticky=W)


        
        









        #table frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("Times New Roman",16,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)


        #SCROLL
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)



        self.Room_Detail_table = ttk.Treeview(table_frame,column=("Room Number", 
                                "Vacancy", "Price Per Month", "Cleanliness"),xscrollcommand=scroll_x.set,
                                yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Detail_table.xview)
        scroll_y.config(command=self.Room_Detail_table.yview)


        self.Room_Detail_table.heading("Room Number","Ro")


















if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
