'''델타 탐색법과 dfs를 함께 사용해서 풀이할게요.'''
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)



def dfs(start_point):
    start_r, start_c = start_point
    steak.append((start_r, start_c))
    visited_set = {(start_r, start_c)}

    while steak:
        rdx, cdx = steak.pop()

        for d in range(4):
            r = rdx + dr[d]
            c = cdx + dc[d]

            if 0<=r<N and 0<= c<N: # 규격 이내라면 ㅎ
                if (r,c) not in visited_set: # 아직 안 가봤다면 
                    if big_arr[r][c] == 0: # 길이라면

                        visited_set.add((r,c))
                        steak.append((r,c))

                    elif big_arr[r][c] == 3: # 도착했다면
                        return 1

    return 0




                
        


            





T= int(input())

for tc in range(1, T+1):
    N = int(input())
    big_arr = [list(map(int, input())) for _ in range(N)]

    # 출발점과 도착점을 찾자.
    steak = deque()
    visited_set = set() 

    for rdx in range(N):
        for cdx in range(N):
            if big_arr[rdx][cdx] == 2:
                start_point = (rdx, cdx)
            if big_arr[rdx][cdx] == 3:
                end_point = (rdx, cdx)

    result = dfs(start_point)

    print(f'#{tc} {result}')

    