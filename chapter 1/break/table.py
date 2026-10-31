n = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 6:
        break
    print(n, "x", i, "=", n * i)