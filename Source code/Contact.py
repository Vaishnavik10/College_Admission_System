import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

class Contact:
    def __init__(self,root):
        self.root=root
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="light gray" )

        header=Frame(root, bg="orange", bd=0)
        header.place(x=80,y=5,width=1100,height=90)
        title=Label(header,text="Contact Us",font=("times new roman",30,"bold"),bg="orange",fg="white").place(x=480,y=30)
        
        self.bg=ImageTk.PhotoImage(file="img5.png")
        bg=Label(self.root,image=self.bg).place(x=80,y=100,width=1100,height=450)  

        def Contact_info(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=Contact(self.new_win)



root=Tk()
obj=Contact(root)
root.mainloop()