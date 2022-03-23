from tkinter import*
cal=Tk()
cal.title('calculator')
text_input=''
text_input=StringVar()
operator=''

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

txtDisplay=Entry(cal,bd=15,relief=GROOVE,bg='light green',justify='right',textvariable=text_input).grid(columnspan=15)

btn7=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='7',command=lambda: btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='8',command=lambda: btnClick(8))
btn8.grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='9',command=lambda: btnClick(9))
btn9.grid(row=1,column=2)

btn4=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='4',command=lambda: btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='5',command=lambda: btnClick(5))
btn5.grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='6',command=lambda: btnClick(6))
btn6.grid(row=2,column=2)

btn3=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='3',command=lambda: btnClick(3))
btn3.grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='2',command=lambda: btnClick(2))
btn2.grid(row=3,column=1)

btn1=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='1',command=lambda: btnClick(1))
btn1.grid(row=3,column=2)

btnC=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='C',command=lambda: btnClick("C"))
btnC.grid(row=4,column=0)

btn1=Button(cal,padx=16,bd=5,fg='red',font=('calibri','15','bold'),text='1',command=lambda: btnClick(1))
btn1.grid(row=4,column=1)

btnDEL=Button(cal,padx=5,bd=5,fg='red',font=('calibri','15','bold'),text='DEL',command=lambda: btnClick("DEL"))
btnDEL.grid(row=4,column=2)


cal.mainloop()
