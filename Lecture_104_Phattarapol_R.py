class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()
customer2.name = "BBJ"
customer2.lastName = "747"
customer2.age = 56
customer2.addCart()

customer3 = Customer()
customer3.name = "ASTON"
customer3.lastName = "MARTIN"
customer3.age = 106
customer3.addCart()

customer4 = Customer()
customer4.name = "BUGATTI"
customer4.lastName = "CHIRON SPORT"
customer4.age = 490
customer4.addCart()