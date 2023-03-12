from tkinter import ttk
import tkinter as tk
import mysql
import mysql.connector
from sqlalchemy.sql.selectable import Select

class view:
    def __init__(self,root):
        self.root=root
        self.root.title("SVPM COE Malegaon Bk Baramati-Student Admission System")
        self.root.geometry("1366x700+0+0")
        self.root.config(bg="misty rose" )




       

    my_conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="admission3",port="3306")
    r_set=my_conn.cursor()
    r_set.execute("SELECT * from form")


    my_w=tk.Tk()
    my_w.geometry('1000x700')
    my_w.config(bg="misty rose")
    my_w.title("SVPM COE Malegaon Bk Baramati-Student Admission System")

    
    trv=ttk.Treeview(my_w,selectmode='browse')
    trv.grid(row=1,column=1,padx=100,pady=50)
    trv["columns"]=("1","2","3","4","5","6")
    trv['show']='headings'
    trv.column("1",width=180,anchor='c')
    trv.column("2",width=200,anchor='c')
    trv.column("3",width=80,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=120,anchor='c')
    trv.column("6",width=80,anchor='c')

    trv.heading("1",text="fname")
    trv.heading("2",text="email")
    trv.heading("3",text="DOB")
    trv.heading("4",text="category")
    trv.heading("5",text="Aadharno")
    trv.heading("6",text="Contact")

    for dt in r_set:
        #print(dt),
        trv.insert("",'end',iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
    my_w.mainloop()


