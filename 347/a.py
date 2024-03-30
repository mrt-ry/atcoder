n, k = list(map(int, input().split()))

array = list(map(int, input().split()))


ans = []

for i in array:
    if i % k == 0:
        ans.append(i // k)

ans = sorted(ans)
print(" ".join(map(str, ans)))
