n, x, t = list(map(int, input().split()))

ans = 0
if n % x == 0:
    ans = n // x * t
else:
    ans = n // x * t + t

print(ans)
