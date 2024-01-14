n, a, b = list(map(int, input().split()))

# ans = 0

# for i in range(1, n+1):
#     # 値保持
#     tmp = i

#     # 格桁の合計
#     sum = 0
#     while i > 0:
#         sum += i % 10
#         i //= 10

#     # 条件式
#     if a <= sum and sum <= b:
#         ans += tmp

# print(ans)

# 解答コード


def cals_sum_digits(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10

    return sum_digit


result = 0

for i in range(1, n + 1):
    if a <= cals_sum_digits(i) <= b:
        result += i

print(result)
