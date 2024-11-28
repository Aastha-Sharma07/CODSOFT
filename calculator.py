def calculator():
    num_1 = float(input("Enter first number:"))
    num_2 = float(input("Enter second number:"))

    print("Select your operation that you have to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        operation = int(input("Enter your operation number:"))
        if operation == 1:
            print("Your answer is =",num_1+num_2)
        elif operation == 2:
            print(f"Your answer is=",num_1-num_2)
        elif operation == 3:
            print(f"Your answer is=",num_1*num_2)
        elif operation == 4:
            if num_2 != 0:
                print(f"Your answer is=",num_1 /num_2)
            else:
                print("Error,Second number cannot be equals to 0 for division")
        elif operation==5:
            print("Thank You...")
            break
        else:
            print("Invalid Operation \nPlease enter given operation number")
calculator()
