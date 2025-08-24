def is_triple(lst):
    return max(lst) == min(lst)

def is_run(lst):
    '''gpt의 조언 : lst.sort() 대신 하단의 코드를 사용하라.'''
    # 연속된 3개인지 (부작용 없는 정렬)
    a, b, c = sorted(lst)
    return a + 1 == b and b + 1 == c



''' 완전 탐색으로 구현하겠습니다.'''

from itertools import combinations

#import sys
#sys.stdin = open("input_46546.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

total_set = {0,1,2,3,4,5}
    # 시간복잡도를 반으로 나누기 위하여
# 중복된 케이스 제거할게요.
# (1,2,3)에 대해서 탐색을 실패하였다면, 
# (0, 4, 5)는 볼 필요가 없으니깐!

# 그리고, 차집합 연산을 위하여
# set로 형변환하여 list로 저장하겠습니다.
idx_pick_3_lst = [i for i in list(combinations(range(6), 3)) if 0 in i]
# 마음이 바뀌었어요. 왜냐. set로 했더니 계속 런타임 에러가 나서.

for test_case in range(1, T + 1):
    num_lst = list(map(int, input().strip()))
    
    result = 'false'
    for A in idx_pick_3_lst:
        B = [idx for idx in total_set if idx not in A]
        
        lst_a = [num_lst[i] for i in A]
        lst_b = [num_lst[i] for i in B]
        
        '''gpt가 내 14줄의 코드를 3 줄로 만들었어요.'''
        if (is_run(lst_a) or is_triple(lst_a)) and (is_run(lst_b) or is_triple(lst_b)):
            result = 'true'
            break
        
        '''if is_run(lst_a) is True:
            if is_run(lst_b) is True:
                result = 'true'
                break
            
            elif is_triple(lst_b) is True:
                result =  'true'
                break
            
        elif is_triple(lst_a) is True:
            if is_run(lst_b) is True:
                result = 'true'
                break
            
            elif is_triple(lst_b) is True:
                result = 'true'
                break'''
    
    print(f'#{test_case} {result}')
    