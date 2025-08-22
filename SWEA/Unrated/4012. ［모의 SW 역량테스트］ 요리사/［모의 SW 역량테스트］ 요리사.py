
'''완전탐색으로 구현해보겠습니다.'''
# ------------------------------------------------------
# [문제 요약]
# N개의 재료를 반반 나누어 두 요리를 만든다.
# 같은 음식 안에서 재료 (i,j)가 만나면 시너지 S[i][j]가 발생한다.
# 각 음식의 "맛"은 음식 내 모든 재료쌍의 시너지 합.
# 목표: 두 음식 맛의 차이를 최소화.
#
# [접근 방법]
# 1) 완전탐색: 모든 N/2 조합을 한 쪽 요리(A)로 선택
# 2) 나머지 재료로 다른 요리(B) 구성
# 3) 각각 맛 계산 후 차이 기록, 최소값 출력
# 4) (A,B)와 (B,A)는 중복이므로, 항상 0번 재료를 A에 넣어 절반만 탐색
# ------------------------------------------------------
 
 
from itertools import combinations
 
 
T = int(input())
 
 
for test_case in range(1, T+1):
    N = int(input())   #print(f'재료는 {N}개에요')
    big_arr = [list(map(int,input().split())) for _ in range(N)]
 
 
    # range(N) 이면 충분합니다.
    idx_all = range(N)
    '''idx_all = [0] * N
    for i in range(N):
        idx_all[i] = i
    # #print(idx_all) #[0, 1, 2, 3]'''
 
 
    min_synergy_diff = float('inf')
 
    for taste_A in (list(combinations(idx_all, N//2))):
        # 각 요리에 대한 경우에서 idx번째 경우를 데려옵니다. 예시 (0,1)
         
        if 0 not in taste_A:  
            # (A, B) 중복 제거: 0번을 A에 고정
            # 0이 없는 것은 taste_B에 포함되어 있으므로, taste_A로서 계산하지 않음
            continue
         
 
        taste_A_set = set(taste_A)   # membership 검사 빠르게 하기 위해 set 변환
        taste_B =   [i for i in idx_all if i not in taste_A_set]
 
        #print('taste_A 에 대한 정보에요.', taste_A)
        #print('taste_B 에 대한 정보에요.', taste_B)
 
 
 
 
 
        synergy = 0
        synergy_b = 0
 
        for rdx, cdx in combinations(taste_A, 2):
            synergy += big_arr[rdx][cdx] + big_arr[cdx][rdx]
 
        for rdx, cdx in combinations(taste_B, 2):
            synergy_b += big_arr[rdx][cdx] +  big_arr[cdx][rdx]
         
        #print(f'{taste_A_set}조합을 요리했더니 A요리는 맛이{synergy}가 났어요.')
        #print(f'{taste_A_set}조합을 요리했더니 B요리는 맛이{synergy_b}가 났어요.')
 
 
 
 
        synergy_diff = abs(synergy - synergy_b)
        #print(f'두 음식간 맛의 차이는 {synergy_diff}에요')
 
 
        if synergy_diff < min_synergy_diff:
            min_synergy_diff = synergy_diff
            #print(f'{max_food}조합을 요리했더니 {min_synergy_diff}가 났어요.')
 
 
        if min_synergy_diff == 0:
            # 최적값(0)이 나오면, 더 볼 필요가 없다.
            break
 
 
 
 
    print(f'#{test_case} {min_synergy_diff}')
    
 
    '''gpt의 코드리뷰
 
    1) 멤버십 검사는 tuple이 아니라 set에서 수행해야 간단하다.
    멤버십 검사가 필요하면 set을 써서 O(1)로.
 
    2) rdx, cdx는 전체 N * N으로 돌릴 필요가 없다.
    그룹 내 쌍만 돌리고, 맛은 S[i][j] + S[j+i]로 한번에 계산해라
 
    3) 중복 케이스 (A,B)와 (B,A)를 둘 다 탐색할 필요가 없다.
    이를 개선하기 위해서, 항상 0번 재료를 A에 포함시키면, 
    (A,B)만 보게 되어 탐색량이 절반으로 줄어든게 된다.
 
    4) 9999999999999 말고, float('inf')가 가독성이 좋다.
 
    5) 최적값(0)이 나오면, 더 볼 필요가 없다.
    '''

 