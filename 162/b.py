n = int(input())


def is_fizzbuzz(n):
    if n % 3 == 0 or n % 5 == 0:
        return True


result = 0

for i in range(1, n + 1):
    if not is_fizzbuzz(i):
        result += i

print(result)
