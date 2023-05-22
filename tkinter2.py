from tkinter import *
from tkinter import messagebox
import random
def coin_chk():
    com = random.randrange(1, 3)
    if com == coin_var.get():
        messagebox.showinfo("결과", "정답")
    else:
        messagebox.showinfo("결과", "오답")

    label1.config(text=str(coin_var.get()))

window = Tk()

window.title("Coin Toss")
window.geometry("300x120")
window.resizable(width=False, height=False)

coin_var = IntVar()  # 라디오 버튼 값을 정수형으로 저장하는 coin_var 변수 생성
coin_f = Radiobutton(window, text="앞면", value=1, variable=coin_var)
coin_f.place(x=10, y=10)
coin_b = Radiobutton(window, text="뒷면", value=2, variable=coin_var)
coin_b.place(x=10, y=30)

button1 = Button(window, text="시작", command=coin_chk)
button1.place(x=10, y=55)

label1 = Label(window, width=20, text="", borderwidth=3, relief="raised")
label1.place(x=150, y=20)

window.mainloop()