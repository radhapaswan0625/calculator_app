print("....Simple Calculator....")

num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

print("chosse operations:")
print("1. Adddition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")

choice=input("enter your choice(1/2/3/4):")

if choice=="1":
    result=num1+num2
    print("Result:",result)
elif choice=="2":
    result=num1-num2
    print("Result:",result)
elif choice=="3":
    result=num1*num2
    print("Result:",result)
elif choice=="4":
    if num2==0:
        print("Error:cannot divided by 0.")
    else:
        result=num1/num2
        print("Result:",result)
else:
    print("Invalid Choice:")
