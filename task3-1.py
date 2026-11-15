lines = 0
w = 0
pairs = []
words = []

with open("Dane-NF-2605/pary.txt", "r") as pp:
    for line in pp:
        lines += 1
        line = line.strip()
        pair = line.split(" ")
        langth = len(pair)
        #print(langth)
        
        pairs.append(pair)
        
        words.append(pair[0])
        words.append(pair[1])
        w += 2

#print(pairs[0])
#print(words)
#print(w)

x = 0
asciwods = []

while x < w:
    y = 0
    z = 0
    letters = []
    asciwod = 0
    
    word = words[x]
    wlen = len(word)
    #print(wlen)
    
    while y < wlen:
        letters.append(word[y])
        y += 1

    while z < wlen:
        letter = letters[z]
        ascilet = ord(letter)
        asciwod += ascilet
        #print(ascilet)
        z += 1
    #print(asciwod)

    asciwods.append(asciwod)

    x += 1
#print(asciwods)

a = 0
b = 1
a_val = []

while b < w:
    a_val.append(abs(asciwods[a] - asciwods[b]))
    a += 2
    b += 2
#print(a_val)

#   Bubble Sort algorithm

n = len(a_val)
for i in range(n - 1):
    for j in range(n - i - 1):
        if a_val[j] > a_val[j +  1]:
            a_val[j], a_val[j + 1] = a_val[j + 1], a_val[j]
print(a_val)
