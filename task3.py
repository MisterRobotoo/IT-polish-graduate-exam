lines = 0
w = 0
pairs = []
words = []

with open("pary.txt", "r") as pp:
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
s = []

while x < w:
    y = 0
    z = 0
    letters = []
    asciwod = 0

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    word = words[x]
    wlen = len(word)
    #print(wlen)
    
    while y < wlen:
        letters.append(word[y])
        y += 1

    while z < wlen:
        letter = letters[z]
        match letter:
            case "a":
                a += 1
            case "b":
                b += 1
            case "c":
                c += 1
            case "d":
                d += 1
            case "e":
                e += 1
        ascilet = ord(letter)
        asciwod += ascilet
        #print(ascilet)
        z += 1
    #print(asciwod)

    s.append((a,b,c,d,e))
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
print("Answer for 3.1:  ", a_val[n - 1])

a = 0
b = 1
sws = []

while b < w:
    len_a = len(s[a])
    len_b = len(s[b])
    x = 0
    y = 0
    m = 0
    ws = []
    while x < len_b:
        if s[a][x] < s[b][x]:
            ws.append(s[a][x])
        else:
            ws.append(s[b][x])
        x += 1
    len_ws = len(ws)
    while y < len(ws):
        m += ws[y]
        y += 1
    sws.append(m)
    a += 2
    b += 2

n = len(sws)
for i in range(n - 1):
    for j in range(n - i - 1):
        if sws[j] > sws[j +  1]:
            sws[j], sws[j + 1] = sws[j + 1], sws[j]
print("Answer for 3.2:  ", sws[n - 1])

prefix = []
for word_a, word_b in pairs:
    best = 0
    max_len = min(len(word_a), len(word_b))

    for i in range(5, max_len + 1):
        if word_a[:i] == word_b[-i:]:
            best = i
        if word_a[-i:] == word_b[:i]:
            best = i

    #print(word_a, word_b, best)

    if best >= 5:
        prefix.append((word_a, word_b, best))

print("Answer for 3.3:  ", prefix)
