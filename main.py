



f = open('sygnaly.txt', 'r')
ktore = 0
pom_1 = 40
odp_1 = ''
najw_2 = ''
ile_2 = 0
for linia in f:
    ktore += 1
    t = []
    x = linia.strip()
    if ktore == pom_1:
        pom_1 += 40
        odp_1 = odp_1 + x[9]
    for y in range(len(x)):
        if x[y] not in t:
            t.append(x[y])
    if len(t) > ile_2:
        ile_2 = len(t)
        najw_2 = x
f.close()

print(f"4.1: {odp_1}")
print(f"4.2: {najw_2} {ile_2}")
print("4.3: ")
f = open('sygnaly.txt', 'r')

for linia in f:
    x = linia.strip()
    is_3 = True
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            a = ord(x[i]) - ord(x[j])
            if a > 10 or a < -10:
                is_3 = False
    if is_3:
        print(x)
