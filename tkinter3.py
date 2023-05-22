from tkinter import *
from tkinter import messagebox
import random
def p_img():
    sel = forb.get()
    if sel == 1:
        label1.config(image=img_f)
    else:
        label1.config(image=img_b)

def coin_chk():
    com = random.choice(["앞면", "뒷면"])
    user_sel = "앞면" if forb.get() == 1 else "뒷면"
    if com == user_sel:
        messagebox.showinfo("결과", "정답")
    else:
        messagebox.showinfo("결과", "오답")

window = Tk()
window.title("동전 던지기")
window.resizable(width=False, height=False)

img_f = PhotoImage(file="python/imgfile/fr.jpg")
img_b = PhotoImage(file="python/imgfile/ba.jpg")
label1 = Label(window, image=img_f)
label1.grid(row=0, column=0)

forb = IntVar()
r1 = Radiobutton(window, text="앞면", value=1, command=p_img)
r1.select()
r2 = Radiobutton(window, text="뒷면", value=2, command=p_img)
r1.grid(row=2, column=0)
r2.grid(row=3, column=0)

button1 = Button(window, text="시작", command=coin_chk)
button1.grid(row=4, column=0)

window.mainloop()