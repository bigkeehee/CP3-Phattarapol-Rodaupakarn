from tkinter import *
import math
Fat = []
def BMItotal(event):
    x = int((float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100, 2)))
    if x >= 30:
        x = "อ้วนมาก"
    elif x > 24.9 and x <= 29.9:
        x = "อ้วน"
    elif x > 22.9 and x <= 24.9:
        x = "น้ำหนักเกิน"
    elif x > 18.5 and x <= 22.9:
        x = "น้ำหนักปกติ"
    elif x <= 18.5:
        x = "ผอมเกินไป"

    Total.configure(text = x)

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.grid(row=2, column = 0)
calculateButton.bind('<Button-1>', BMItotal)
Total = Label(MainWindow, text = "ผลลัพธ์")
Total.grid(row = 2, column = 1)

MainWindow.mainloop()


