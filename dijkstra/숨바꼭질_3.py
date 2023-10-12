import heapq

N, K = map(int, input().split())

MAX = 100001
INF = 1e9
time = [INF] * MAX

def dijkstra(start):

    Q = []
    heapq.heappush(Q, (0, start))
    time[start] = 0

    if 0 <= start - 1:
        heapq.heappush(Q, (1, start-1))
        time[start - 1] = 1
    if start + 1 < MAX:
        heapq.heappush(Q, (1, start+1))
        time[start + 1] = 1
    if 2 * start < MAX:
        heapq.heappush(Q, (0, start * 2))
        time[start * 2] = 0

    while(Q):

        t, node = heapq.heappop(Q)

        if node == K:
            break

        if time[node] < t:
            continue

        for spot in [node-1, node+1]:
            if 0 <= spot < MAX and t + 1 < time[spot]:
                time[spot] = t + 1
                heapq.heappush(Q, (t + 1, spot))
        if 2 * node < MAX and t < time[2 * node]:
            time[2 * node] = t
            heapq.heappush(Q, (t, 2 * node))
        
    

dijkstra(N)
print(time[K])