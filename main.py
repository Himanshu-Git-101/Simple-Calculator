while True:
    Equation = input("Enter expression (or 'exit' to quit): ")

    if    Equation.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = eval   ( Equation)
        print("Result:", result)
    except:
        print("Invalid expression. Please try again.")                             
