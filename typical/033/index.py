# 解答見て分からなかった

H, W = list(map(int, input().split()))

area = H * W
ans = area // 4 if area % 4 == 0 else area // 4 + 1

print(ans)
