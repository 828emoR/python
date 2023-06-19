from tkinter import *

def click(num):
    if num == '=' :
        result = eval(number_entry.get())
        number_entry.insert(END,'=' + str(result))
    else :
        number_entry.insert(END, num)

button_n = ['1','2','3','/','4','5','6','*','7','8','9','-','00','0',':','+','C','=','<']
window =Tk()
window.title("계산기")
window.geometry("200x300")
window.resizable(width=FALSE, height=FALSE) 
number_entry = Entry(window, width=26)
number_entry.place(x=5,y=10)
x = 5
y = 40

for b in button_n :
    def process(t=b):
        click(t)

        Button(window,text=b, width=4, height=2, command=process).place(x=x, y=y)
        x=x+50
        if (x-5)%200 == 0 :
            y = y + 50
            x = 5


window.mainloop()