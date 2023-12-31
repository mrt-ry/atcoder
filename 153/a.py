h, a = list(map(int, input().split()))

# ans = 0

# while h > 0:
#     h -= a
#     ans += 1

# print(ans)

# 割り算で行った場合

if h % a == 0:
    print(h // a)
else:
    print(h // a + 1)
