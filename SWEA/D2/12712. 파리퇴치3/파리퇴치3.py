def spray_range_plus(now_point):
    '''이 함수는
    스프레이를 뿌리는 범위에 따라서
    스프레이가 닿는 범위를 set으로다가 출력해줍니다.
    단, + 방향에 해당하는 함수입니다ㅏ.
    
    '''
    spray_set_plus = set()

    x = now_point[0]
    y = now_point[1]
    ### 상하좌우 찾아보기
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    # 영역을 벗어나도 상관없다고 하나, 
    # 범위를 벗어나면 우리의 이중 리스트를 돌지 못할 것이므로, 없애버릴 것이에요

    for m in range(M):              # 스프레이 세기만큼
        for d in range(4):
            a = x + dr[d] * m
            b = y + dc[d] * m
            if 0<= a <N and 0<= b<N:             #범위 밖이면 없애자
                spray_set_plus.add((a,b))
                #print((a,b))
    return spray_set_plus





def spray_range_x(now_point):
    '''이 함수는
    스프레이를 뿌리는 범위에 따라서
    스프레이가 닿는 범위를 set으로다가 출력해줍니다.
    단, x 방향에 해당하는 함수입니다ㅏ.
    
    '''
    spray_set_x = set()

    x = now_point[0]
    y = now_point[1]
    ### 각 방향 찾아보기
    dr = [-1, +1, +1, -1]  
    dc = [+1, -1, +1, -1]

    # 영역을 벗어나도 상관없다고 하나, 
    # 범위를 벗어나면 우리의 이중 리스트를 돌지 못할 것이므로, 없애버릴 것이에요

    for m in range(M):              # 스프레이 세기만큼
        for d in range(4):
            a = x + dr[d] * m
            b = y + dc[d] * m
            if 0<= a <N and 0<= b<N:             #범위 밖이면 없애자
                spray_set_x.add((a,b))
                #print((a,b))
    return spray_set_x


#print(spray_range_plus(now_point))
#print(spray_range_x(now_point))
#{(1, 2), (1, 1), (1, 4), (0, 2), (2, 2), (1, 0), (3, 2), (1, 3)}
#{(0, 1), (1, 2), (2, 1), (3, 4), (0, 3), (3, 0), (2, 3)}


def get_flies(input_set):
    flies = 0

    for s in input_set:
        r = s[0]
        c = s[1]

        flies += big_arr[r][c]
    
    return flies




T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    big_arr = [list(map(int,input().split())) for _ in range(N)]

    flies_lst = []

    for i in range(N):
        for j in range(N):
            now_point = (i,j)


            input_set_plus = spray_range_plus(now_point)
            flies_lst.append(get_flies(input_set_plus))

            input_set_x = spray_range_x(now_point)
            flies_lst.append(get_flies(input_set_x))

    
    print(f"#{test_case} {max(flies_lst)}")


