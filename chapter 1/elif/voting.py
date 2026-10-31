age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for voting")
elif age >= 0:
    print("Not eligible for voting")
else:
    print("Invalid age")