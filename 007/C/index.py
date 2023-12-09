from collections import deque

# 4
# 2 6 1
# 6 1 5 7
# 1 5 7 7

# . 1 1 . 0 . 1 .


# キュー
que = deque()


# 行数・列数
row_count, column_count = list(map(int, input().split()))

# スタート
start_x, start_y = list(map(int, input().split()))
start = (start_x - 1, start_y - 1, 0)

# ゴール
goal_x, goal_y = list(map(int, input().split()))
goal = (goal_x - 1, goal_y - 1)


# 壁情報
m = []
for i in range(row_count):
    m.append(input())

# 距離の二次元配列
distance = [[-1 for i in range(row_count)] for j in range(column_count)]
# print(distance)
que.append(start)

while len(que) != 0:
    # 先頭を取り出す
    tpl = que.popleft()
    x = tpl[0]
    y = tpl[1]
    d = tpl[2]
    # print("x y d")
    # print(x,y,d)
    # print("distance")
    # print(distance)

    if distance[x][y] != -1:
        continue

    distance[x][y] = d

    # 4方向のマス
    tpl1 = (x - 1, y, d + 1)
    tpl2 = (x + 1, y, d + 1)
    tpl3 = (x, y - 1, d + 1)
    tpl4 = (x, y + 1, d + 1)

    # 探索済みでなく壁じゃなかったらキューに追加
    if m[tpl1[1]][tpl1[0]] != "#" :
        que.append(tpl1)
    if m[tpl2[1]][tpl2[0]] != "#" :
        que.append(tpl2)
    if m[tpl3[1]][tpl3[0]] != "#" :
        que.append(tpl3)
    if m[tpl4[1]][tpl4[0]] != "#" :
        que.append(tpl4)

print(distance[goal[1]][goal[0]])
