from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk



win=Tk()
win.geometry("900x700")
win.title("Expense Analysis Tool ")



def register():
    def click_register():
        id=entry_id.get()
        name=entry_name.get()
        email=entry_email.get()
        psw=entry_password.get()
        contact=entry_contact.get()

        if (id=="" or psw=="" or name=="" or email=="" or contact==""):
            MessageBox.showinfo("Alert","Enter all Credentials")
        else:
            con=mysql.connect(host="localhost",user="root",password="Yash@123",database="proj",auth_plugin='mysql_native_password')
            cursor=con.cursor()
            cursor.execute("insert into new_table values('"+id+"','"+name+"','"+email+"','"+contact+"','"+psw+"')")
            cursor.execute("commit")

            MessageBox.showinfo("Alert","Registration completed Successfully")
            con.close()
    

    f1=Frame(bg="#0096DC")
    f1.place(x=0,y=0,height=500,width=500)

    l1=Label(f1,text="User Id:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l2=Label(f1,text="Name:",font=("Verdena 15"),fg="white",bg="#0096DC")
    l3=Label(f1,text="Email",font=("Verdena 15"),fg="white",bg="#0096DC")
    l4=Label(f1,text="Contact",font=("Verdena 15"),fg="white",bg="#0096DC")
    l5=Label(f1,text="Password:",font=("Verdena 15"),fg="white",bg="#0096DC")

    l1.place(x=100,y=100)
    l2.place(x=100,y=150)
    l3.place(x=100,y=200)
    l4.place(x=100,y=250)
    l5.place(x=100,y=300)

    entry_id=Entry(f1,font=("Verdena 15"))
    entry_name=Entry(f1,font=("Verdena 15"))
    entry_email=Entry(f1,font=("Verdena 15"))
    entry_contact=Entry(f1,font=("Verdena 15"))
    entry_password=Entry(f1,show="*",font=("Verdena 15"))
    
    entry_id.place(x=200,y=100)
    entry_name.place(x=200,y=150)
    entry_email.place(x=200,y=200)
    entry_password.place(x=200,y=300)
    entry_contact.place(x=200,y=250)

    b1=Button(f1,text="Register",font=("Verdena 15"),fg="white",bg="grey",command=click_register)
    b2=Button(f1,text="LogIn",font=("Verdena 15"),fg="white",bg="grey",command=login)
    b1.place(x=150,y=400)
    b2.place(x=250,y=400)
    
    
    
