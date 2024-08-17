a, b, c = list(map(int, input().split()))

# 24時を超えている場合は24を足して補正
if b > c:
    c += 24
    if a < b:
        a += 24

ans = "No" if b < a and a < c else "Yes"
print(ans)
