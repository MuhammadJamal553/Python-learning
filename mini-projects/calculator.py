# ===== Simple Calculator =====
# A simple calculator that can perform basic arithmetic operations
# like addition, subtraction, multiplication, and division.
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 

print("## Simple Calculator ##")
# A loop to keep the calculator running until the user decides to exit.
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
while True:
    print("Choose An Option.")
    print("1. Add.")
    print("2. Subtract.")
    print("3. Multiple.")
    print("4. Divide.")
    print("5. Exit.")
    # Option Selection.
    choice = input("Enter Your Choice (1-5): ")
    # Exits If Don't Want to use
    if choice == "5":
        print("Exiting Calculator. Bye ")
        break
    # Try Block To Catch Errors
    try:
        num1 = float(input("Enter The First Value: "))
        num2 = float(input("Enter The Second Value: "))
        # Options Execution
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
        # If Choice Is Invalid
        else:
            print("Invalid Choice Please Try Again")
    # If Input Is Not A Valid Number
    except ValueError:
        print("Enter A Valid Number")