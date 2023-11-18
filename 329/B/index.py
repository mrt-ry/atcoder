s = int(input())
nums = list(map(int, input().split()))

max_num = max(nums)
count = 0

for num in nums:
    if num == max_num:
        count += 1

for i in range(count):
    nums.remove(max_num)

result = max(nums)

print(result)
