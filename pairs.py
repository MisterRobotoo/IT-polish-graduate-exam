with open("dane_przyklad.txt", "r") as dp:
    for line in dp:
        line = line.strip()
        print(line)
        langth = len(line)
        print(langth)

    x = 0
    y = 1
    pairs = []

    quantity_pairs = langth // 2
    
    while x < langth:
        pairs.append((line[x], line[y]))
        x += 2
        y += 2
    print(pairs)
    print(quantity_pairs)

    x = 0
    y = 1

    np_pairs = []
    quantity_np_pairs = 0

    while y < quantity_pairs:
        if pairs[x] == pairs[y]:
            np_pairs.append((pairs[x], pairs[y]))
            quantity_np_pairs += 1
        x += 1
        y += 1
    print(np_pairs)
    print(quantity_np_pairs)