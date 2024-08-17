x = input()

# 末尾の数字が0の場合は削除
for i in range(3):
    if x[-1] == "0":
        x = x[:-1]

# 整数の場合は.を削除
if x[-1] == ".":
    x = x[:-1]

print(x)
