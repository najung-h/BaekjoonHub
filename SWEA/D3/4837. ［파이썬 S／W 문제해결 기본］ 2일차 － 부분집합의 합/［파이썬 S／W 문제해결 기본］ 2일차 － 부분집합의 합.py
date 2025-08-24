'''itertools를 이용해서 완전 탐색으로 풀겠습니당'''

A = list(range(1, 13))


from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    
    # 원소 변환이 없을 예정이므로 tuple로 담아올게요.
    subset_tuple = tuple(combinations(A, N))
    
    cnt = 0
    
    for subset in subset_tuple:
        if sum(subset) == K:
            cnt += 1
    
    print(f'#{tc} {cnt}')
            