from tkinter import*
from PIL import Image, ImageTk # type: ignore
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
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


     self.var_emp_id=StringVar()
     self.var_gender=StringVar()
     self.var_Designation=StringVar()
     self.var_contact=StringVar()
     self.var_name=StringVar()
     self.var_dob=StringVar()
     self.var_doj=StringVar()
     
     self.var_email=StringVar()
     self.var_password=StringVar()
     self.var_uType=StringVar()
     self.var_salary=StringVar()

    

     #=================search==========
     SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
     SearchFrame.place(x=250,y=20,width=600,height=70)

     cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchBy,values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("goudy old style", 15))
     cmb_search.place(x=10,y=10,width=180)
     cmb_search.current(0)

     txt_search=Entry(SearchFrame,textvariable=self.var_searchTxt,font=("goudy old style",15), bg="light yellow").place(x=200,y=10)
     btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15), bg="#4caf50", fg="white",cursor="hand2").place(x=410,y=9,width=150,height="30")
    #============title===========
     title=Label(self.root,text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
    #==========Content=========
     #====Row2======
     lbl_empId=Label(self.root,text="Emp ID", font=("goudy old style", 15), bg="white").place(x=50,y=150)
     lbl_gender=Label(self.root,text="Gender", font=("goudy old style", 15), bg="white").place(x=350,y=150)
     lbl_contact=Label(self.root,text="Contact", font=("goudy old style", 15), bg="white").place(x=750,y=150)

     txt_empId=Entry(self.root,textvariable=self.var_emp_id, font=("goudy old style", 15), bg="light yellow").place(x=150,y=150,width=180)
     cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select", "Male", "Female", "Other"), state='readonly', justify=CENTER, font=("goudy old style", 15))
     cmb_gender.place(x=500,y=150,width=180)
     cmb_gender.current(0)
     txt_contact=Entry(self.root,textvariable=self.var_contact, font=("goudy old style", 15), bg="light yellow").place(x=850,y=150,width=180)

     #====Row2======
     lbl_name=Label(self.root,text="Name", font=("goudy old style", 15), bg="white").place(x=50,y=190)
     lbl_dob=Label(self.root,text="D.O.B", font=("goudy old style", 15), bg="white").place(x=350,y=190)
     lbl_doj=Label(self.root,text="D.O.J", font=("goudy old style", 15), bg="white").place(x=750,y=190)

     txt_name=Entry(self.root,textvariable=self.var_name, font=("goudy old style", 15), bg="light yellow").place(x=150,y=190,width=180)
     txt_dob=Entry(self.root,textvariable=self.var_dob, font=("goudy old style", 15), bg="light yellow").place(x=500,y=190,width=180)
     txt_doj=Entry(self.root,textvariable=self.var_doj, font=("goudy old style", 15), bg="light yellow").place(x=850,y=190,width=180)

    #====Row3======
     lbl_email=Label(self.root,text="Email", font=("goudy old style", 15), bg="white").place(x=50,y=230)
     lbl_password=Label(self.root,text="Password", font=("goudy old style", 15), bg="white").place(x=350,y=230)
     lbl_userType=Label(self.root,text="User Type", font=("goudy old style", 15), bg="white").place(x=750,y=230)

     txt_email=Entry(self.root,textvariable=self.var_email, font=("goudy old style", 15), bg="light yellow").place(x=150,y=230,width=180)
     txt_pass=Entry(self.root,textvariable=self.var_password, font=("goudy old style", 15), bg="light yellow").place(x=500,y=230,width=180)
     cmb_uType=ttk.Combobox(self.root,textvariable=self.var_uType,values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("goudy old style", 15))
     cmb_uType.place(x=850,y=230,width=180)
     cmb_uType.current(0)

     #====Row4======
     lbl_address=Label(self.root,text="Address", font=("goudy old style", 15), bg="white").place(x=50,y=270)
     lbl_salary=Label(self.root,text="Salary", font=("goudy old style", 15), bg="white").place(x=480,y=270)

     self.txt_address=Text(self.root,font=("goudy old style", 15), bg="light yellow")
     self.txt_address.place(x=150,y=270,width=300,height=60)
     txt_salary=Entry(self.root,textvariable=self.var_salary, font=("goudy old style", 15), bg="light yellow").place(x=560,y=270,width=180)

     lbl_designation=Label(self.root,text="Designation", font=("goudy old style", 15), bg="white").place(x=750,y=270)
     txt_designation=Entry(self.root,textvariable=self.var_Designation, font=("goudy old style", 15), bg="light yellow").place(x=855,y=270,width=180)


    #========Buttons==========
     btn_search=Button(self.root,text="Save",command=self.add,font=("goudy old style",15), bg="#2196c3", fg="white",cursor="hand2").place(x=500,y=305,width=110,height="28")
     btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy old style",15), bg="#4caf55", fg="white",cursor="hand2").place(x=620,y=305,width=110,height="28")
     btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15), bg="#f44339", fg="white",cursor="hand2").place(x=740,y=305,width=110,height="28")
     btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15), bg="#607d9f", fg="white",cursor="hand2").place(x=860,y=305,width=110,height="28")
    #===========Employee Details==========
     emp_frame=Frame(self.root,bd=3,relief=RIDGE)
     emp_frame.place(x=0,y=350,relwidth=1,height=150)

     scrolly=Scrollbar(emp_frame,orient=VERTICAL)
     scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

     self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid", "name", "email", "gender","designation", "contact", "dob", "doj", "password", "uType", "address", "salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
     scrollx.pack(side=BOTTOM,fill=X)
     scrolly.pack(side=RIGHT,fill=Y)
     scrollx.config(command=self.EmployeeTable.xview)
     scrolly.config(command=self.EmployeeTable.yview)

     self.EmployeeTable.heading("eid", text="EMP ID")
     self.EmployeeTable.heading("name", text="Name")
     self.EmployeeTable.heading("email", text="Email")
     self.EmployeeTable.heading("gender", text="Gender")
     self.EmployeeTable.heading("designation", text="Designation")
     self.EmployeeTable.heading("contact", text="Contact")
     self.EmployeeTable.heading("dob", text="D.O.B")
     self.EmployeeTable.heading("doj", text="D.O.J")
     self.EmployeeTable.heading("password", text="Password")
     self.EmployeeTable.heading("uType", text="uType")
     self.EmployeeTable.heading("address", text="Address")
     self.EmployeeTable.heading("salary", text="Salary")

     self.EmployeeTable["show"]="headings"

     self.EmployeeTable.column("eid",width=90)
     self.EmployeeTable.column("name", width=110)
     self.EmployeeTable.column("email", width=100)
     self.EmployeeTable.column("gender", width=100)
     self.EmployeeTable.column("designation", width=100)
     self.EmployeeTable.column("contact", width=100)
     self.EmployeeTable.column("dob", width=100)
     self.EmployeeTable.column("doj", width=100)
     self.EmployeeTable.column("password", width=100)
     self.EmployeeTable.column("uType", width=100)
     self.EmployeeTable.column("address", width=100)
     self.EmployeeTable.column("salary", width=200)
     self.EmployeeTable.pack(fill=BOTH,expand=1)
     self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

     self.show()
    #=============================================
     
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
               messagebox.showerror("Error", "Employee ID must be required",parent=self.root)
            else:
               cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
               row=cur.fetchone()
               if row!=None:
                  messagebox.showerror("Error", "This Employee ID already assigned, try different ", parent=self.root)
               else:
                    cur.execute("Insert into employee (eid, name, email, gender, designation, contact, dob, doj, password, uType, address, salary) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                                            self.var_emp_id.get(),
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_Designation.get(),
                                            self.var_contact.get(),

                                            self.var_dob.get(),
                                            self.var_doj.get(),

                                            self.var_password.get(),
                                            self.var_uType.get(),
                                            self.txt_address.get("1.0", END),
                                            self.var_salary.get(),

                  ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
       
    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           cur.execute("Select * from employee")
           rows=cur.fetchall()
           self.EmployeeTable.delete(*self.EmployeeTable.get_children())
           for row in rows:
              self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


    def get_data(self,ev):
       f=self.EmployeeTable.focus()
       content=(self.EmployeeTable.item(f))
       row=content["values"]
      #  print(row)

       self.var_emp_id.set(row[0]),
       self.var_name.set(row[1]),
       self.var_email.set(row[2]),
       self.var_gender.set(row[3]),
       self.var_Designation.set(row[4]),
       self.var_contact.set(row[5]),

       self.var_dob.set(row[6]),
       self.var_doj.set(row[7]),

       self.var_password.set(row[8]),
       self.var_uType.set(row[9]),
       self.txt_address.delete("1.0",END),
       self.txt_address.insert(END,row[10]),
       self.var_salary.set(row[11]),


    def Update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
               messagebox.showerror("Error", "Employee ID must be required",parent=self.root)
            else:
               cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
               row=cur.fetchone()
               if row==None:
                  messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
               else:
                    cur.execute("Update employee set name=?, email=?, gender=?, designation=?, contact=?, dob=?, doj=?, password=?, uType=?, address=?, salary=? where eid=? ",(
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_gender.get(),
                                            self.var_Designation.get(),
                                            self.var_contact.get(),

                                            self.var_dob.get(),
                                            self.var_doj.get(),

                                            self.var_password.get(),
                                            self.var_uType.get(),
                                            self.txt_address.get("1.0", END),
                                            self.var_salary.get(),
                                            self.var_emp_id.get(),
                  ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()

        try:
            if self.var_emp_id.get()=="":
               messagebox.showerror("Error", "Employee ID must be required",parent=self.root)
            else:
               cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
               row=cur.fetchone()
               if row==None:
                  messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
               else:
                  op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
                  if op==True:
                     cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                     con.commit()
                     messagebox.showinfo("Delete", "employee Deleted successfully",parent=self.root)
                     self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
           
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_Designation.set(""),
        self.var_contact.set(""),

        self.var_dob.set(""),
        self.var_doj.set(""),

        self.var_password.set(""),
        self.var_uType.set("Admin"),
        self.txt_address.delete("1.0",END),
        self.var_salary.set(""),
        self.var_searchTxt.set(""),
        self.var_searchBy.set("Select"),
        self.show()

    def search(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           if self.var_searchBy.get()=="Select":
              messagebox.showerror("Error", "Select search By option", parent=self.root)
           elif self.var_searchTxt.get()=="":
              messagebox.showerror("Error", "Search input should be required", parent=self.root)
           else:
              cur.execute("Select * from employee where "+self.var_searchBy.get()+" LIKE '%"+self.var_searchTxt.get()+"%'")
              rows=cur.fetchall()
              if len(rows)!=0:
               self.EmployeeTable.delete(*self.EmployeeTable.get_children())
               for row in rows:
                   self.EmployeeTable.insert('',END,values=row)
              else:
                 messagebox.showerror("Error", "No record found!!!", parent=self.root)    
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

       

if __name__=="__main__":
   root=Tk()
   obj=employeeClass(root)
   root.mainloop()