first = input("1st: ")
operator = input("operator: ")
second = input("2nd: ")

first = int(first)
second = int(second)

match operator:
    case "+":
        print(first + second)
    case "-":
        print(first - second)
    case "*":
        print(first * second)
    case "/":
        if second != 0:
            print(first / second)
        else:
            print("Error: Division by zero!")
    case "%":
        print(first % second)
    case _:
        print("Invalid operator")
