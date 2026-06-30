while True:
    print("---welcome to my calculator-----")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")
    choice=input("enter your choice:")
    if choice=="5":
        print("exiting calculator")
        break
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    if choice == '1':
        print("Result:", num1 + num2)

    elif choice == '2':
        print("Result:", num1 - num2)

    elif choice == '3':
        print("Result:", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero.")

    else:
        print("Invalid choice! Try again.")



    

