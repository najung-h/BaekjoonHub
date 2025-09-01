

from collections import deque


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def bfs(start_point):
    '''
    bfs 하겠습니다. 
    start_point를 받아서 최소한의 칸 수를 반환합니다.
    '''
    rdx, cdx = start_point
    min_cnt = 999999
    visited_lst = [[False] * N for _ in range(N)]
    q = deque()

    visited_lst[rdx][cdx] = True
    q. append((rdx, cdx, 0))   # 좌표와 이동칸수

    while q:
        rr, cc, kk = q.popleft()
        
        for d in range(4):
            r = rr + dr[d]
            c = cc + dc[d]

            if (r,c) == end_point:
                return kk
            
            # 규격 이내라면
            if 0<=r<N and 0<=c<N:
                #통로라면
                    if big_arr[r][c] == 0:
                    # 아직 방문하지 않았다면
                        if not visited_lst[r][c]:
                        # 도착지가 아니라면,
                        # if (r,c) != end_point:
                            visited_lst[r][c] = True
                            q.append((r,c, kk+1)) # 
    
    return 0





T = int(input())

for tc in range(1, T+1):
    N = int(input())
    big_arr = [list(map(int, input())) for _ in range(N)]

    for rdx in range(N):
        for cdx in range(N):
            if big_arr[rdx][cdx] == 2:
                start_point = (rdx, cdx)
            elif big_arr[rdx][cdx] == 3:
                end_point = (rdx, cdx)

    result = bfs(start_point)
                
    print(f'#{tc} {result}')
    

