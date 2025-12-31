# Basic calculator
print("NEW BASIC CALCULATOR")

def menu():
    print("\nMenu")
    print("1. Addition : +")
    print("2. Subtraction : -")
    print("3. Multiplication : *")
    print("4. Division : /")
    print("5. Power : **")
    print("6. Modulus : %  [To get remainder]")
    print("7. Exit")

# input function
def input_fun():
     while True:
        try:
            a = float(input("Enter first digit : "))
            b = float(input("Enter second digit : "))
            return a, b
        except ValueError:
            print(" Invalid input! Please enter only numbers.")

# operation functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b


while True:
    menu()
    choice = input("Enter your choice : ")

    if choice == "7":
        print("Calculator closed. Thank you!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        x, y = input_fun()

        if choice == "1":
            print("Result:", add(x, y))

        elif choice == "2":
            print("Result:", sub(x, y))

        elif choice == "3":
            print("Result:", mul(x, y))

        elif choice == "4":
            print("Result:", div(x, y))

        elif choice == "5":
            print("Result:", power(x, y))

        elif choice == "6":
            print("Result:", modulus(x, y))

    else:
        print("Invalid choice! Please select again.")
