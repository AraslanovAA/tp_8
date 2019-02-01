import xmlrpc.client
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import xmlrpc.client
from tkinter import *

client = xmlrpc.client.ServerProxy("http://localhost:8000/")
print("Клиент подключен к серверу")
print("Ожидание ввода от клиента")
ListParams = [u"Круг", u"Прямоугольник", u"Квадрат"]
global UsingParam
UsingParam= ListParams[0]

def ShowResult(stroka, result, corx=0, cory=0,NumberOfEdit = 1) :
    if NumberOfEdit ==1 :
        message_entry.place(x=7, y=78, height=60, width=592)
        message_entry2.place(x=7, y=78, height=27, width=592)
        message_entry2.lower((message_entry))
        button1.place(x=7, y=142, height=28, width=90)
        Label4["text"] = stroka + result
        Label4.place(x = corx, y = cory)
    if NumberOfEdit ==2 :
        Label2.place(y= 47)
        Label2.lower(combobox)
        message_entry.place(x=7, y=73, height= 20, width=592)
        Label3.place(x=-105, y=90, height=30, width=600)
        message_entry2.place(x=7, y=120, height=20, width=592)
        button1.place(x=7, y=142, height=28, width=90)
        Label3.lower(message_entry)
        Label3.lower(message_entry2)
        Label4["text"] = stroka + result
        Label4.place(x=corx, y=cory)

def calculate(): # основной метод, отправляет введённые параметры на сервер и возвращает результат
    try:

        if combobox.get() == ListParams[0] :
            resstr = client.evaluate(combobox.get(),message_entry.get())
            if resstr == "ErrType" :
                messagebox.showinfo("Ошибка", "Неверный формат строки")
            else :
                if resstr == "ErrZero" :
                    ShowResult("Значение отрицательно", "", -220, 170, 1)
                else :
                    ShowResult("Площадь круга равна: ", str(resstr), -160, 170, 1)

        if combobox.get() == ListParams[1] :
            resstr = client.evaluate(combobox.get(),message_entry.get(), message_entry2.get())
            if resstr == "ErrType" :
                messagebox.showinfo("Ошибка", "Неверный формат строки")
            else :
                if resstr == "ErrZero" :
                    ShowResult("Значение отрицательно", "", -220, 170, 2)
                else :
                    ShowResult("Площадь прямоугольника: ", str(resstr), -200, 170, 2)
        if combobox.get() == ListParams[2]:
            resstr = client.evaluate(combobox.get(), message_entry.get())
            if resstr == "ErrType" :
                messagebox.showinfo("Ошибка", "Неверный формат строки")
            else :
                if resstr == "ErrZero" :
                    ShowResult("Значение отрицательно", "", -220, 170, 1)
                else :
                    ShowResult("Площадь квадрата равна: ", str(resstr), -200, 170, 1)
    except xmlrpc.client.Fault as err: #обработка ошибок соединения
        print(err.faultCode)
        if err.faultCode == 1:
            raise ZeroDivisionError
    except ConnectionRefusedError:
        messagebox.showinfo("Error", "Connection error, try again later")
    except ValueError:
        raise ValueError


def Get_Selected(param):
    UsingParam = combobox.get()
    if UsingParam == ListParams[0]:
        Label2["text"] = "Введите радиус круга: "
        Label2.place(x=-193,y =53)
        message_entry.place(x=7, y=78, height=75, width=592)
        button1.place(x=7, y=157, height=28, width=90)
    if UsingParam == ListParams[1] :
        Label2["text"] = "Введите длину 1 стороны прямоугольника:"
        Label2.place(x=-105, y=53)
        message_entry.place(x=7, y=78, height=28, width=592)
        button1.place(x=7, y=157, height=28, width=90)
    if UsingParam == ListParams[2] :
        Label2.place(x=-145, y =53)
        Label2["text"] = "Введите длину стороны квадрата:"
        message_entry.place(x=7, y=78, height=75, width=592)
        button1.place(x=7, y=157, height=28, width=90)
    Label4["text"]=""
    Label4.lower(button1)
    message_entry2.place(x=7, y=128, height=27, width=592)
    message_entry2.lower((message_entry))
    Label3.place(x=-105, y=98, height=30, width=600)
    Label3.lower(message_entry)

#---------------------------------------------------------------------
root = tk.Tk()
root.title("GUI на Python")
root.geometry("600x185")

Label1 = Label(justify = LEFT,text ="Выберите фигуру :",font = "Arial 14")#,justify = LEFT не меняет положение текста, с анкором текст уползает вообще неведо куда
Label1.place(x=-210,y=-5, height=30, width=600)

frame = tk.Frame(root)
frame.grid()
combobox = ttk.Combobox(root,values = ListParams,font = "Arial 14",height=3, background='#0000FF',state='readonly')
combobox.set(u"Круг")
combobox.place(x=7,y=20, height =32, width =593)
combobox.bind('<<ComboboxSelected>>', Get_Selected)

Label2 = Label(text ="Введите радиус круга: ",font = "Arial 14")
Label2.place(x=-193,y=53, height=30, width=600)

message_entry = Entry(font = "Arial 14")
message_entry.place(x=7,y=78, height =75, width = 592)

Label3 = Label(text ="Введите длину 2 стороны прямоугольника:",font = "Arial 14")
Label3.place(x=-105,y=98, height=30, width=600)
Label3.lower(message_entry)

message_entry2 = Entry(font = "Arial 14")
message_entry2.place(x=7,y=128, height =27, width = 592)
message_entry2.lower((message_entry))

button1=Button(root,text='посчитать',font='arial 10',command = calculate)
button1.place(x=7,y=157, height = 28, width = 90)


Label4 = Label(text ="",font = "Arial 10")
Label4.place(x=-220,y=170, height=15, width=600)
Label4.lower(button1)

root.mainloop()
