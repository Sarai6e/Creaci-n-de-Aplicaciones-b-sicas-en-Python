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
ventana.title("FACTURA ELECTRONICA")
ventana.configure(bg="lead")

lab0 = Label(ventana,text='Ferreteria El Tornillo Feliz', font=("Times New Arial",15), fg= "black", bg="lead")
lab0.place(x=170,y=10)

lab1 = Label(ventana, text='DNI: ',font=("Times New Arial",10), fg="black", bg="lead")
lab1.place(x=40,y=50, height=25)
txt1 = Entry(ventana)
txt1.place(x=100, y=50, width=70, height=25)

lab2 = Label(ventana, text='APELLIDOS: ', font=("Times New Arial",10), fg="black" , bg="lead")
lab2.place(x=20, y=90)
txt2 = Entry(ventana)
txt2.place(x=100,y=90, width=130, height=25)

lab3 = Label(ventana, text='NOMBRES: ' ,font=("Times New Arial",10), fg="black" ,bg="lead")
lab3.place(x=300,y=90)
txt3 = Entry(ventana)
txt3.place(x=370,y=90, width=130, height=25)

lab4 = Label(ventana, text='DIRECCION: ', font=("Times New Arial",10), fg="black", bg="lead")
lab4.place(x=20, y=130)
txt4 = Entry(ventana)
txt4.place(x=100, y=130, width=350, height=25)

lab5 = Label(ventana, text='TELELEFONO: ', font=("Times New Arial",10), fg="black", bg="lead")
lab5.place(x=20, y=170)
txt5 = Entry(ventana)
txt5.place(x=100, y=170, width=350, height=25)

lab6 = Label(ventana, text='Codigo de producto', font=("Times New Arial",11), fg="black", bg="lead")
lab6.place(x=20, y=210)

lab7 = Label(ventana, text='Descripcion', font=("Times New Arial",11), fg="black", bg="lead")
lab7.place(x=160, y=210)

lab8 = Label(ventana, text='Unidad', font=("Times New Arial",11), fg="black", bg="lead")
lab8.place(x=260, y=210)

lab9 = Label(ventana, text='Cantidad', font=("Times New Arial",11), fg="black", bg="lead")
lab9.place(x=340, y=210)

lab10= Label(ventana, text='Precio', font=("Times New Arial",11), fg="black", bg="lead")
lab10.place(x=430, y=210)

lab11 = Label(ventana, text='Subtotal', font=("Times New Arial",11), fg="black", bg="lead")
lab11.place(x=500, y=210)

txt6 = Entry(ventana)
txt6.place(x=40,y=250,width=70, height=25)
txt7 = Entry(ventana)
txt7.place(x=349,y=250,width=40, height=25)
txt8 = Entry(ventana)
txt8.place(x=423,y=250,width=60, height=25)
txt9 = Entry(ventana)
txt9.place(x=498,y=250,width=65, height=25)
txt10 = Entry(ventana)

txt10.place(x=40,y=280,width=70, height=25)
txt11 = Entry(ventana)
txt11.place(x=349,y=280,width=40, height=25)
txt12 = Entry(ventana)
txt12.place(x=423,y=280,width=60, height=25)
txt13 = Entry(ventana)
txt13.place(x=498,y=280,width=65, height=25)

txt14 = Entry(ventana)
txt14.place(x=40,y=310,width=70, height=25)
txt15 = Entry(ventana)
txt15.place(x=349,y=310,width=40, height=25)
txt16 = Entry(ventana)
txt16.place(x=423,y=310,width=60, height=25)
txt17 = Entry(ventana)
txt17.place(x=498,y=310,width=65, height=25)

btn = Button(ventana,text='Calcular Total', font=("Times New Arial" ,11),commad = calcularST1, bg="black", fg="white")
btn.place(x=190, y=350)

lab12 = Label(ventana,text='Total: ', font=("Times New Arial",11),fg="black",bg="white")
lab12.place(x=428, y=350)
txt18 = Entry(ventana)
txt18.place(x=498, y=350, width=65, height=25)




    
