import heapq

n, m = list(map(int, input().split()))

graph = {}

# グラフの作成
for i in range(n):
    graph[i + 1] = []

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

q = [1]
heapq.heapify(q)

visited = [False for _ in range(n)]

while q:
    current = heapq.heappop(q)
    visited[current - 1] = True
    toList = graph[current]
    for to in toList:
        heapq.heappush(q, to)

print(graph)
