from tkinter import *

def order_chk():
    print(drink_sel.get())
def order_chk2():
    print(cup_sel.get())
window = Tk()


label_sel=Label(window, text="과일주스 종류를 선택하세요")
drink_sel=StringVar()
drink_sel1= Radiobutton(window, text="딸기", variable=drink_sel, value="딸기")
drink_sel1.select()
drink_sel2=Radiobutton(window, text="포도", variable=drink_sel, value="포도")
drink_sel3=Radiobutton(window, text="바나나", variable=drink_sel, value="바나나")

label_sel.pack()
drink_sel1.pack()
drink_sel2.pack()
drink_sel3.pack()



label_sel=Label(window, text="몇 잔을 선택하시겠습니까?")
cup_sel=StringVar()
cup_sel1= Radiobutton(window, text="1잔", variable=cup_sel, value="1잔")
cup_sel1.select()
cup_sel2= Radiobutton(window, text="2잔", variable=cup_sel, value="2잔")
cup_sel3= Radiobutton(window, text="3잔", variable=cup_sel, value="3잔")
label_sel.pack()
cup_sel1.pack()
cup_sel2.pack()
cup_sel3.pack()

button1 = Button(window, text="주문", command=order_chk)
button1.pack()

Label.config(text=f"{drink_sel}, {cup_sel}")


window.mainloop()


