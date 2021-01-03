def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
            print("Done!")
            return showMenu(True)
    else:
        print("Try Again")
        login()

def showMenu(Name):
    if Name:
        print("----- iShop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")
        Select = int(input("Choose Your Menu: "))
        return menuSelect(Select)

def menuSelect(UserSelected):
    if UserSelected == 1:
        Total = int(input("Enter Your Price:"))
        return vatCalculator(Total)
    elif UserSelected == 2:
        return priceCalculator()

def vatCalculator(Price):
    vat = 7
    result = Price + (Price * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

print(login())

