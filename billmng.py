from tkinter import Tk, Label, Entry, Button, LabelFrame, Frame, IntVar, Text, Scrollbar, END, StringVar
import tkinter.ttk as ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys


def main():
    win = Tk()
    app = Loginpage(win)
    win.mainloop()


class Loginpage:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750")
        self.win.title("Hostel Management System")

        self.title_label = Label(self.win, text='Hostel Management System', font='Arial 35 bold', bg='lightgray', bd=8,relief='groove')
        self.title_label.pack(side='top', fill='x')

        ############resizable##########
        self.win.resizable(0, 0)

        #######variables#########
        self.bill_no = random.randint(100, 9999)
        self.bill_no_tk = IntVar()
        self.bill_no_tk.set(self.bill_no)

        self.calc_var = StringVar()
        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())

        total_list=[]
        self.grd_total=0

        #############entry#############

        self.entry_frame = LabelFrame(self.win, text='Enter Detail', bg='Lightgray', font=('Arial', 20), bd=7,relief='groove')
        self.entry_frame.place(x=20, y=95, width=500, height=650)

        self.bill_no_lbl = Label(self.entry_frame, text="Bill Number", font=('Arial', 15), bg='lightgray')
        self.bill_no_lbl.grid(row=0, column=0, padx=2, pady=2)

        self.bill_no_ent = Entry(self.entry_frame, bd=5, font=('Arial', 15), textvariable=self.bill_no_tk)
        self.bill_no_ent.grid(row=0, column=1, padx=2, pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame, text="Customer Name", font=('Arial', 15), bg='lightgray')
        self.cust_nm_lbl.grid(row=1, column=0, padx=2, pady=2)

        self.cust_nm_ent = Entry(self.entry_frame, bd=5, textvariable=cust_nm, font=('Arial', 15))
        self.cust_nm_ent.grid(row=1, column=1, padx=2, pady=2)

        self.cust_cot_lbl = Label(self.entry_frame, text="Customer Contact Number", font=('Arial', 15),bg='lightgray')
        self.cust_cot_lbl.grid(row=2, column=0, padx=2, pady=2)

        self.cust_cot_ent = Entry(self.entry_frame, bd=5, textvariable=cust_cot, font=('Arial', 15))
        self.cust_cot_ent.grid(row=2, column=1, padx=2, pady=2)

        self.date_lbl = Label(self.entry_frame, text="Date", font=('Arial', 15), bg='lightgray')
        self.date_lbl.grid(row=3, column=0, padx=2, pady=2)

        self.date_ent = Entry(self.entry_frame, bd=5, textvariable=date_pr, font=('Arial', 15))
        self.date_ent.grid(row=3, column=1, padx=2, pady=2)
        self.date_ent.config(state="disabled")

        self.Item_pur_lbl = Label(self.entry_frame, text="Item Name", font=('Arial', 15), bg='lightgray')
        self.Item_pur_lbl.grid(row=4, column=0, padx=2, pady=2)

        self.Item_pur_ent = Entry(self.entry_frame, bd=5, textvariable=item_pur, font=('Arial', 15))
        self.Item_pur_ent.grid(row=4, column=1, padx=2, pady=2)

        self.Item_qty_lbl = Label(self.entry_frame, text="Item Quantity", font=('Arial', 15), bg='lightgray')
        self.Item_qty_lbl.grid(row=5, column=0, padx=2, pady=2)

        self.Item_qty_ent = Entry(self.entry_frame, bd=5, textvariable=item_qty, font=('Arial', 15))
        self.Item_qty_ent.grid(row=5, column=1, padx=2, pady=2)

        self.cost_one_lbl = Label(self.entry_frame, text="Cost Per Item", font=('Arial', 15), bg='lightgray')
        self.cost_one_lbl.grid(row=6, column=0, padx=2, pady=2)

        self.cost_one_ent = Entry(self.entry_frame, bd=5, textvariable=cone, font=('Arial', 15))
        self.cost_one_ent.grid(row=6, column=1, padx=2, pady=2)

        ###########function#########
        def default_bill():
            self.bill_txt.insert(END, "\t\t\t\tsample txt\n")
            self.bill_txt.insert(END, "\t\t\tsample txt\n")
            self.bill_txt.insert(END, "\t\t\tcontact-374783\n")
            self.bill_txt.insert(END, "============================================================================\n")
            self.bill_txt.insert(END, f"bill number:{self.bill_no_tk.get()}\n")

        def genbill():
            if cust_cot.get()== "" or (cust_cot.get()=="" or len(cust_cot.get())!=10):
                messagebox.showerror("Error!","pealse enter all the fielda correctly.",parent=self.win)
            else:    
                self.bill_txt.insert(END, f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END, f"\nCustomer Contact : {cust_cot.get()}")
                self.bill_txt.insert(END, f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END, "\n============================================================================\n")
                self.bill_txt.insert(END,"   product Name\t\t         Quantity\t\t         Per Cost\t\t         Total")
                self.bill_txt.insert(END, "\n============================================================================\n")

            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            

        def total_func():
            for item in total_list:
                self.grd_total=self.grd_total + item
            self.bill_txt.insert(END, "\n============================================================================\n")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\tGrand Total : {self.grd_total}\n")
            self.bill_txt.insert(END, "\n============================================================================\n")
            self.save_btn.config(state="normal")

        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")


            
        def reset_func():
            total_list.clear()
            self.grd_total=0
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
            self.bill_txt.delete("1.0",END)
            default_bill()

        def add_func():
            if item_pur.get()=="" or item_qty.get()=="":
                messagebox.showerror("Error!","pealse enter all the fielda correctly.",parent=self.win)
            else:
                qty=int(item_qty.get())
                cones=int(cone.get())
                total=qty*cones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n   {item_pur.get()}\t\t             {item_qty.get()}\t\t               $ {cone.get()}\t\t             $ {total}")

        def save_func():
            user_choice=messagebox.askyesno("Conform?",f"do you want to save the bill{self.bill_no_tk.get()}",parent=self.win)
            if user_choice>0:
                self.bill_content=self.bill_txt.get("1.0",END)
                try:
                    con= open(f"{sys.path[0]}/bills/"+str(self.bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to{e}",parent=self.win)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success",f"Bill {self.bill_no_tk.get()} has been saved successfully!",parent=self.win)
            else:
                return


        def add_pur():
            pass

        ########botton#######

        self.botton_frame = LabelFrame(self.entry_frame, bd=5, text='option', bg='lightgray', font=('Arial', 15))
        self.botton_frame.place(x=20, y=280, width=455, height=300)

        self.add_btn = Button(self.botton_frame, text='Add', font=('Arial', 12), width=12, height=3,command=add_func)
        self.add_btn.grid(row=0, column=0, padx=4, pady=2)

        self.generate_btn = Button(self.botton_frame, text='Generate', font=('Arial', 12), width=12, height=3,command=genbill)
        self.generate_btn.grid(row=0, column=1, padx=4, pady=2)

        self.clear_btn = Button(self.botton_frame, text='Clear', font=('Arial', 12), width=12, height=3,command=clear_func)
        self.clear_btn.grid(row=0, column=2, padx=4, pady=2)

        self.total_btn = Button(self.botton_frame, text='Total', font=('Arial', 12), width=12, height=3,command=total_func)
        self.total_btn.grid(row=1, column=0, padx=4, pady=2)

        self.reset_btn = Button(self.botton_frame, text='Reset', font=('Arial', 12), width=12, height=3,command=reset_func)
        self.reset_btn.grid(row=1, column=1, padx=4, pady=2)

        self.save_btn = Button(self.botton_frame, text='Save', font=('Arial', 12), width=12, height=3,command=save_func)
        self.save_btn.grid(row=1, column=2, padx=4, pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        #######calculater########

        self.calc_frame = Frame(self.win, bd=3, bg="lightgray", relief='groove')
        self.calc_frame.place(x=585, y=110, width=660, height=295)

        self.num_ent = Entry(self.calc_frame, bd=15, bg="lightgray", textvariable=self.calc_var, font=('Arial', 15),width=54, justify='right')
        self.num_ent.grid(row=0, column=0, columnspan=11)

        def press_btn(event):
            text = event.widget.cget("text")
            if text.isdigit() or text in ['+', '-', '*', '/']:
                self.calc_var.set(self.calc_var.get() + text)
                self.num_ent.update()
            elif text == "=":
                try:
                    value = eval(self.calc_var.get())
                    self.calc_var.set(value)
                    self.num_ent.update()
                except Exception as e:
                    print('Error:', e)
            elif text == "C":
                self.calc_var.set('')
                self.num_ent.delete(0, 'end')
            elif text == ".":
                self.calc_var.set(self.calc_var.get() + text)
                self.num_ent.update()

        self.btn7 = Button(self.calc_frame, bg='lightgray', text="7", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn7.grid(row=1, column=0, padx=2, pady=2)
        self.btn7.bind("<Button-1>", press_btn)

        self.btn8 = Button(self.calc_frame, bg='lightgray', text="8", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn8.grid(row=1, column=1, padx=2, pady=2)
        self.btn8.bind("<Button-1>", press_btn)

        self.btn9 = Button(self.calc_frame, bg='lightgray', text="9", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn9.grid(row=1, column=2, padx=2, pady=2)
        self.btn9.bind("<Button-1>", press_btn)

        self.btnadd = Button(self.calc_frame, bg='lightgray', text="+", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnadd.grid(row=1, column=3, padx=2, pady=2)
        self.btnadd.bind("<Button-1>", press_btn)

        self.btn4 = Button(self.calc_frame, bg='lightgray', text="4", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn4.grid(row=2, column=0, padx=2, pady=2)
        self.btn4.bind("<Button-1>", press_btn)

        self.btn5 = Button(self.calc_frame, bg='lightgray', text="5", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn5.grid(row=2, column=1, padx=2, pady=2)
        self.btn5.bind("<Button-1>", press_btn)

        self.btn6 = Button(self.calc_frame, bg='lightgray', text="6", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn6.grid(row=2, column=2, padx=2, pady=2)
        self.btn6.bind("<Button-1>", press_btn)

        self.btnsubs = Button(self.calc_frame, bg='lightgray', text="-", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnsubs.grid(row=2, column=3, padx=2, pady=2)
        self.btnsubs.bind("<Button-1>", press_btn)

        self.btn1 = Button(self.calc_frame, bg='lightgray', text="1", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn1.grid(row=3, column=0, padx=2, pady=2)
        self.btn1.bind("<Button-1>", press_btn)

        self.btn2 = Button(self.calc_frame, bg='lightgray', text="2", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn2.grid(row=3, column=1, padx=2, pady=2)
        self.btn2.bind("<Button-1>", press_btn)

        self.btn3 = Button(self.calc_frame, bg='lightgray', text="3", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn3.grid(row=3, column=2, padx=2, pady=2)
        self.btn3.bind("<Button-1>", press_btn)

        self.btnmult = Button(self.calc_frame, bg='lightgray', text="*", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnmult.grid(row=3, column=3, padx=2, pady=2)
        self.btnmult.bind("<Button-1>", press_btn)

        self.btn0 = Button(self.calc_frame, bg='lightgray', text="0", bd=8, width=12, height=1, font=('Arial', 15))
        self.btn0.grid(row=4, column=0, padx=2, pady=2)
        self.btn0.bind("<Button-1>", press_btn)

        self.btnpoint = Button(self.calc_frame, bg='lightgray', text=".", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnpoint.grid(row=4, column=1, padx=2, pady=2)
        self.btnpoint.bind("<Button-1>", press_btn)

        self.btnclear = Button(self.calc_frame, bg='lightgray', text="=", bd=8, width=12, height=1, font=('Arial', 15))
        self.btnclear.grid(row=4, column=2, padx=2, pady=2)
        self.btnclear.bind("<Button-1>", press_btn)

        self.btndivide = Button(self.calc_frame, bg='lightgray', text="/", bd=8, width=12, height=1, font=('Arial', 15))
        self.btndivide.grid(row=4, column=3, padx=2, pady=2)
        self.btndivide.bind("<Button-1>", press_btn)

        ############bill##############

        self.bill_frame = LabelFrame(self.win, text="Bill Area", font=('Arial', 18), bg='lightgray', bd=8, relief="groove")
        self.bill_frame.place(x=585, y=420, width=650, height=320)

        self.y_scroll = Scrollbar(self.bill_frame, orient="vertical")
        self.bill_txt = Text(self.bill_frame, bg="white", yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side='right', fill='y')
        self.bill_txt.pack(fill='both', expand=True)

        default_bill()


if __name__ == "__main__":
    main()