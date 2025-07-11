while True:
 print("Welcome to Simple Ccalcualtor")
 print("1. Addition")
 print("2. Subtraction")
 print("3. Division")
 print("4. Multplication")
 print("5. Power")
 print("6. Exit")
 
 user_input = int(input("Choose the Operation: "))
 

 a = float(input("Enter The First Number: "))
 b = float(input("Enter The Second Number: "))

 if user_input == 6:
    print("Goodluck with your assignment")
    break

 elif user_input == 1:
    result = a+b
    print("The result is: ", result)

 elif user_input == 2:
    result = a-b
    print("The result is: ", result)

 elif user_input == 3:
    result = a/b
    print("The result is: ", result)

 elif user_input == 4:
    result = a*b
    print("The result is: ", result)

 elif user_input == 5:
    result = a**b
    print("The result is: ", result)

 else:
    print("Invalid choice.")
