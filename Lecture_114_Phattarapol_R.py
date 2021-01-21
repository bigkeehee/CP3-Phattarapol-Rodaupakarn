from tkinter import *
from forex_python.converter import CurrencyRates
c = CurrencyRates()
convert_result = 0


def Total_Currency(event):
    convert_result = c.get_rate(textBox_First.get(), textBox_Sec.get())
    Total.configure(text=convert_result)


MainWindow = Tk()
label_First = Label(MainWindow, text="สกุลเงินที่ต้องการเปรียบเทียบ :")
label_First.grid(row=0, column=0)
textBox_First = Entry(MainWindow)
textBox_First.grid(row=0, column=1)
label_Sec = Label(MainWindow, text="สกุลเงินที่ต้องการให้เปรียบเทียบ :")
label_Sec.grid(row=1, column=0)
textBox_Sec = Entry(MainWindow)
textBox_Sec.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.grid(row=2, column=0)
calculateButton.bind('<Button-1>', Total_Currency)
Total = Label(MainWindow, text="ผลลัพธ์")
Total.grid(row=2, column=1)
MainWindow.mainloop()