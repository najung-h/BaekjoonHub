
'''dfs로 풀이하겠습니다.'''
 
from collections import deque
 
# 델타탐색
dr = [-1, 1, 0, 0] 
dc = [0, 0, -1, 1]
 
opp_dir = {0:1, 2:3, 3:2, 1:0}
 
 
def dfs(max_r, max_c):
    '''각각의 max 포인트마다 돌리기 시작할 함수입니다. '''
     
    q = deque()
    max_h = big_arr[max_r][max_c] # 높이 확인
 
    l = 1
    gongsa = False
    visited_set = {(max_r, max_c)}
 
    q.append((max_r, max_c, max_h, -1, l, gongsa, visited_set)) 
    # 행인덱스, 열인덱스, 높이, 직전 방향, 탐색 경로 길이, 공사했니
    # 초기에는 방향이 의미없으니, 
    # 0,1,2,3 아닌 수 암거나 넣어둠 
    # 방향의 경우, 직전 방향으로 다시는 돌아가지 않게끔 하기 위해서 
    # 참고할 예정
     
    #print('등산로 출발점 ', (max_r, max_c, max_h, -1, l, K))
 
    max_l = 1
 
    while q:
        rdx, cdx, hdx, bf_d , l, gongsa, visited = q.popleft()
 
        if l > max_l :
            max_l = l
             
 
        # 초기 확인 - 출발점
        for d in range(4):
            '''if opp_dir.get(d) == bf_d: # 갔던 방향으로 되돌아가는 셈 
                continue                # -> 되돌아가지마'''
 
            # 델타탐색
            r = rdx + dr[d]
            c = cdx + dc[d]
 
            if 0<=r<N and 0<=c<N and (r,c) not in visited: 
                #규격 이내일 때만 고려, 
                # 안 갔을 때만 고려
                h = big_arr[r][c]
                if  h< hdx:
                    q.append((r,c,h, d, l+1, gongsa, visited.union({(r,c)})))
                    #print('등산로 가능', (r,c,h, d, l+1, k))
 
                if h>=hdx:
                    if gongsa:# 공사 했으면 
                        continue  # 넘어가, 이제 더 이상 등산로 안 됨
                    
                    else:  # 공사 안 했으면 공사해보자.
                        for kk in range(1,K+1):
                            if h-kk < hdx:
                                q.append((r,c,h-kk,d,l+1, True, visited.union({(r,c)})))
                                break
                    #print('공사하면서 깍자', (r,c,h-1,d,l+1, k-1))
 
 
    return max_l
 
 
 
T = int(input())
 
for tc in range(1, T+1):
    N, K = tuple(map(int, input().split()))
    big_arr = [list(map(int, input().split())) for _ in range(N)]
 
    # 큐 써서 dfs 탐색 할 예정
    q = deque()
 
    # 높이가 얼만게 가장 높은거야?
    max_height = max([max(row) for row in big_arr])    
 
    # 가장 높은 포인트들 찾아서
    # 싹 다 map_point_lst에 담아놓자.
    max_point_lst = []
    for x in range(N):
        for y in range(N):
            if big_arr[x][y] == max_height:
                max_point_lst.append((x,y))
 
 
    # 이제 map_point_lst에 담아놓은 
    max_path_length = 0
    for x,y in max_point_lst:
        # 모든 시작점에 대해서 등산로 길이를 탐색해서
        path_length = dfs(x, y)
 
        # 대빵인 놈을 찾자.
        if path_length > max_path_length:
            max_path_length = path_length
 
    print(f'#{tc} {max_path_length}')