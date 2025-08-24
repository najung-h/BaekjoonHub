T = 10
 
 
for test_case in range(1, T + 1):
    N = int(input())
 
    building_lst = list(map(int, input().split()))
    # print(building_lst)
    # [0, 0, 254, 185, 76, 227, 84, 175, 0, 0]
 
 
 
    view_right_num = 0   # 조망권이 확보된 건물의 수
 
    idx = 0   # 몇번째 빌딩이니?
    for building in building_lst:
 
        if building == 0:
            idx += 1
            pass
 
        else:
            # 양옆으로 두 개 다 비교해서 해당 건물보다 낮다면.
            if building_lst[idx-1] < building and building_lst[idx-2] < building and building_lst[idx+1] <building and building_lst[idx+2] < building:
                # 정확히 몇 칸에 대해서 조망권이 확보되는지를 min or max 로 확인.
                # 원래 min 쓰는게 맞는데, 실수로 잘못 빼서 -씌우고 max 함수 사용함
                view_right_num += -(max( building_lst[idx-1] - building, building_lst[idx-2] - building, building_lst[idx+1] - building, building_lst[idx+2] - building))
            idx += 1
 
 
 
 
    print(f'#{test_case} {view_right_num}')