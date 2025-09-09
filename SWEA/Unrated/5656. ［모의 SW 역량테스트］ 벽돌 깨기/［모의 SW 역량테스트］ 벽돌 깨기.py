#import sys
#sys.stdin = open('input_5656.txt', 'r')


from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def shoot(cnt, remains, now_arr):
    global min_blocks

    # 종료 조건 : N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return 
    
    # 모든 열에 한 줄 씩 떨구자
    for col in range(W):

        '''# 벽돌이 없으면 안 떨궈도 됨
        # 구슬이 파괴되는 가장 윗 층을 찾아줘야함'''

        '''
        방법 1. 원본을 복사해두고, 다시 되돌리는 방법
        1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
        copy_arr = copy.deepcopy
        2. 원본 리스트의 col 위치에 떨구고
        3. cnt+1번 재귀 상태로 이동한 다음에
        4. 떨구기 전 상태로 복구
        '''

        '''
        방법 2. 복구 시간이 없는 방식
        1. col 위치에 떨구기 전 상태를 복사
        copy_arr = [row[:] for row in arr]
        2. 복사한 리스트의 col 위치에 떨군다.
        3. cnt + 1번 상태로 이동할 때, copy_arr를 함께 전달
        '''
        copy_arr = [row[:] for row in now_arr]
        
        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H): # 위에서부터 전체를 볼 예정
            if copy_arr[r][col]: 
                row = r
                break

        # 벽돌이 없는 열은 무시
        if row == -1:
            continue
        
        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 담아야한다.
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1 # 벽돌 하나 줄엇다.
        copy_arr[row][col] = 0 #초기화 # 구슬이 처음 만나는 벽돌 자리

        # 주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p칸을 모두 제거
            for k in range(1, p): # 자기자신은 의미없으니 빼고 1부터 p-1개
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc <0 or nc >=W:
                        continue

                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue

                    # 벽돌이 있으면:
                    # 1) 그 벽돌도 연쇄 파괴의 기점이 되므로 큐에 추가
                    # 2) 즉시 제거(중복 파괴 방지), 3) 남은 벽돌 수 감소
                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0 #벽돌 제거
                    now_remains -= 1 # 남은 벽돌 수 감소


        # 빈칸 메우기 # 중력 처리
        for c in range(W):
            idx = H - 1  # 벽돌이 위치할 index # 바닥부터 채움 # 역순
            # 바닥부터 천장가지 거슬로 올라가면서 벽돌을 끌어내린다.
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]: # 현재 가장 낮은 칸으로 보내버리자.
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1 # 다음 벽돌이 쌓일 자리를 한 칸 위로 설정한다.


        # cnt+1번째 구슬을 쏘는 상태로 재귀 호출
        shoot(cnt + 1, now_remains, copy_arr)






T = int(input())
for tc in range(1, T+1):

    '''
    1. 최소 벽돌
    - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다 - > 현재 벽돌 수를 관리

    2. n번의 구슬을 굴려야한다.
    - 모든 케이스를 보아야 한다.(12 ^ 4, 약 25만번)
    - 백 트래킹
        - 한 번 쏘았을 때 벽돌들이 연쇄로 개진다.
        - 현재 기준으로 퍼져나가면서 탐색 (BFS)
        - 빈칸 메우기

    '''
    N, W, H = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(H)]

    # 최소 벽돌수
    min_blocks = 1e9

    # 남은 벽돌 수 저장
    blocks = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1
    
    # 구슬 쏘기
    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')

