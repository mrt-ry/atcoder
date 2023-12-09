n = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayC = list(map(int, input().split()))
# 結果
count = 0

# Aのループ
for a in arrayA:
    # Cのループ
    for c in arrayC:
        cj = c
        bcj = arrayB[cj - 1]
        if a == bcj: count += 1

print(count)
