from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import billingClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
   def __init__(self,root):
     self.root=root
     self.root.geometry("1500x1000+0+0")
     self.root.title("Municipal Committee Sehwan Management System | Developed By Majid Meerani Sehwani")
     self.root.config(bg="white")
   #   self.icon_title=PhotoImage(file="Images/government-of-Sindhi-pakistan-logo1.png")

     self.icon_title=Image.open("Images/government-of-Sindhi-pakistan-logo1.png")
     self.icon_title = self.icon_title.resize((130, 130), Image.Resampling.LANCZOS)
     self.icon_title=ImageTk.PhotoImage(self.icon_title)
   #   lbl_icon_title=Label(lbl_icon_title,image=self.icon_title)
   #   lbl_icon_title.pack(side=TOP,fill=X)


     title=Label(self.root,text="Municipal Committee Sehwan MIS",image=self.icon_title, compound=LEFT, font=("times new roman", 40,"bold"), bg="#010c48", fg="white" , anchor="w", padx=10).place(x=0,y=0,relwidth=1,height=170)

        #=================Button Logout================
     btn_logout=Button(self.root,text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150,y=15,height=30,width=150)

        #=========Clock============
     
     self.lbl_clock=Label(self.root,text="Welcome to Town Commitee Sehwan MIS\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15), bg="#4d636d", fg="white")
     self.lbl_clock.place(x=0,y=170,relwidth=1,height=30)

    #===============Left Menu===============
     
     self.MenuLogo=Image.open("Images/inventory-management-system-png.png")
     self.MenuLogo=self.MenuLogo.resize((150,150),Image.Resampling.LANCZOS)
     self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

     leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
     leftMenu.place(x=0,y=204,height=560)

     lbl_menuLogo=Label(leftMenu,image=self.MenuLogo)
     lbl_menuLogo.pack(side=TOP,fill=X)

     self.icon_side=PhotoImage(file="images/side arrow.png")
     lbl_menu=Label(leftMenu,text="Menu", font=("times new roman",20), bg="#009688").pack(side=TOP,fill=X)
     
     btn_employee=Button(leftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
     btn_supplier=Button(leftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
     btn_category=Button(leftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
     btn_product=Button(leftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
     btn_sales=Button(leftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
     btn_billing=Button(leftMenu,text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=5, anchor="w", font=("times new roman",20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

      #===========Content==============
     self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20,"bold"))
     self.lbl_employee.place(x=300,y=220,height=130,width=300)

     self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20,"bold"))
     self.lbl_supplier.place(x=650,y=220,height=130,width=300)

     self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20,"bold"))
     self.lbl_category.place(x=1000,y=220,height=130,width=300)

     self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old style", 20,"bold"))
     self.lbl_product.place(x=300,y=400,height=130,width=300)

     self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20,"bold"))
     self.lbl_sales.place(x=650,y=400,height=130,width=300)


      
      
      #============Footer===========
     lbl_footer=Label(self.root,text="Town Committee Sehwan MIS | Developed by Majid Meerani\nFor any technical issue Contact: 923003772293", font=("times new roman",12), bg="#4d636d", fg="white").pack(side=BOTTOM,fill=X)

     self.update_content()
#=======================================================
   def employee(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=employeeClass(self.new_win)

   def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win)


   def category(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=categoryClass(self.new_win)   
   
   def product(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productClass(self.new_win)   

   def sales(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=salesClass(self.new_win) 

   def billing(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=billingClass(self.new_win)   

   def update_content(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:   
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_=time.strftime('%I:%M:%S')
            date_=time.strftime('%d-%m-%Y')
            self.lbl_clock.config(text=f"Welcome to Municipal Committee Sehwan MIS\t\t Date:{str(date_)}\t\t Time: {str(time_)}",font=("times new roman",15), bg="#4d636d", fg="white")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)


   def logout(self):
      self.root.destroy()
      os.system("python login.py")

if __name__=="__main__":
   root=Tk()
   obj=IMS(root)
   root.mainloop()