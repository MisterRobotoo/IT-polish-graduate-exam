def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pow(a, b - 1)

print("1 = addition 2 = reduction 3 = multiply 4 = division 5 = power")

opr = int(input("choose an operation: "))

match opr:
    case 1:
        n1 = float(input("first number: "))
        n2 = float(input("secound number: "))
        sol = n1 + n2
        print(sol)
    case 2:
        n1 = float(input("first number: "))
        n2 = float(input("secound number: "))
        sol = n1 - n2
        print(sol)
    case 3:
        n1 = float(input("first number: "))
        n2 = float(input("secound number: "))
        sol = n1 * n2
        print(sol)
    case 4:
        n1 = float(input("first number: "))
        n2 = float(input("secound number: "))
        sol = n1 / n2
        print(sol)
    case 5:
        n1 = float(input("number: "))
        n2 = float(input("to the power of: "))
        sol = pow(n1, n2)
        print(sol)
