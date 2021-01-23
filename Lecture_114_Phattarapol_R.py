from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import messagebox

c = CurrencyRates()
result = 0

def Total_Currency(event):
    if textBox_First.get() == '' or textBox_Sec.get() == '' or textBox_Num.get() == '':
        messagebox.showerror('Error!', 'Enter Your Info')
    Result = float(textBox_Num.get()) * c.get_rate(textBox_First.get(), textBox_Sec.get())
    Total.configure(text=Result)

# Create GUI
MainWindow = Tk()
MainWindow.geometry('300x100')
MainWindow.title("Foreign Currency Converter")

# Label and TextBox
label_First = Label(MainWindow, text="สกุลเงินที่ต้องการเปรียบเทียบ :")
label_First.grid(row=0, column=0)
textBox_First = Entry(MainWindow)
textBox_First.grid(row=0, column=1)

label_Sec = Label(MainWindow, text="สกุลเงินที่ต้องการให้เปรียบเทียบ :")
label_Sec.grid(row=1, column=0)
textBox_Sec = Entry(MainWindow)
textBox_Sec.grid(row=1, column=1)

calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.grid(row=3, column=0)
calculateButton.bind('<Button-1>', Total_Currency)

Number = Label(MainWindow, text="จำนวนเงิน :")
Number.grid(row=2, column=0)
textBox_Num = Entry(MainWindow)
textBox_Num.grid(row=2, column=1)

Total = Label(MainWindow, text="ผลลัพธ์")
Total.grid(row=3, column=1)

MainWindow.mainloop()