from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='#fafafa')

        self.otp=''
        ######images######
        self.phone_image=ImageTk.PhotoImage(file="images/phone.jpg")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)


    ###########Login Frame########
        self.empid=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login Here",font=("Elephant",30,"bold"),bg="white",bd=0).place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee ID",font=("Andalus",15,),bg="white",fg="#767171").place(x=50,y=100)

        txt_user=Entry(login_frame,textvariable=self.empid ,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*", font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Log In",command=self.login,font=("gloudy old style",15,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",font=("times old roman",15,"bold"),fg="lightgray",bg="white").place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget,font=("times old roman",12),bd=0,bg="white",fg="#00759E",activebackground="white",activeforeground="#00759E").place(x=90,y=390)

    #####Frame @2############

        register_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="All growth depends\n upon activity..",font=("italic",12,"bold"),bg="white").place(x=75,y=0)

    #####Animation Images######
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()
    

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(1000,self.animate)





    def login(self):
        
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()


        try:
            if self.empid.get()=="" or self.password.get()=="":
                messagebox.showerror('Error',"All Field Are Required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.empid.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error',"Invalid EMPLOYE ID/PASSWORD",parent=self.root)
                else:
                    if user[0]=="Admin":

                        self.root.destroy()
                        os.system("python Dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def forget(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.empid.get()=="":
                messagebox.showerror('Error',"Employee ID Required",parent=self.root)
            else:
                 cur.execute("select email from employee where eid=?",(self.empid.get(),))
                 email=cur.fetchone()

                 if email==None:
                     messagebox.showerror('Error',"Invalid Employee ID ,Try Again!",parent=self.root)
                 else:    

                    if email[0]==None or email[0]=="":
                        messagebox.showerror('Error', "Employee ID Is Valid, But No Email is Linked.\nKindly Contact Your Admin", parent=self.root)

                    else:
                        #######Forget Window
                        self.var_otp=StringVar()
                        self.var_new_pass=StringVar()
                        self.var_conf_pass=StringVar()

                        #####call send email function
                        chk=self.send_email(email[0])
                        if chk!='s':
                            messagebox.showerror('Error',"Connection Error,try again",parent=self.root)
                        else:
                            self.forget_win=Toplevel(self.root)
                            self.forget_win.title("Forget Password")
                            self.forget_win.geometry('400x350+500+100')
                            self.forget_win.focus_force()

                            title=Label(self.forget_win,text='Reset Password',font=("goudy old style",15,"bold"),bg="#3F51B5",fg="white").pack(side=TOP,fill=X)
                            lbl_reset=Label(self.forget_win,text='Enter OTP Sent On Registred Email',font=("times old roman",11,)).place(x=20,y=60)
                            txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times old roman",10,),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                            self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("goudy old style",11,),bd=3,bg="lightblue")
                            self.btn_reset.place(x=280,y=98,width=98,height=28)

                            lbl_pass=Label(self.forget_win,text='New Password',font=("times old roman",11,)).place(x=20,y=160)
                            txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times old roman",10,),bg="lightyellow").place(x=20,y=190,width=250,height=30)

                            co_pass=Label(self.forget_win,text='Confirm Password',font=("times old roman",11,)).place(x=20,y=225)
                            txt_co_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times old roman",10,),bg="lightyellow").place(x=20,y=250,width=250,height=30)

                            self.btn_update=Button(self.forget_win,text="UPDATE",state='disabled',command=self.update_password,font=("goudy old style",11,),bd=3,bg="lightblue")
                            self.btn_update.place(x=150,y=300,width=98,height=28)



        except Exception as ex:
                messagebox.showerror("Error","Check Internet Connection",parent=self.root)

    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror('Error',"Password is required",parent=self.forget_win)

        elif self.var_new_pass.get()!=self.var_conf_pass.get(): 
            messagebox.showerror('Error',"New Password & Confirm Password Should Be Same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",(self.var_new_pass.get(),self.empid.get()))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successflly",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state='disabled')
            messagebox.showinfo('OTP',"OTP Verification Succesful",parent=self.forget_win)

        else:
            messagebox.showerror('Error',"Invalid OTP, Try Again",parent=self.forget_win)
               
 
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)
        self.otp=int(time.strftime("%M%S%H"))+int(time.strftime("%S"))
        

        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'



root=Tk()
obj=Login(root)
root.mainloop()