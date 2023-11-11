n = int(input())
nums = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(n - i - 1):
        if (nums[i] - nums[j +i + 1]) % 200 == 0:
            result += 1

print(result)
