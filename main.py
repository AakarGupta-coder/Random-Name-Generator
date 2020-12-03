from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import names

root  = tk.Tk()
root.geometry('397x308+550+250')
root.title("Name Generator")
root.resizable(0,0)

def search():

        Gender = gender.get()
        Type = types.get()
        text.config(text="")
        if Gender == 'Male' and Type == "Full Name":
                name = names.get_full_name(gender="male")
                text.config(text=name)
        elif Gender == 'Male' and Type == "First Name":
                name = names.get_first_name()
                text.config(text=name)
        elif Gender == 'Male' and Type == "Last Name":
                name = names.get_last_name()
                text.config(text=name)
        
        elif Gender == 'Female' and Type == "Full Name":
                name = names.get_full_name(gender="female")
                text.config(text=name)
        elif Gender == 'Female' and Type == "First Name":
                name = names.get_first_name()
                text.config(text=name)
        elif Gender == 'Female' and Type == "Last Name":
                name = names.get_last_name()
                text.config(text=name)

l =  Label(root, text="Name Generator",font=('verdana',30,'bold'),bg="black",fg="white")
l.place(x=10,y=10)

l1 = Label(root,text="Gender: ",font=('verdana',23,'bold'))
l1.place(x=10,y=80)
g = tk.StringVar() 
gender = Combobox(root, width = 10, textvariable = g, state='readonly',font=('verdana',20,'bold'),justify=CENTER) 
gender['values'] = ('Male','Female')
gender.place(x=175,y=85)
gender.current(0)

l2 = Label(root,text="Type: ",font=('verdana',23,'bold'))
l2.place(x=10,y=130)
t = tk.StringVar() 
types = Combobox(root, width = 10, textvariable = t, state='readonly',font=('verdana',20,'bold'),justify=CENTER) 
types['values'] = ('Full Name','First Name','Last Name')
types.place(x=175,y=135)
types.current(0) 

text = Label(root,width=18,height=1,padx=8,borderwidth=1,background="aqua",justify=CENTER)
text['font'] = ("verdana",22,'bold')
text.place(x=10,y=185)

button = Button(root,width=19,text="GENERATE",font=('verdana','20','bold'),command=search,padx=3,borderwidth=4)
button.place(x=10,y=235)
root.mainloop()
