s = input()

maru = []
batu = []

for index, char in enumerate(s):
    if char == "o":
        maru.append(index)
    elif char == "x":
        batu.append(index)


count = 0
flag = True
n = 0

a = 0
b = 0
c = 0
d = 0

while n < 10000:

    a = n // 1000
    b = (n % 1000) // 100
    c = (n % 100) // 10
    d = n % 10

    n = str(a) + str(b) + str(c) + str(d)

    flag = True

    for m in maru:
        if str(m) not in n:
            flag = False
            break

    for b in batu:
        if str(b) in n:
            flag = False
            break

    if flag == True:
        count += 1

    n = int(n) + 1

print(count)
