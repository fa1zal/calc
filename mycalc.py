from tkinter import *
 
def btnClick(numbers):
   global operator
   operator=operator+str(numbers)
   text_input.set(operator)
 
def btnClearDisplay():
   global operator
   operator=""
   text_input.set("")
 
def btnEqualsInput():
   global operator
   sumof=str(eval(operator))
   text_input.set(sumof)
   operator=""
 
 
cal = Tk()
cal.title("my calculator")
operator=""
text_input=StringVar()
 
txtdisplay=Entry(cal,font=('SF Mono',10),textvariable=text_input,bd=4,fg='red',
                insertwidth=2).grid(columnspan=7)
 
btnClear=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="C",command=btnClearDisplay).grid(row=1,column=0)
 
btnSquareRoot=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="√",command=lambda:btnClick("**0.5")).grid(row=1,column=1)
 
btnPercentage=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="%",command=lambda:btnClick("/100*")).grid(row=1,column=2)
 
btnDivision=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="/",command=lambda:btnClick("/")).grid(row=1,column=3)
 
btn7=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="7",command=lambda:btnClick(7)).grid(row=2,column=0)
 
btn8=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="8",command=lambda:btnClick(8)).grid(row=2,column=1)
 
btn9=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="9",command=lambda:btnClick(9)).grid(row=2,column=2)
 
btnMultiplication=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="*",command=lambda:btnClick("*")).grid(row=2,column=3)
 
btn4=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="4",command=lambda:btnClick(4)).grid(row=3,column=0)
 
btn5=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="5",command=lambda:btnClick(5)).grid(row=3,column=1)
 
btn6=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="6",command=lambda:btnClick(6)).grid(row=3,column=2)
 
btnSubtraction=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="-",command=lambda:btnClick("-")).grid(row=3,column=3)
 
btn1=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="1",command=lambda:btnClick(1)).grid(row=4,column=0)
 
btn2=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="2",command=lambda:btnClick(2)).grid(row=4,column=1)
 
btn3=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
           text="3",command=lambda:btnClick(3)).grid(row=4,column=2)
 
btnAddition=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="+",command=lambda:btnClick("+")).grid(row=4,column=3)

btnDot=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text=".",command=lambda:btnClick(".")).grid(row=5,column=0)
 
btn0=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10,'bold'),
           text="0",command=lambda:btnClick(0)).grid(row=5,column=1)
 
btnZeroZero=Button(cal,padx=18,bd=4,fg="black",font=('SF Mono',10),
               text="00",command=lambda:btnClick("00")).grid(row=5,column=2)
 
btnEquals=Button(cal,padx=18, bd=4,fg="black",font=('SF Mono',10),
               text="=",command=btnEqualsInput).grid(row=5,column=3)
 
cal.mainloop()
