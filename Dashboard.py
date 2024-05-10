from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from employe import emp
from supplier import supp
from category import cat
from product import pdt
from sales import sales
from billing import bill
import sqlite3
from tkinter import messagebox
import os
import time
import hashlib
from tkinter.simpledialog import askstring

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        #TITILE
        self.icon_title=PhotoImage(file="images/icon.png")
        title=Label(self.root,text="Inventory Management",image=self.icon_title,compound=LEFT, font=("times new roman",35,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,relwidth=1,height=70)
         
        #logout btn
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15, "bold"),bd=3,bg="Red",cursor="hand2").place(x=1100,y=10,height=50,width=150)    
        # Make Bill Button
        btn_makebill=Button(self.root,text="Make Bill",command=self.bills,font=("times new roman",15, "bold"),bd=3,bg="lightgreen",cursor="hand2").place(x=900,y=10,height=50,width=150)    

        #Clock
        self.lbl_clock=Label(self.root,text="Welcome To Management\t\t Date;DD-MM-YYYY\t\t Time:HH-MM-SS",font=("times new roman",15,),bg="#4d636d",fg="white",anchor="w")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Left Menu
        self.Menulogo=Image.open("images/menu_im.png")
        self.Menulogo=self.Menulogo.resize((200,160),Image.BILINEAR)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
       
        btn_emp=Button(LeftMenu,text="Employe",command=self.employe ,image=self.icon_side ,compound=LEFT, padx=5, anchor=W, font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side ,compound=LEFT, padx=5, anchor=W, font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side ,compound=LEFT, padx=5, anchor=W, font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side ,compound=LEFT, padx=5, anchor=W, font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sale",command=self.sales,image=self.icon_side ,compound=LEFT, padx=5, anchor=W, font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit_application,image=self.icon_side ,compound=LEFT, padx=5, anchor=W , font=("times new roman",15, "bold"),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_reset_sales = Button(LeftMenu, text="Reset Sales", command=self.reset_sales, image=self.icon_side,compound=LEFT, padx=5, anchor=W, font=("times new roman", 15, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        #content

        self.lbl_employe=Label(self.root,text="Total Employe\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style", 20,"bold"))
        self.lbl_employe.place(x=300,y=120,height=110,width=250)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style", 20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=110,width=250)

        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style", 20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=110,width=250)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style", 20,"bold"))
        self.lbl_product.place(x=300,y=300,height=110,width=250)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style", 20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=110,width=250)

       

        #footer
        self.lbl_footer=Label(self.root,text="Inventory Management | Developed BY SAYYED FIROZ \n For Any Technical Issue Contact: 8828532248 " ,font=("times new roman",12,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        self.update_content()
###############################################################################
    def employe(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=emp(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supp(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=cat(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=pdt(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=sales(self.new_win)

    def bills(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=bill(self.new_win)
        


    def exit_application(self):
        self.root.destroy() 


    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()


        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employe=cur.fetchall()
            self.lbl_employe.config(text=f'Total Employe\n[{str(len(employe))}]')

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome To Management\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

  
    def reset_sales(self):
        try:
            # Ask for confirmation
            confirmation = messagebox.askyesno("Reset Sales", "Are you sure you want to reset sales?")
            if not confirmation:
                return  # If the user clicks 'No', do nothing

            # Prompt for admin password
            admin_password = askstring("Admin Password", "Enter Admin Password:", show='*')

            # Check if the entered password matches any admin password stored in the database
            if self.is_valid_admin_password(admin_password):
                # Connect to the database

                # Clear the contents of the 'bill' directory (assuming it contains sales records)
                bill_directory = 'bill'
                for file_name in os.listdir(bill_directory):
                    file_path = os.path.join(bill_directory, file_name)
                    os.remove(file_path)

                # Update the sales label to show zero sales
                self.lbl_sales.config(text='Total Sales\n[0]')
                messagebox.showinfo("Success", "Sales reset successfully", parent=self.root)
            else:
                messagebox.showerror("Authentication Failed", "Invalid Admin Password", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error resetting sales: {str(ex)}", parent=self.root)

    def is_valid_admin_password(self, entered_password):
        try:
            # Connect to the database
            con = sqlite3.connect(database=r'ims.db')
            cur = con.cursor()

            # Execute SQL to fetch all admin passwords from the employee table
            cur.execute("SELECT pass FROM employee WHERE utype='Admin'")
            admin_passwords_from_db = [row[0] for row in cur.fetchall()]

            # Close the connection
            con.close()

            # Check if the entered password matches any admin password
            return entered_password in admin_passwords_from_db

        except Exception as ex:
            messagebox.showerror("Error", f"Error validating admin password: {str(ex)}", parent=self.root)
            return False




if __name__=="__main__":

    root=Tk()
    obj=IMS(root)
    root.mainloop()
    