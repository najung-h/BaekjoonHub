from collections import deque

def bfs(S, G):
    visited_lst = [False] * (V+1)
    q = deque()

    visited_lst[S] = True
    q.append((S, 0))

    while  q:
        current_node, cnt = q.popleft()

        for items in node_info_lst[current_node]:
            # 도착 노드 발견
            if items == G:
                return cnt + 1
            
            # 아직 가지 않았다면,
            if not visited_lst[items] :
                visited_lst[items] = True
                q.append((items, cnt+1))
                
    
    return 0









T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    node_info_lst = [[] for _ in range(V+1)] # 0번 비워두기
    
    for _ in range(E):
        a,b = list(map(int, input().split()))
        node_info_lst[a].append(b)
        node_info_lst[b].append(a)
    # print(node_info_lst)

    # 출발 노드 S와 도착 노드 G
    S, G = list(map(int, input().split()))
    # print(S, G)

    result = bfs(S, G)

    print(f'#{tc} {result}')