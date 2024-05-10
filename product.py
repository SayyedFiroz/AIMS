from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from tkinter import ttk,messagebox
import sqlite3
class pdt:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        self.root.focus_force()

    #variable
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_date=StringVar()
        self.var_batchno=StringVar()
    #PRODUCT FRAME

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=500)

        title=Label(product_Frame,text="Manage Product Detail",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
    #COLOUMN !
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",12),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",12),bg="white").place(x=30,y=110)
        lbl_name=Label(product_Frame,text="Name",font=("goudy old style",12),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",12),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quntity",font=("goudy old style",12),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",12),bg="white").place(x=30,y=310)
        lbl_date=Label(product_Frame,text="EXP Date",font=("goudy old style",12),bg="white").place(x=30,y=360)
        lbl_batch=Label(product_Frame,text="Batch No.",font=("goudy old style",12),bg="white").place(x=30,y=410)


 #COLOUNM
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=160,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)
       
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
        txt_date=Entry(product_Frame,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=150,y=360,width=200)
        txt_batchno=Entry(product_Frame,textvariable=self.var_batchno,font=("goudy old style",15),bg="lightyellow").place(x=150,y=410,width=200)
       
    #BUTTON

        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",10),bd=3, bg="blue",fg="white",cursor="hand2").place(x=10,y=450,width=100, height=35)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",10),bd=3, bg="green",fg="white",cursor="hand2").place(x=120,y=450,width=100, height=35)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",10),bd=3, bg="red",fg="white",cursor="hand2").place(x=230,y=450,width=100, height=35)
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",10),bd=3, bg="darkblue",fg="white",cursor="hand2").place(x=340,y=450,width=100, height=35)
   
    #Search Frame

        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=480,y=10,width=600,height=80)

    
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name","Date"),state='readonly',justify=CENTER,font=("goudy old style",10))
        cmb_search.place(x=10,y=10,width=100,height=25)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",10),bg="lightyellow").place(x=130,y=10,height=25)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",10),bg="green",fg="white",cursor="hand2").place(x=320,y=9,width=130, height=25)
    
    #PRODUCT DETAIL

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.producttable=ttk.Treeview(p_frame,columns=("pid","category","supplier","name","price","qty","status","date","batchno"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.producttable.xview)
        scrolly.config(command=self.producttable.yview)
    
        self.producttable.heading("pid",text="Product")
        self.producttable.heading("category",text="Category")
        self.producttable.heading("supplier",text="Supplier")
        self.producttable.heading("name",text="Name")
        self.producttable.heading("price",text="Price")
        self.producttable.heading("qty",text="Quantity")
        self.producttable.heading("status",text="Status")
        self.producttable.heading("date",text="EXP Date")
        self.producttable.heading("batchno",text="Batch No")

        self.producttable["show"]="headings"
            
        self.producttable.column("pid",width=100)
        self.producttable.column("category",width=100)
        self.producttable.column("supplier",width=100)
        self.producttable.column("name",width=100)
        self.producttable.column("price",width=100)
        self.producttable.column("qty",width=100)
        self.producttable.column("status",width=100)
        self.producttable.column("date",width=100)
        self.producttable.column("batchno",width=100)
        self.producttable.pack(fill=BOTH,expand=1)
        self.producttable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
         
                for i in cat:
                    self.cat_list.append(i[0])
        
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
         
                for i in sup:
                    self.sup_list.append(i[0])
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                            

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All Field Required Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product Already Present,Try Different",parent=self.root)
                else:
                    cur.execute("Insert into product (category,supplier,name,price,qty,status,date,batchno) values(?,?,?,?,?,?,?,?)",(
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                self.var_date.get(),      
                                                self.var_batchno.get(),
                                                                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.producttable.delete(* self.producttable.get_children())
            for row in rows:
                self.producttable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        

    def get_data(self,ev):
        f=self.producttable.focus()
        content=(self.producttable.item(f))
        row=content['values']
        if row:
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_sup.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6])
            self.var_date.set(row[7])      
            self.var_batchno.set(row[8])
        else:
            print()
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product",parent=self.root)

            #elif self.var_name.get()=="":
             #   messagebox.showerror("Error","Name Must Be Required",parent=self.root) 
                   
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error"," Invalid Product",parent=self.root)
                else:
                    cur.execute("Update product set category=?,supplier=?,name=?,price=?,qty=?,status=?,date=?,batchno=? where pid= ?",(
                                                
                                                self.var_cat.get(),
                                                self.var_sup.get(),
                                                self.var_name.get(),
                                                self.var_price.get(),
                                                self.var_qty.get(),
                                                self.var_status.get(),
                                                self.var_date.get(),      
                                                self.var_batchno.get(),
                                                self.var_pid.get()                                                
                                                                                                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select Product From The List",parent=self.root)           
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Succucefully",parent=self.root)                 
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        f=self.producttable.focus()
        content=(self.producttable.item(f))
        row=content['values']


        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_date.set("")      
        self.var_batchno.set("")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select") 
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
                cur.execute("select * from product where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.producttable.delete(* self.producttable.get_children())
                    for row in rows:
                        self.producttable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
 

if __name__=="__main__":

    root=Tk()
    obj=pdt(root)
    root.mainloop()