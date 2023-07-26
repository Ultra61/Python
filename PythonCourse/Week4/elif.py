age = 0
age = input("input your age: ")
if int(age) < 4:
    print("your admission is $0")
elif int(age) < 18:
    print("your admission is $25")
else:
    print("your admission in $50")
