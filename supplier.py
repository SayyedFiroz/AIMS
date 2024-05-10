from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from tkinter import ttk,messagebox
import sqlite3
class supp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        self.root.focus_force()

    #ALL VARIABLE
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_inv=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_description=StringVar()

    #OPTION
        lbl_search=Label(self.root,text="Invoice No:",bg="white",font=("goudy old style",10))
        lbl_search.place(x=700,y=80)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=790,y=80,width=150,height=25)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",10),bg="green",fg="white",cursor="hand2").place(x=950,y=80,width=100, height=25)

    #TITLE
        title=Label(self.root,text="Supplier Detail",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)
    
    #CONTENT

    #ROW1
        lbl_supinv=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
        txt_supinv=Entry(self.root,textvariable=self.var_sup_inv,font=("goudy old style",15),bg="lightyellow").place(x=200,y=80,width=180)
    
    #ROW2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=200,y=120,width=180)

    #ROW3

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=200,y=160,width=180)


    #ROW
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)

        txt_desc=Entry(self.root,textvariable=self.var_description,font=("goudy old style",15),bg="lightyellow").place(x=200,y=200,width=450,height=100)
        

    #BUTTONS....
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",10),bd=3, bg="blue",fg="white",cursor="hand2").place(x=200,y=370,width=110, height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",10),bd=3, bg="green",fg="white",cursor="hand2").place(x=320,y=370,width=110, height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",10),bd=3, bg="red",fg="white",cursor="hand2").place(x=440,y=370,width=110, height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",10),bd=3, bg="darkblue",fg="white",cursor="hand2").place(x=560,y=370,width=110, height=35)

    #EMPLOYE DETAIL
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=120,width=380,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.suppliertable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.suppliertable.xview)
        scrolly.config(command=self.suppliertable.yview)
        
        self.suppliertable.heading("invoice",text="Invoice No.")
        self.suppliertable.heading("name",text="Name")
        self.suppliertable.heading("contact",text="Contact")
        self.suppliertable.heading("desc",text="Description")

        self.suppliertable["show"]="headings"
            
        self.suppliertable.column("invoice",width=100)
        self.suppliertable.column("name",width=100)
        self.suppliertable.column("contact",width=100)
        self.suppliertable.column("desc",width=100)
        
        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind("<ButtonRelease-1>",self.get_data)
       # self.show()
##############################################################################
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_inv.get()=="":
                messagebox.showerror("Error","Invoive Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_inv.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice No, Already Assigned,Try Different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                                self.var_sup_inv.get(),
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.var_description.get(),
                                                                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppliertable.delete(* self.suppliertable.get_children())
            for row in rows:
                self.suppliertable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        if row:
            self.var_sup_inv.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.var_description.set(row[3])
        else:
            print()
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_inv.get()=="":
                messagebox.showerror("Error","Invoice No. Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_inv.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice= ?",(
                                                
                                                self.var_name.get(),
                                                self.var_contact.get(),
                                                self.var_description.get(),
                                                self.var_sup_inv.get(),                                                
                                                                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_inv.get()=="":
                messagebox.showerror("Error","Invoice No. Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_inv.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_inv.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Succucefully",parent=self.root)                 
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        print(row)

        self.var_sup_inv.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_description.set("") 
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:       
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoive No. Should Be Reqiured",parent=self.root)
           
            else:    
                cur.execute("select * from supplier where invoice=?" , (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.suppliertable.delete(* self.suppliertable.get_children())
                    self.suppliertable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
 

if __name__=="__main__":

    root=Tk()
    obj=supp(root)
    root.mainloop()