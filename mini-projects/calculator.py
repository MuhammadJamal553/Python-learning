print("## Simple Calculator ##")
while True:
    print("Choose An Option.")
    print("1. Add.")
    print("2. Subtract.")
    print("3. Multiple.")
    print("4. Divide.")
    print("5. Exit.")
    choice = input("Enter Your Choice (1-5): ")
    if choice == "5":
        print("Exiting Calculator. Bye ")
        break
    try:
        num1 = float(input("Enter The First Value: "))
        num2 = float(input("Enter The Second Value: "))
        if choice == "1":
            print("Result:", num1 + num2)
            break
        elif choice == "2":
            print("Result: ", num1 - num2)
            break
        elif choice == "3":
            print("Result: ", num1 * num2)
            break
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot Divide By Zero.")
            print("Result: ", num1 / num2)
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter A Valid Number")