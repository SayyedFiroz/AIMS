from tkinter import*
from PIL import Image,ImageTk #PIP INSTALL PILLOW
from tkinter import ttk,messagebox
import sqlite3
import os
from billing import bill
class sales:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("Inventory Managment")
        self.root.config(bg="white")
        self.root.focus_force()
        self.bill_list=[]
        self.var_invoice=StringVar()

        lbl_title=Label(self.root,text="Customer Bill",font=("goudy old style",30),bg="darkblue",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice=Label(self.root,text="Invoice No.",font=("time new roman",12),bg="white").place(x=50,y=100)  
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",12),bg="lightyellow").place(x=160,y=100,width=180,height=25)

        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=25)   
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="lightgray",fg="black",cursor="hand2").place(x=490,y=100,width=120,height=25)

    #Bill List
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=20,y=140,width=200,height=330)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_Frame,font=("goudy old style",11),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

    #Bill Area
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)

        lbl_title=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("Times New Roman CE",8),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)


    #IMAGE
        self.bill_img=Image.open("images/cat2.jpg")
        self.bill_img=self.bill_img.resize((450,300),Image.BILINEAR)
        self.bill_img=ImageTk.PhotoImage(self.bill_img)

        lbl_image=Label(self.root,image=self.bill_img,bd=0)
        lbl_image.place(x=700,y=110)
        self.show()


    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name) 
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close() 

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)








if __name__=="__main__":

    root=Tk()
    obj=sales(root)
    root.mainloop()