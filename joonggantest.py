from tkinter import*

def clacwon():
    print(Won_entry.get())
    res.config(text=f"{round(float(Won_entry.get()) *0.00098,3)} 달러")

def clacdol():
    print(Dol_entry.get())
    res.config(text=f"{round(float(Dol_entry.get()) * 1276,2)} 원")

window = Tk()
window. title("환율계산기")
window.geometry("300x200")

window.resizable(width=False, height=False)



Wonlabel = Label(window, text="원")
Wonlabel.grid(row = 0, column=1)

Won_entry = Entry(window, width = 26)
Won_entry.grid(row = 0, column=2)

DolLabel = Label(window, text="달러")
DolLabel.grid(row=1, column=1)

Dol_entry = Entry(window, width = 26)
Dol_entry.grid(row=1, column=2)

Nowchan = Label(window, text="현재 환율 원: 1,276 - 달러: 1")
Nowchan.grid(row=2, column=2)

Wonclacbutt = Button(window, text="원-달러 변환", command=clacwon)
Wonclacbutt.grid(row=0, column=3)
Dolclacbutt = Button(window, text="달러-원 변환", command=clacdol)
Dolclacbutt.grid(row=1,column=3)

res = Label(window, text="결과")
res.grid(row=4, column=2)
window.mainloop()
