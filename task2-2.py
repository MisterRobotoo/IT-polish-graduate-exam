a = 27732
b = 72619

inmem = 0
p = 0
while a > 0:
    numa = a % 10 # mod 10 is always the last digit od the number
    numb = b % 10
    sum = numa + numb + inmem
    if sum >= 10:
        inmem = 1
        p += 1
    else:
        inmem = 0
    a = a // 10 # // operates integer devision and skip the change
    b = b // 10
print(p)
