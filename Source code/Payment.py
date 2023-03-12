import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

class Payment:
    def __init__(self,root):
        self.root=root
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="light gray" )

        self.bg=ImageTk.PhotoImage(file="Img11.jpg")
        bg=Label(self.root,image=self.bg).place(x=-10,y=0,relwidth=1,relheight=1)

        header=Frame(root, bg="orange", bd=0)
        header.place(x=80,y=5,width=1100,height=90)
        title=Label(header,text="Payment Details",font=("times new roman",30,"bold"),bg="orange",fg="white").place(x=480,y=30)

        
        frame1=Frame(self.root,bg="misty rose",highlightbackground="black", highlightthickness=2)
        frame1.place(x=350,y=100,width=600,height=570,)

        PID=Label(frame1,text="Payment ID",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=110)
        self.txt_PID=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_PID.place(x=200,y=110)

        Amount=Label(frame1,text="Amount",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=160)
        self.txt_Amount=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Amount.place(x=200,y=160)

        Time=Label(frame1,text="Time",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=210)
        self.txt_Time=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Time.place(x=200,y=210)

        Date=Label(frame1,text="Date Of\n Payment",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=260)
        self.txt_Date=Entry(frame1,font=("times new roman",15,),bg="light gray",width=30)
        self.txt_Date.place(x=200,y=260)
   
        mode=Label(frame1,text="Payment Mode",font=("times new roman",15,"bold"),bg="misty rose",fg="black").place(x=50,y=320)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13,),width=30,state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Online","Offline")
        self.cmb_quest.place(x=200,y=320)
        self.cmb_quest.current(0)

        btn = Button(frame1, text = "Submit",font=("times new roman",20,"bold"),bg="light Green",bd=1,command=self.Payment_data).place(x=200,y=420,height=50, width=200)
        
    
    def Payment_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Payment(self.new_win)

    def Payment_data(self):
        if self.txt_PID.get()==""or self.txt_Amount.get()==""or self.txt_Time.get()==""or self.txt_Date.get()==""or self.cmb_quest.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
                try:
                        con=mysql.connector.connect(host="localhost",user="root",password="",database="admission3")
                        cur=con.cursor()
                        sqlquery1="insert into payment_details(PID,Amount,Time,Date,mode) values(%s,%s,%s,%s,%s)"
                        mydata1=self.txt_PID.get(),self.txt_Amount.get(),self.txt_Time.get(),self.txt_Date.get(),self.cmb_quest.get()
                        cur.execute(sqlquery1,mydata1)
                                
                        con.commit()
                        con.close()
                        messagebox.showinfo("Successfull","Submitted Successfully",parent=self.root)

                except Exception as es:
                        messagebox.showerror("Error",f"Errordue to: {str(es)}",parent=self.root)





root=Tk()
obj=Payment(root)
root.mainloop()