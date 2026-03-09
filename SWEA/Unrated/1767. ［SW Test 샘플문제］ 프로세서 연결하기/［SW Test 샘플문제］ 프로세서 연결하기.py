# 방향: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
def dfs(idx, core_cnt, wire_len):
    global max_core, min_wire
     
    # 가지치기: 남은 코어를 다 합쳐도 현재 최대 코어보다 적으면 탐색 종료
    if core_cnt + (len(cores) - idx) < max_core:
        return
     
    # 모든 코어를 확인한 경우
    if idx == len(cores):
        if core_cnt > max_core:
            max_core = core_cnt
            min_wire = wire_len
        elif core_cnt == max_core:
            min_wire = min(min_wire, wire_len)
        return
 
    r, c = cores[idx]
     
    # 4방향 탐색
    for i in range(4):
        can_connect = False
        dist = 0
        nr, nc = r, c
         
        while True:
            nr += dr[i]
            nc += dc[i]
             
            # 벽에 도달하면 연결 성공
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                can_connect = True
                break
            # 중간에 전선이나 코어를 만나면 실패
            if board[nr][nc] != 0:
                break
            dist += 1
             
        if can_connect:
            # 전선 채우기 (2로 표시)
            curr_r, curr_c = r, c
            for _ in range(dist):
                curr_r += dr[i]
                curr_c += dc[i]
                board[curr_r][curr_c] = 2
             
            dfs(idx + 1, core_cnt + 1, wire_len + dist)
             
            # 백트래킹 (원상 복구)
            curr_r, curr_c = r, c
            for _ in range(dist):
                curr_r += dr[i]
                curr_c += dc[i]
                board[curr_r][curr_c] = 0
                 
    # 코어를 연결하지 않고 넘어가는 경우도 체크
    dfs(idx + 1, core_cnt, wire_len)
 
# SWEA 전용 입력 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
     
    cores = []
    for r in range(N):
        for c in range(N):
            # 가장자리에 있는 코어는 이미 연결된 것으로 간주하므로 제외
            if board[r][c] == 1:
                if r == 0 or r == N-1 or c == 0 or c == N-1:
                    continue
                cores.append((r, c))
                 
    max_core = 0
    min_wire = float('inf')
     
    dfs(0, 0, 0)
    print(f"#{tc} {min_wire}")