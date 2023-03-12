import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
#from view import view
from About import About
from Contact import Contact
from Payment import Payment
from Register import Register




class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="light gray" )
        
        #bg image
        #self.bg=ImageTk.PhotoImage(file="img4.jpg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #Header
        header=Frame(root, bg="orange", bd=0)
        header.place(x=80,y=5,width=1100,height=90)
        title=Label(header,text="SVPM's College Of Engineering Malegaon Bk Baramati.",font=("times new roman",25,"bold"),bg="orange",fg="white").place(x=230,y=30)
          
        #logo
        image1 = Image.open("logo123.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(header,image=test)
        label1.image=test
        label1.place(x=10, y=0, height=90,width=90)

        #left image
        self.bg=ImageTk.PhotoImage(file="img4.jpg")
        bg=Label(self.root,image=self.bg).place(x=80,y=100,width=400,height=550)
        
        #register frame
        frame1=Frame(self.root,bg="misty rose",highlightbackground="black", highlightthickness=2)
        frame1.place(x=480,y=100,width=700,height=550)
        title=Label(frame1,text="Online Admission System",font=("times new roman",20,"bold"),bg="light green",fg="black").place(x=220,y=30)



        #buttons
        btn = Button(frame1, text = "Register",command=self.register_info,font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=100,y=100,height=50, width=200)
        btn = Button(frame1, text = "Search",font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=450,y=100,height=50, width=200)
        btn = Button(frame1, text = "Contact Us",command=self.Contact_info,font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=100,y=400,height=50, width=200)
        btn = Button(frame1, text = "About",command=self.about_info,font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=450,y=400,height=50, width=200)
        btn = Button(frame1, text = "View",font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=450,y=250,height=50, width=200)  
        btn = Button(frame1, text = "Payment",command=self.Payment_info,font=("times new roman",20,"bold"),bg="light blue",bd=1).place(x=100,y=250,height=50, width=200)  

        #calling function

    def register_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Register(self.new_win)

    """def login_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=search2(self.new_win)"""

    def Contact_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Contact(self.new_win)

    
    def about_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=About(self.new_win)

    """def view_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=search(self.new_win)"""
    
    def Payment_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Payment(self.new_win)
    

       # command=self.view_info,
    
        

        


root=Tk()
obj=Home(root)
root.mainloop()