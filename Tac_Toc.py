from tkinter import*
import tkinter.messagebox
tik=Tk()
tik.title("TIK TAC TOE")
click=True
def checker(buttons):
	global click
	if buttons["text"]==" " and click==True:
		buttons["text"]="X"
		click=False
	elif buttons["text"]==" " and click==False:
		buttons["text"]="O"
		click=True
	elif(button1["text"]=="X" and button2["text"]=="x" and button3["text"]=="X" or
		button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
		button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
		button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
		button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
		button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
		button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
		button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" ):
		tkinter.messagebox.showinfo("WINNER X","YOU HAVE JUST WON THE GAME")


	elif(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
		button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
		button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
		button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
		button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
		button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
		button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
		button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" ):
		tkinter.messagebox.showinfo("WINNER O","YOU HAVE JUST WON THE GAME")
	else:
		tkinter.messagebox.showinfo("NO ONE CAN WIN THIS MATCH","MATCH TRIDE")
buttons=StringVar()
button1=Button(tik,text=" ",font=('Times 26 bold'),bg="yellow",height=4,width=8,command=lambda:checker(button1))
button1.grid(row=1,column=0)

button2=Button(tik,font=('Times 26 bold'),text=" ",bg="blue",height=4,width=8,command=lambda:checker(button2))
button2.grid(row=1,column=1)

button3=Button(tik,font=('Times 26 bold'),text=" ",bg="green",height=4,width=8,command=lambda:checker(button3))
button3.grid(row=1,column=2)

button4=Button(tik,text=" ",font=('Times 26 bold'),bg="green",height=4,width=8,command=lambda:checker(button4))
button4.grid(row=2,column=0)

button5=Button(tik,font=('Times 26 bold'),text=" ",bg="pink",height=4,width=8,command=lambda:checker(button5))
button5.grid(row=2,column=1)

button6=Button(tik,font=('Times 26 bold'),text=" ",bg="yellow",height=4,width=8,command=lambda:checker(button6))
button6.grid(row=2,column=2)

button7=Button(tik,font=('Times 26 bold'),text=" ",bg="yellow",height=4,width=8,command=lambda:checker(button7))
button7.grid(row=3,column=0)

button8=Button(tik,font=('Times 26 bold'),text=" ",bg="blue",height=4,width=8,command=lambda:checker(button8))
button8.grid(row=3,column=1)

button9=Button(tik,font=('Times 26 bold'),text=" ",bg="green",height=4,width=8,command=lambda:checker(button9))
button9.grid(row=3,column=2)
tik.mainloop()