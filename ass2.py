while 'true':
    print("press 1 if you want to perform addition")
    print("press 2 if you want to perform subtraction")
    print("press 3 if you want to perform multiplication")
    print("press 4 if you want to perform division")
    print("press 5 if you want to exit")
    choice=input()
if choice =='1':
    number1=int(input("please enter the number1:"))
    number2=int(input("please enter the number2:"))
    result=number1+number2
    print(f"\n the sum of {number1} and {number2} is {result}\n")
elif choice =='2':
    number1=int(input("please enter the number1:"))
    number2=int(input("please enter the number2:"))
    if number1>number2:
        result=number1-number2
    else:
        result=number2-number1
        print(f"\n the difference of{number1}and {number2} is {result}\n")
elif choice =='3':
    number1=int(input("please enter the number1:"))
    number2=int(input("please enter the number2:"))
    result=number1*number2
    print(f"\nthe multiplication of {number1} and {number2} is {result}\n")
elif choice =='4':
    number1=int(input("please enter the number1:"))
    number2=int(input("please enter the number2:"))
    result=number1/number2
    print(f"\n the division of {number1} and {number2} is{result}\n")
elif choice =='5':
    exit()
else:
    print("please enter a valid choice")
