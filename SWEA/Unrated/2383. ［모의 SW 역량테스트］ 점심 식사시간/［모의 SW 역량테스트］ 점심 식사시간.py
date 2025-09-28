# import sys
# sys.stdin = open('input_2383.txt', 'r')


from heapq import heappush, heappop

def moving(stair_arrival_time, stair_length):
    if not stair_arrival_time:
        return 0
    stair_arrival_time.sort()
    on_stair = []  # 현재 하강 중인 사람들의 종료시각을 담는 최소힙
    
    for a in stair_arrival_time:
        # a 시간에 도착한 사람에 대해서 살펴보자.
        
        # 이미 진입한 사람 있다면 그 중에 빠질 사람 있니?
        while on_stair and on_stair[0] <= a:
            heappop(on_stair)
        
        # 계단 가득 안 찼다면
        if len(on_stair) < 3:
            # 바로 하강 시작 가능
            finish = a + stair_length
            heappush(on_stair, finish)
        else: # 계단 차있으니까.
            # 가장 빨리 끝나는 사람 이후에 시작
            earliest = heappop(on_stair)
            # (earliest 가 최소이므로 추가 pop은 불필요)
            finish = earliest + stair_length
            heappush(on_stair, finish)
            
    # 그 계단을 이용한 사람들 모두가 다 내려간 시각
    return max(on_stair)

def solve():

        
    # 사람은 좌표값만 저장하고, 계단은 좌표값 + 계단 길이를 함께 저장해야됨.    
    human_lst = []
    stair_lst = []  # (r, c, P)
    for r in range(N):
        for c in range(N):
            val = big_arr[r][c]
            if val == 1:
                human_lst.append((r, c))
            elif val > 1:
                stair_lst.append((r, c, val))

            # 백트래킹 야무지게
            if len(human_lst) >= 10 and len(stair_lst)>=2 :
                break
        if len(human_lst) >= 10 and len(stair_lst)>=2 :
            break
        # 문제에서 계단은 2개, 사람은 최대 10명이라고 지정했기 때문
    
    # 계단에 대한 정보 받아두기
    sr1, sc1, sl1 = stair_lst[0]
    sr2, sc2, sl2 = stair_lst[1]
    
    human_num = len(human_lst)
    min_time = 10**9

    # 미리 사람별 두 계단까지의 도착 시각을 싹 계산
    # 택시 거리
    arr1 = []
    arr2 = []
    
    for hr, hc in human_lst:
        arr1.append(abs(hr - sr1) + abs(hc - sc1) + 1)
        arr2.append(abs(hr - sr2) + abs(hc - sc2) + 1)

    # 사람들을 두 계단으로 배정하는 모든 경우 탐색 (비트마스크)
    # 사람들을 일단 계단 1과 계단 2로 보내버리고
    for mask in range(1 << human_num):
        stair_1_arrival_time, stair_2_arrival_time = [], [] # 도착 시간 모으기
        for i in range(human_num):
            if (mask >> i) & 1:
                stair_2_arrival_time.append(arr2[i])
            else:
                stair_1_arrival_time.append(arr1[i])
        
        # 각 계단을 시뮬레이션 해서, 마지막 종료시간 모으기        
        t1 = moving(stair_1_arrival_time, sl1)
        t2 = moving(stair_2_arrival_time, sl2)
        
        # 더 늦게 끝난 시간이 최종 시간
        total = max(t1, t2)
        
        # 최소 갱신
        min_time = min(min_time, total)
        
    return min_time


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    big_arr = [list(map(int, input().split())) for _ in range(N)]
    # print(big_arr)
    
    ans = solve()
    print(f'#{tc} {ans}')