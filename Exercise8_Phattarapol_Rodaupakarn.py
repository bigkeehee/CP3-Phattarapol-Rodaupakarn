username = input("User :")
password = input("Password :")

priceA = 12
priceM = 15
priceO = 20

if username == "customer" and password == "1234":
    print("Welcome customer")
    print("-"*16,"Fruit","-"*16)
    print("1.Apple  : 12 BAHT")
    print("2.Mango  : 15 BAHT")
    print("3.Orange : 20 BAHT")
    Select = input("What kind do you want :")
    Number = int(input("How much do yo want :"))
    if Select == "1":
        print("Apple x", Number, "=" , Number * priceA, "BAHT")
    elif Select == "2":
        print("Mango x", Number, "=", Number * priceM, "BAHT")
    elif Select == "3":
        print("Orange x", Number, "=", Number * priceO, "BAHT")
    print("-"*16, "Thank You", "-"*16)

else:
    print("Login Error")