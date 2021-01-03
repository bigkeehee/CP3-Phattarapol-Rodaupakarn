def vat(total):
    result = total + (total * 7/100)
    return result

total = int(input("Enter Your Total: "))
print(vat(total))