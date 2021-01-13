Allmenu = {"ข้าวมันไก่": "30", "ข้าวขาหมู": "50", "ข้าวมันไก่ทอด": "35"}
menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0] + ":" +menuList[number][1])

def total():
    price = 0
    for i in range(len(menuList)):
        price += int(menuList[i][1])
    print("Total =", price)

while True:
    menuName = input("Plese Enter Menu :")
    if (menuName.lower() == "exit"):
        break

    else:
        menuList.append([menuName, Allmenu[menuName]])

showBill()
total()