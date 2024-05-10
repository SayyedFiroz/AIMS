from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from tkinter import ttk,messagebox
import sqlite3
class cat:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #VARIABLE
        self.var_catid=StringVar()
        self.var_name=StringVar()

    #TITILE
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="darkblue",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30)).place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15),bg="green",fg="white",bd=3,cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",bd=3,cursor="hand2").place(x=520,y=170,width=150,height=30)

    #CATREGORY DETAIL

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=120,width=380,height=100)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categorytable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categorytable.xview)
        scrolly.config(command=self.categorytable.yview)
        
        self.categorytable.heading("cid",text="Category ID.")
        self.categorytable.heading("name",text="Name")

        self.categorytable["show"]="headings"
            
        self.categorytable.column("cid",width=100)
        self.categorytable.column("name",width=100)
        
        self.categorytable.pack(fill=BOTH,expand=1)
        self.categorytable.bind("<ButtonRelease-1>",self.get_data)
       
    #Images
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.BILINEAR)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,250),Image.BILINEAR)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        self.show()
    
    #FUNCCTIONS...

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name Must Be Required",parent=self.root)           
            else:
                cur.execute("Select * from category where cid=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category Already Present,Try Different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),)
                                              
                                                                                                    
                    )
                    con.commit()
                    messagebox.showinfo("Success","Category Added Succefully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categorytable.delete(* self.categorytable.get_children())
            for row in rows:
                self.categorytable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def get_data(self,ev):
        f=self.categorytable.focus()
        content=(self.categorytable.item(f))
        row=content['values']

        self.var_catid.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_catid.get()=="":
                messagebox.showerror("Error","Please Select Category from the list",parent=self.root)           
            else:
                cur.execute("Select * from category where cid=?",(self.var_catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Try Again.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_catid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Succucefully",parent=self.root)                 
                        self.show()
                        self.var_catid.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":

    root=Tk()
    obj=cat(root)
    root.mainloop()