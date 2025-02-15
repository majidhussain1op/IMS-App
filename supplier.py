from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
     self.root=root
     self.root.geometry("1100x520+220+140")
     self.root.title("Municipal Committee Sehwan Management System | Developed By Majid Meerani Sehwani")
     self.root.config(bg="#cdf",bd="10")
     self.root.focus_force()
    #==================
    #  All variables=========
     self.var_searchBy=StringVar()
     self.var_searchTxt=StringVar()


     self.var_sup_invoice=StringVar()
     self.var_name=StringVar()
     self.var_contact=StringVar()
     
    

    

     #=================search==========
    
     lbl_search=Label(self.root,text="Invoice No.",bg="white",font=("goudy old style", 15))
     lbl_search.place(x=700,y=80)

     txt_search=Entry(self.root,textvariable=self.var_searchTxt,font=("goudy old style",15), bg="light yellow").place(x=800,y=80,width=160)
     btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15), bg="#4caf50", fg="white",cursor="hand2").place(x=980,y=79,width=100,height=28)
    #============title===========
     title=Label(self.root,text="Supplier Details", font=("goudy old style", 20,"bold"), bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)
    
    #==========Content=========
     #====Row2======
     lbl_supplier_invoice=Label(self.root,text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50,y=80)
     txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="light yellow").place(x=180,y=80,width=180)
    
     #====Row2======
     lbl_name=Label(self.root,text="Name", font=("goudy old style", 15), bg="white").place(x=50,y=120)
     txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="light yellow").place(x=180,y=120,width=180)
    
    #====Row3======
     lbl_contact=Label(self.root,text="Contact", font=("goudy old style", 15), bg="white").place(x=50,y=160)
     txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="light yellow").place(x=180,y=170,width=200)
    
     #====Row4======
     lbl_desc=Label(self.root,text="Description", font=("goudy old style", 15), bg="white").place(x=50,y=200)
     self.txt_desc=Text(self.root,font=("goudy old style", 15), bg="light yellow")
     self.txt_desc.place(x=180,y=200,width=470,height=120)
     
    #========Buttons==========
     btn_search=Button(self.root,text="Save",command=self.add,font=("goudy old style",15), bg="#2196c3", fg="white",cursor="hand2").place(x=180,y=425,width=110,height="35")
     btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy old style",15), bg="#4caf55", fg="white",cursor="hand2").place(x=300,y=425,width=110,height="35")
     btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15), bg="#f44339", fg="white",cursor="hand2").place(x=420,y=425,width=110,height="35")
     btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15), bg="#607d9f", fg="white",cursor="hand2").place(x=540,y=425,width=110,height="35")
    
    #===========Employee Details==========
     emp_frame=Frame(self.root,bd=3,relief=RIDGE)
     emp_frame.place(x=700,y=120,width=380,height=350)

     scrolly=Scrollbar(emp_frame,orient=VERTICAL)
     scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

     self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice", "name", "contact", "desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
     scrollx.pack(side=BOTTOM,fill=X)
     scrolly.pack(side=RIGHT,fill=Y)
     scrollx.config(command=self.SupplierTable.xview)
     scrolly.config(command=self.SupplierTable.yview)

     self.SupplierTable.heading("invoice", text="Invoice")
     self.SupplierTable.heading("name", text="Name")
     self.SupplierTable.heading("contact", text="Contact")
     self.SupplierTable.heading("desc", text="Description")
     self.SupplierTable["show"]="headings"

     self.SupplierTable.column("invoice",width=90)
     self.SupplierTable.column("name", width=110)
     self.SupplierTable.column("contact", width=100)
     self.SupplierTable.column("desc", width=100)
     self.SupplierTable.pack(fill=BOTH,expand=1)
     self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

     self.show()
    #=============================================
     
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error", "Invoice must be required",parent=self.root)
            else:
               cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row!=None:
                  messagebox.showerror("Error", "Invoice no. already assigned, try different ", parent=self.root)
               else:
                    cur.execute("Insert into supplier (invoice, name, contact, desc) values(?,?,?,?)",(
                                            self.var_sup_invoice.get(),
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            self.txt_desc.get("1.0", END),
                                           
                  ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
       
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           cur.execute("Select * from supplier")
           rows=cur.fetchall()
           self.SupplierTable.delete(*self.SupplierTable.get_children())
           for row in rows:
              self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
       f=self.SupplierTable.focus()
       content=(self.SupplierTable.item(f))
       row=content["values"]
      #  print(row)

       self.var_sup_invoice.set(row[0]),
       self.var_name.set(row[1]),
       self.var_contact.set(row[2]),
       self.txt_desc.delete("1.0",END),
       self.txt_desc.insert(END,row[3]),
       


    def Update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error", "Invoice no. must be required",parent=self.root)
            else:
               cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row==None:
                  messagebox.showerror("Error", "Invalid Invoice no.", parent=self.root)
               else:
                    cur.execute("Update supplier set name=?, contact=?, desc=? where invoice=? ",(
                                            self.var_name.get(),
                                            self.var_contact.get(),
                                            self.txt_desc.get("1.0", END),
                                            self.var_sup_invoice.get(),
                  ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()

        try:
            if self.var_sup_invoice.get()=="":
               messagebox.showerror("Error", "Invoice no. must be required",parent=self.root)
            else:
               cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
               row=cur.fetchone()
               if row==None:
                  messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
               else:
                  op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                  if op==True:
                     cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "Supplier Deleted successfully",parent=self.root)
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
           
    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete("1.0",END),
        self.var_searchTxt.set(""),
        self.show()

    def search(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
          if self.var_searchTxt.get()=="":
              messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
          else:
              cur.execute("Select * from supplier where invoice=?",(self.var_searchTxt.get(),))
              row=cur.fetchone()
              if row!=None:
               self.SupplierTable.delete(*self.SupplierTable.get_children())
               self.SupplierTable.insert('',END,values=row)
              else:
                 messagebox.showerror("Error", "No record found!!!", parent=self.root)    
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

       

if __name__=="__main__":
   root=Tk()
   obj=supplierClass(root)
   root.mainloop()