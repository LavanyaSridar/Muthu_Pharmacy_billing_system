from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk, Image


def submit():
    Id=e_Id.get();
    P_Name=e_P_Name.get();
    contactno=e_contactno.get();
    Doctor_Name=e_Doctor_Name.get();
    Manufacturedby=e_Manufacturedby.get();
    Manufactureddate=e_Manufactureddate.get();
    Expirydate=e_Expirydate.get();
    Product=e_Product.get();
    Quantity=e_Quantity.get();
    Price=e_Price.get();
    
    if(Id=="" or P_Name=="" or contactno=="" or Doctor_Name=="" or Manufacturedby=="" or Manufactureddate=="" or Expirydate=="" or Product=="" or Quantity=="" or Price==""):
        MessageBox.showinfo("Insert status","all required")

    else:
        con=mysql.connect(host="localhost",user="root",passwd="admin",port="3306",database="Patient")
        cursor=con.cursor()
        cursor.execute("insert into history values('"+Id+"','"+P_Name+"','"+Doctor_Name+"','"+contactno+"','"+Manufacturedby+"','"+Manufactureddate+"','"+Expirydate+"','"+Product+"','"+Quantity+"','"+Price+"')")
        cursor.execute("commit")
        MessageBox.showinfo("insert status","inserted sucessfully")
        con.close()


root=Tk()

root.title("PHARMACY MANAGEMENT SYSTEM")

root.geometry("700x500")

frame = Frame(root, width=600, height=400)

frame.pack()

frame.place(anchor='center', relx=0.5, rely=0.5)

root.configure(background='black')

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("dn.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)

label.pack()

Id=Label(root,text='Id',font=('bold',15),bg="teal")
Id.place(x=50,y=50)

P_Name=Label(root,text="P_Name",font=('bold',15),bg="teal")
P_Name.place(x=50,y=100)

contactno=Label(root,text='contactno',font=('bold',15),bg="teal")
contactno.place(x=50,y=150)

Doctor_Name=Label(root,text='Doctor_Name',font=('bold',15),bg="teal")
Doctor_Name.place(x=50,y=200)

Manufacturedby =Label(root,text='Manufacturedby',font=('bold',15),bg="teal")
Manufacturedby.place(x=40,y=250)

Manufactureddate=Label(root,text='Manufactureddate',font=('bold',15),bg="teal")
Manufactureddate.place(x=40,y=300)

Expirydate=Label(root,text='Expirydate',font=('bold',15),bg="teal")
Expirydate.place(x=370,y=50)

Product=Label(root,text='Product',font=('bold',15),bg="teal",width='15')
Product.place(x=350,y=100)

Quantity=Label(root,text='Quantity',font=('bold',15),bg="teal",width='15')
Quantity.place(x=350,y=150)

Price=Label(root,text='Price',font=('bold',15),bg="teal",width='15')
Price.place(x=350,y=200)

e_Id=Entry()
e_Id.place(x=200,y=50)

e_P_Name=Entry()
e_P_Name.place(x=200,y=100)

e_Doctor_Name=Entry()
e_Doctor_Name.place(x=200,y=150)

e_contactno=Entry()
e_contactno.place(x=200,y=200)

e_Manufacturedby=Entry()
e_Manufacturedby.place(x=210,y=250)

e_Manufactureddate=Entry()
e_Manufactureddate.place(x=210,y=300)

e_Expirydate=Entry()
e_Expirydate.place(x=550,y=50)

e_Product=Entry()
e_Product.place(x=550,y=100)

e_Quantity=Entry()
e_Quantity.place(x=550,y=150)

e_Price=Entry()
e_Price.place(x=550,y=200)

submit=Button(root,text="submit",font=('italic'),bg="teal",command=submit)
submit.place(x=40,y=350)

get=Button(root,text="Get",font=('italic',20),bg="teal",command=get)
get.place(x=40,y=350)


root.mainloop()


