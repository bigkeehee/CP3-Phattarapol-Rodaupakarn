x = int(input("Enter Number:"))
for i in range(x):
    text = " " * (x - i - 1) + "*" * (2 * i + 1)
    print(text)