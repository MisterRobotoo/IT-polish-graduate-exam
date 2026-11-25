from collections import Counter

e = [] # Employee
s = [] # Supervisor

lines = 0
with open("Dane-NF-2605/korpo.txt") as korpo:
    for line in korpo:
        lines += 1
        line = line.strip()
        e.append(int(lines))
        s.append(int(line))

print(len(e))

x = 0
y = 0
ns = 1 # employee not an supervisor
for x in s:
    y += 1
    if x == len(e): break
    if y in s:
        x += 1
    else:
        ns += 1
print(ns)

counts = Counter(s)
most_common_value, count = counts.most_common(1)[0]
print(most_common_value, count)

sc = [] # supervisor counts

for employee in range(1, len(s) + 1):
    count = 0
    boss = s[employee - 1]

    while boss != 0:
        count += 1
        boss = s[boss - 1]

    sc.append(count)
maximum = max(sc)
print(maximum, sc.count(maximum))