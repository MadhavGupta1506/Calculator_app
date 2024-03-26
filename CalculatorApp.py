from tkinter import *
root=Tk()
# root.geometry("600x700")
root.title("Calculator App")

root.resizable(False,False)
entry=Entry(root, borderwidth=5, width=35)
entry.grid(row=0,column=0,columnspan=3,padx=20,pady=30)

def buttonClick(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))
def clearButton():
    entry.delete(0,END)

def add():
    firstNumber=entry.get()
    global f_n
    global math
    math="additon"
    f_n=int(firstNumber)
    entry.delete(0,END)


def divide():
    firstNumber=entry.get()
    global f_n
    global math
    math="division"
    f_n=int(firstNumber)
    entry.delete(0,END)
    
    
def multiply():
    firstNumber=entry.get()
    global f_n
    global math
    math="multiplication"
    f_n=int(firstNumber)
    entry.delete(0,END)
    
def sub():
    firstNumber=entry.get()
    global f_n
    global math
    math="subtraction"
    f_n=int(firstNumber)
    entry.delete(0,END)

def equal():
    s_number=entry.get()
    entry.delete(0,END)
    s_n=int(s_number)
    if(math=="addtion"):
        entry.insert(0,f_n+s_n)    
    elif(math=="multiplication"):
        entry.insert(0,f_n*s_n)    
    elif(math=="subtraction"):
        entry.insert(0,f_n-s_n)    
    elif(math=="division"):
        entry.insert(0,f_n/s_n)    
    
    
#Creating Buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonClick(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonClick(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonClick(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonClick(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonClick(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonClick(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonClick(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonClick(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonClick(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonClick(0))


#Buttons of operation
button_sub=Button(root,text="-",padx=41,pady=20,command=sub)
button_add=Button(root,text="+",padx=39,pady=20,command=add)
button_multiply=Button(root,text="x",padx=41,pady=20,command=multiply)
button_divide=Button(root,text="/",padx=41,pady=20,command=divide)


button_clear=Button(root,text="Clear",padx=85,pady=20,command=clearButton)
button_equal=Button(root,text="=",padx=95,pady=20,command=equal)



#Adding Button to Screen
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=5,column=1,columnspan=2)


button_add.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)



root.mainloop()
