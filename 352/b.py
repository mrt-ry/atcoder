s = input()
t = input()

s_list = list(s)
t_list = list(t)

result_array = []

t_count = 0

# s_listに対して繰り返し
for s_char in s_list:
    # t_listの文字とs_charが一緒だったらindexをresult_arrayに格納
    for i in range(t_count, len(t_list)):
        if s_char == t_list[i]:
            t_count = i + 1
            result_array.append(str(i + 1))
            break

print(" ".join(result_array))
