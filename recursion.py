def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pow(a, b - 1)

def A(m, n):
    global calls
    calls += 1

    if n == 1:
        return m
    elif n % 2 == 0:
        return A(2 * m, n // 2)
    else:
        return 2 * A(m, (n - 1) // 2) + m

calls = -1 #starts at -1 because the script caunts a start function as a call                             
print(A(3, 9), calls)
calls = -1
print(A(pow(2, 5), pow(2, 5)), calls)
calls = -1
print(A(10, 15),calls)
calls = -1
print(A(1, pow(2, 100) + 1), calls)

calls = -1
print(A(1, 777), calls)
calls = -1
print(A(2*pow(10, 6), 256*pow(10, 6)), calls)
