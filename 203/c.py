n,k = list(map(int, input().split()))

money = k

dict = {}

for num in range(n):
    a,b = list(map(int, input().split()))
    if a in dict:
        dict[a] += b
    else:
        dict[a] = b

sortedKeys = sorted(dict.keys())
print(dict)

villageNum = 0
# # # 所持金が0になるまでループ
while money > 0:
    if villageNum in sortedKeys:
        money += dict[villageNum]

    money -= 1
    villageNum += 1

print(villageNum)

# # 結果
# count = 0

# # Aのループ
# for a in arrayA:
#     # Cのループ
#     for c in arrayC:
#         cj = c
#         bcj = arrayB[cj - 1]
#         if a == bcj: count += 1

# print(count)
