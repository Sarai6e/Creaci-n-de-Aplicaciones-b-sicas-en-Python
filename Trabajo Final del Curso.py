#Desarrollo de un  sistema de registro de pedidos por teléfono en python:

from tkinter import Tk, Label, Button, Entry

def calcularST1():

    v1 = txt7.get()
    v2 = txt8.get()
    v3 = txt11.get()
    v4 = txt12.get()
    v5 = txt15.get()
    v6 = txt16.get()
    ST = float(v1)*float(v2)
    txt9.delete(0,"end")
    txt9.insert(0,ST)
    ST2 = float(v3)*float(v4)
    text13.delate(0,"end")
    text13.insert(0,ST2)
    ST3 = float (v5)*float(v6)
    txt17.delete(0,"end")
    txt17.insert(0,ST3)
    T = ST + ST2 + ST3
    txt18.delete(0,"end")
    txt18.insert(0,T)

ventana = Tk()
ventana.geometry("600x450")
ventana.configure(bg="lead")

lab0 = Label(ventana,text='Ferretería El Tornillo Feliz', font=("Times New Arial",16), fg= "black", bg="lead")
lab0.place(x=170,y=10)

lab1 = Label(ventana, text='DNI: 'font=("Times New Arial",10), fg="black", bg="lead")
lab1.place(x=40,y=50, height=25)
txt1 = Entry(ventana)
txt1.place(x=100, y=50, width=70, height=25)

lab2 = Label(ventana, text='APELLIDOS: ', font=("Times New Arial",10), fg="black" , bg="lead")
lab2.place(x=20, y=90)
txt2 = Entry(ventana)
txt2.place(x=100,y=90, width=130, height=25)

lab = Label(ventana, text='NOMBRES: ' ,font=("Times New Arial",10), fg="black" ,bg="lead")
lab3.place(x=300,y=90)
txt3 = Entry(ventana)
txt3.place(x=370,y=90, width=130, height=25)
    
