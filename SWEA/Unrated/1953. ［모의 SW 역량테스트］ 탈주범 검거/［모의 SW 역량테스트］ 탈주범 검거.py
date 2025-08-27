'''# 터널 종류에 따라 델타 탐색이 가능한 dr, dc 리스트를 바꾸자
 
# 이후, for time in range(1, n+1):
if 못 가 :
    break
else:
 
 
 
# dr, dc 탐색함수를 구현해서 재귀적으로 탐색을 진행한다.
 
# went_point가 아니고, 델타 범위라면 이동하면서, went_point에 추가
'''
'''
재귀 포기 !
bfs로 진행 
 
'''
# 터널 종류에 따라 델타 탐색이 가능한 dr, dc 리스트를 바꾸자
def turnel_delta_lst(turnel):
    if turnel ==1:
        dr = [+1, -1, 0, 0] # 상하 좌우
        dc = [0, 0, -1, +1] 
        D = 4  # 반복문용
         
    elif turnel == 2 :
        dr = [+1, -1] # 상하 좌우
        dc = [0, 0] 
        D = 2
 
    elif turnel == 3 :
        dr = [0, 0] # 상하 좌우
        dc = [-1, +1] 
        D = 2
         
    elif turnel == 4:
        dr = [-1, 0]  # 상우 
        dc = [0, 1]
        D = 2
    elif turnel == 5:
        dr = [1, 0]   # 하우 
        dc = [0, 1]
        D = 2
    elif turnel == 6:
        dr = [1, 0]   # 하좌 
        dc = [0, -1]
        D = 2
    elif turnel == 7:
        dr = [-1, 0] # 상 좌 
        dc = [0, -1]
        D = 2
     
    return (dr, dc, D) 
 
 
# 이후, for time in range(1, L+1):
 
'''def find_(M, N, C, R, L, dr, dc, went_set):
    rdx = R
    cdx = C
 
     
     
    for time in range(1, L+1):
         
        for d in range(len(dr)):
            r = rdx + dr[d]
            c = cdx + dc[d]
             
             
            if (r,c) not in went_set :
                rdx, cdx = r, c
                went_set.add((r,c))
                find_(M, N, c, r, L-time, *turnel_delta_lst(big_arr[r][c]), went_set)
            else:
                continue
         
    return len(went_set)'''
 
 
 
# dr, dc 탐색함수를 구현해서 재귀적으로 탐색을 진행한다.
# 아니, 재귀 말고 bfs
 
# went_point가 아니고, 델타 범위라면 이동하면서, went_point에 추가
 
 
 
from collections import deque
 
 
 
 
def bfs(rdx, cdx):
    q = deque()
 
    if big_arr[rdx][cdx] == 0:
        return 0 # 시작도 못 해버렸다.
     
    q.append((rdx, cdx, 1)) # 초기 시간은 1입니당
    visited[rdx][cdx] = 1 # 방문 표시
 
    cnt = 0 # 초기값 설정, 도달 가능 몇 개?
 
    while q: 
        rdx, cdx, t = q.popleft()
 
        if t>L : # 제한 시간 지났으면, 더 이상 탐색하지 않아도 된다.
            continue
         
 
        # 아직 제한 시간 이내라면, 
        cnt += 1 
        # 탐색해볼게요.
         
        dr, dc, D = turnel_delta_lst(big_arr[rdx][cdx])  # 터널 확인하고, 방향 받아오기.
         
        for i in range(D):
            r, c = rdx + dr[i], cdx + dc[i]
 
            if 0 <= r < N and 0 <= c < M : #방향 이내여야 함
                if big_arr[r][c] != 0: # 터널이 없지 않다면
                    if visited[r][c] == 0:  # 아직 안 갔다면
 
                        '''여기서 테케 아웃풋보다 내 아웃풋이 너무 많아서 보니까 반대 방향으로 뚤려있는지도 고민해야함.'''
                        opp_dir = (-dr[i], -dc[i])  # 반대 방향
                        newdr, newdc, newD = turnel_delta_lst(big_arr[r][c])
                        ok = False
                        for j in range(newD):                     # 이웃 파이프의 방향 중
                            if (newdr[j], newdc[j]) == opp_dir:        # 반대 벡터 있으면 연결 가능
                                ok = True
                                break
                        if not ok:  # 
                            continue
 
                        q.append((r, c, t+1))  # 시간 하나 늘려서 큐에 삽입.
 
                        visited[r][c] = 1 # 방문 체크
         
    return cnt
 
 
 
 
 
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))
    big_arr = [list(map(int, input().split()))  for _ in range(N)] 
    visited = [[0] * M for _ in range(N)] # 방문했니?
     
    '''print(f'터널은 {N} * {M}의 크기이고, \
          \n 멘홀 뚜껑이 위치한 장소의 위치는 ({R}, {C})이며, \
          \n탈출 후 소요된 시간은 {L}이다.')'''
     
    #print(big_arr)
    '''숫자 0은 터널이 없는 장소, 수자 1-7은 해당 위치의 터널 구조물 타입'''
     
    result = bfs(R, C)
    print(f'#{tc} {result}')