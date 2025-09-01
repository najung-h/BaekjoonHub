
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def dfs(start_point):
    rdx, cdx = start_point
    visited_lst = [[False] * 16 for _ in range(16)]
    q = deque()

    visited_lst[rdx][cdx] = True
    q.append((rdx, cdx))
    
    while q:
        rr, cc = q.pop()
        # print(f'현재 {rr}, {cc}')

        for d in range(4):
            r = rr + dr[d]
            c = cc + dc[d]

            if (r,c) == end_point:
                return 1
            
            #  규격 내 확인
            if 0<=r<16 and 0<=c<16:
                
                # 방문했는지 확인
                if not visited_lst[r][c] :
                
                    # 통로인지 확인 
                    if maze_arr[r][c] == 0: 

                        # 방문 표시 후 데크에 삽입
                        visited_lst[r][c] = True
                        q.append((r,c))
    
    return 0
    



T = 10
for tc in range(1, T+1):
    TC = int(input())
    maze_arr = [list(map(int, input())) for _ in range(16)]

    # 1. 미로의 출발점과 도착점 찾기
    for rdx in range(16):
        for cdx in range(16):
            if maze_arr[rdx][cdx] == 2:
                start_point = (rdx, cdx)
            elif maze_arr[rdx][cdx] == 3:
                end_point = (rdx, cdx)

    # print(start_point)
    # print(end_point)

    # 2. 미로의 출발점에서 dfs 하겠습니다.
    result = dfs(start_point)

    # 3. 결과 출력
    print(f'#{tc} {result}')

    