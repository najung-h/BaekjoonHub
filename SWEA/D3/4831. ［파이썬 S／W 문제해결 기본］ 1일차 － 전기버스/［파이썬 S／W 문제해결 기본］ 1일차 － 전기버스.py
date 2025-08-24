T = int(input())
for tc in range(1, T +1):
    K, N, M = list(map(int, input().split()))
    charge_station_set = set(map(int, input().split()))
    # 멤버십 검사를 위해 set으로 형변환
    
    now = 0
    charge = 0
    
    while now + K < N:  # 충전이 필요할 때까지 반복

        for k in range(K, 0, -1): # 충전이 필요하다면, 최대한 멀리부터 이동해서 충전기 탐색
            if (now + k) in charge_station_set:
                #(f'{now}에서 {now + k}으로 이동할게요!')
                now += k
                charge += 1
                break
            
        else:
            charge = 0
            break

    
    
    print(f'#{tc} {charge}')