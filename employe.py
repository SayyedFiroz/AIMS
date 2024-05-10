from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from tkinter import ttk,messagebox
import sqlite3
class emp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        self.root.focus_force()

    #ALL VARIABLE
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
       
        
        

    #FRAME
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=80)

    #OPTION
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_search.place(x=10,y=10,width=100,height=25)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=130,y=10,height=25)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",10),bg="green",fg="white",cursor="hand2").place(x=320,y=9,width=130, height=25)

    #TITLE
        title=Label(self.root,text="Employee Detail",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
    
    #CONTENT
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_gender.place(x=500,y=150,width=180,height=35)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
    
    #ROW2

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=200)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=200)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=200)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=200,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=200,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=200,width=180)

    #ROW3

        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=250)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=250)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",12),bg="white").place(x=750,y=250)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=250,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=250,width=180)
        #txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow").place(x=850,y=250,width=180)

        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employe"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_utype.place(x=850,y=250,width=180,height=35)
        cmb_utype.current(0)

    #ROW
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=470,y=300)

        txt_address=Entry(self.root,textvariable=self.var_address,font=("goudy old style",15),bg="lightyellow").place(x=150,y=300,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=580,y=300,width=180)
        

    #BUTTONS....
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",10),bd=3, bg="blue",fg="white",cursor="hand2").place(x=500,y=350,width=110, height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",10),bd=3, bg="green",fg="white",cursor="hand2").place(x=620,y=350,width=110, height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",10),bd=3, bg="red",fg="white",cursor="hand2").place(x=740,y=350,width=110, height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",10),bd=3, bg="darkblue",fg="white",cursor="hand2").place(x=860,y=350,width=110, height=28)

    #EMPLOYE DETAIL
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=380,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.employetable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employetable.xview)
        scrolly.config(command=self.employetable.yview)
        
        self.employetable.heading("eid",text="EMP ID")
        self.employetable.heading("name",text="NAME")
        self.employetable.heading("email",text="EMAIL")
        self.employetable.heading("gender",text="GENDER")
        self.employetable.heading("contact",text="CONTACT")
        self.employetable.heading("dob",text="DOB")
        self.employetable.heading("doj",text="DOJ")
        self.employetable.heading("pass",text="PASSWORD")
        self.employetable.heading("utype",text="USER TYPE")
        self.employetable.heading("address",text="ADDRESS")
        self.employetable.heading("salary",text="SALARY")

        self.employetable["show"]="headings"
            
        self.employetable.column("eid",width=100)
        self.employetable.column("name",width=100)
        self.employetable.column("email",width=100)
        self.employetable.column("gender",width=100)
        self.employetable.column("contact",width=100)
        self.employetable.column("dob",width=100)
        self.employetable.column("doj",width=100)
        self.employetable.column("pass",width=100)
        self.employetable.column("utype",width=100)
        self.employetable.column("address",width=100)
        self.employetable.column("salary",width=100)
        self.employetable.pack(fill=BOTH,expand=1)
        self.employetable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
##############################################################################
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employe ID Already Assigned To,Try Different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_emp_id.get(),
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),      
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.var_address.get(),
                                                self.var_salary.get(),                                               
                                                                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Addes Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.employetable.delete(* self.employetable.get_children())
            for row in rows:
                self.employetable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

    def get_data(self,ev):
        f=self.employetable.focus()
        content=(self.employetable.item(f))
        row=content['values']

        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])      
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.var_address.set(row[9])
        self.var_salary.set(row[10]) 
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid= ?",(
                                                
                                                self.var_name.get(),
                                                self.var_email.get(),
                                                self.var_gender.get(),
                                                self.var_contact.get(),
                                                self.var_dob.get(),
                                                self.var_doj.get(),      
                                                self.var_pass.get(),
                                                self.var_utype.get(),
                                                self.var_address.get(),
                                                self.var_salary.get(),
                                                self.var_emp_id.get(),                                                
                                                                                                    
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
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted Succucefully",parent=self.root)                 
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        f=self.employetable.focus()
        content=(self.employetable.item(f))
        row=content['values']
        print(row)

        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")      
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.var_address.set("")
        self.var_salary.set("")
        self.var_searchby.set("") 
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Searech By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input Should Be Reqiured",parent=self.root)
           
            else:    
                cur.execute("select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employetable.delete(* self.employetable.get_children())
                    for row in rows:
                        self.employetable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
 

if __name__=="__main__":

    root=Tk()
    obj=emp(root)
    root.mainloop()