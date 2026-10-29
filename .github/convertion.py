#power function
def pow(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * pow(n, m - 1)

#converting any to decimal
def anytodec():
    a = input("enter the number: ")
    b = int(input("enter the base of the number: "))
    c = 0
    for i in range(len(a)):
        c += int(a[i]) * pow(b, len(a) - 1 - i)
    print(c)

#anytodec()

def dectoany():
    a = int(input("enter the number: "))
    b = int(input("enter the base to convert to: "))
    c = ""
    while a > 0:
        c = str(a % b) + c
        a //= b
    print(c)

dectoany()