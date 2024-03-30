a, b, k = list(map(int, input().split()))


def is_range_number(n):
    if n - a < k or b - n < k:
        return True


for i in range(a, b + 1):
    if is_range_number(i):
        print(i)
