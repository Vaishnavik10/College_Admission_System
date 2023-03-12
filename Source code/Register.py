import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
#import pymysql
from tkinter import ttk, messagebox
import mysql.connector

class Register:
     def __init__(self,root):
        self.root=root
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="gray" )

        self.bg=ImageTk.PhotoImage(file="Img11.jpg")
        bg=Label(self.root,image=self.bg).place(x=-10,y=0,relwidth=1,relheight=1)

        #header
        header=Frame(root, bg="orange", bd=0)
        header.place(x=80,y=5,width=1100,height=90)
        title=Label(header,text="Online Admission Form",font=("times new roman",25,"bold"),bg="orange",fg="white").place(x=390,y=30)
        

        #entries
        frame1=Frame(self.root,bg="misty rose",highlightbackground="black", highlightthickness=2)
        frame1.place(x=80,y=100,width=540,height=570)

        #registration
        title=Label(frame1,text="Registration",font=("times new roman",20,"bold"),bg="misty rose",fg="black").place(x=200,y=20)

        email1=Label(frame1,text="Email ID",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=80)
        self.txt_email1=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_email1.place(x=200,y=80)

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=120)
        self.txt_password=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_password.place(x=200,y=120)

        Confirm_password=Label(frame1,text="Confirm\n Password",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=160)
        self.txt_Confirm_password=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Confirm_password.place(x=200,y=160)
        #Students Details
        title=Label(frame1,text="Student Details",font=("times new roman",20,"bold"),bg="misty rose",fg="black").place(x=200,y=200)
        
        
        fname=Label(frame1,text="Full Name",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=260)
        self.txt_fname=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_fname.place(x=200,y=260)

        email=Label(frame1,text="Email ID",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=310)
        self.txt_email=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_email.place(x=200,y=310)

        DOB=Label(frame1,text="Date Of Birth",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=360)
        self.txt_DOB=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_DOB.place(x=200,y=360)
   
        category=Label(frame1,text="Category",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=410)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13,),width=30,state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Open","OBC","SC","ST","NT")
        self.cmb_quest.place(x=200,y=410)
        self.cmb_quest.current(0)


        Aadharno=Label(frame1,text="Aadhar No",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=450)
        self.txt_Aadharno=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Aadharno.place(x=200,y=450)

        Contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=500)
        self.txt_Contact=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Contact.place(x=200,y=500)
        

        
       
        #title=Label(frame1,text="",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=70)


        frame2=Frame(self.root,bg="misty rose",highlightbackground="black", highlightthickness=2)
        frame2.place(x=640,y=100,width=540,height=570)
        title=Label(frame2,text="Course Details",font=("times new roman",20,"bold"),bg="misty rose",fg="black").place(x=200,y=40)

        application=Label(frame2,text="Applicant Name",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=100)
        self.txt_application=Entry(frame2,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_application.place(x=200,y=100)

        class1=Label(frame2,text="Class",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=200)
        self.cmb_quest2=ttk.Combobox(frame2,font=("times new roman",15,),width=28,state="readonly",justify=CENTER)
        self.cmb_quest2['values']=("Select","S.E","T.E","B.E")
        self.cmb_quest2.place(x=200,y=200)
        self.cmb_quest2.current(0)

        department=Label(frame2,text="Department",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=150)
        self.cmb_quest3=ttk.Combobox(frame2,font=("times new roman",15,),width=28,state="readonly",justify=CENTER)
        self.cmb_quest3['values']=("Select","Computer Engineering","IT","E&TC","Civil Engineering","Mechanical Engineering","Electrical Engieering")
        self.cmb_quest3.place(x=200,y=150)
        self.cmb_quest3.current(0)

        University=Label(frame2,text="University",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=250)
        self.cmb_quest4=ttk.Combobox(frame2,font=("times new roman",15,),width=28,state="readonly",justify=CENTER)
        self.cmb_quest4['values']=("Select","Savitribai Phule Pune University")
        self.cmb_quest4.place(x=200,y=250)
        self.cmb_quest4.current(0)

       
        
        Appl_date=Label(frame2,text="Application Date",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=310)
        self.txt_Appl_date=Entry(frame2,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Appl_date.place(x=200,y=310)

        year=Label(frame2,text="Year of \nAdmisson",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=370)
        self.txt_year=Entry(frame2,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_year.place(x=200,y=370)

        prn=Label(frame2,text="PRN No.\n(if existing student)",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=430)
        self.txt_prn=Entry(frame2,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_prn.place(x=200,y=430)

        btn = Button(frame2, text = "Submit",font=("times new roman",20,"bold"),bg="light Green",bd=1,command=self.register_data).place(x=200,y=490,height=50, width=200)
     def register_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Register(self.new_win)

     #Connection code

     def register_data(self):
        if self.txt_email1.get()==""or self.txt_password.get()==""or self.txt_fname.get()==""or self.txt_email.get()==""or self.txt_DOB.get()==""or self.cmb_quest.get()=="Select"or self.txt_Aadharno.get()==""or self.txt_Contact.get()==""or self.txt_application.get()==""or self.cmb_quest2.get()=="Select" or self.cmb_quest3.get()=="Select"or self.cmb_quest4.get()=="Select"or self.txt_Appl_date.get()==""or self.txt_year.get()==""or self.txt_prn.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_Confirm_password.get():
                messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        else:
                try:
                        con=mysql.connector.connect(host="localhost",user="root",password="",database="admission3")
                        cur=con.cursor()
                        sqlquery="insert into Register(email1,password) values(%s,%s)"
                        mydata=self.txt_email1.get(),self.txt_password.get()
                        sqlquery1="insert into form(fname,email,DOB,category,Aadharno,Contact) values(%s,%s,%s,%s,%s,%s)"
                        mydata1=self.txt_fname.get(),self.txt_email.get(),self.txt_DOB.get(),self.cmb_quest.get(),self.txt_Aadharno.get(),self.txt_Contact.get()
                        sqlquery2="insert into Course(application,department,class1,University,Appl_date,year,prn) values(%s,%s,%s,%s,%s,%s,%s)" 
                        mydata2=self.txt_application.get(),self.cmb_quest2.get(),self.cmb_quest3.get(),self.cmb_quest4.get(),self.txt_Appl_date.get(),self.txt_year.get(),self.txt_prn.get() 
                        
                        
                        cur.execute(sqlquery,mydata,)
                        cur.execute(sqlquery1,mydata1)
                        cur.execute(sqlquery2,mydata2)
                                
                        con.commit()
                        con.close()
                        messagebox.showinfo("Successfull","Submitted Successfully",parent=self.root)

                except Exception as es:
                        messagebox.showerror("Error",f"Errordue to: {str(es)}",parent=self.root)


root=Tk()
obj=Register(root)
root.mainloop()

