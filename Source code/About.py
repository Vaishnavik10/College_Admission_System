import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

class About:
    def __init__(self,root):
        self.root=root
        
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="light gray" )

        header=Frame(root, bg="orange", bd=0)
        header.place(x=80,y=5,width=1100,height=90)
        title=Label(header,text="About Us",font=("times new roman",30,"bold"),bg="orange",fg="white").place(x=480,y=30)

        self.bg=ImageTk.PhotoImage(file="img9.png")
        bg=Label(self.root,image=self.bg).place(x=80,y=100,width=1100,height=580)  

        """ self.bg2=ImageTk.PhotoImage(file="new.jpg")
                bg2=Label(self.root,image=self.bg2).place(x=580,y=100,width=600,height=250)

        frame1=Frame(self.root,bg="misty rose",highlightbackground="black", highlightthickness=2)
        frame1.place(x=80,y=400,width=1100,height=250)"""


        """ self.root=Tk()
        T = Text(self.root, height = 5, width = 52)
        Fact = """"""The Institute is being managed under the presidentship of Hon. Shri. Sharadchandraji Pawar, Ex Minister for Agriculture, Govt. of India and Ex. Chief Minister of Maharashtra. The Institute was established in the year 1990 under the auspices of Shivnagar Vidya Prasarak Mandal at Malegaon (Bk)Tal - Baramati, Dist - Pune.""""""
        #T.insert(tk.END, Fact)
        text_box = Text(T,height=13,width=40)
        text_box.pack(expand=True)
        text_box.insert('end', Fact)
        T.mainloop()"""
   
    def about_info(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=About(self.new_win)




        self.bg=ImageTk.PhotoImage(file="img4.jpg")
        bg=Label(self.root,image=self.bg).place(x=80,y=100,width=400,height=550)    

        
root=Tk()
obj=About(root)
root.mainloop()
