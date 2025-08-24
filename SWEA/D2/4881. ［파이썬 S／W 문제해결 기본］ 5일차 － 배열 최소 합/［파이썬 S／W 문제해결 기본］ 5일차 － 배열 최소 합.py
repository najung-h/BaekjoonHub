'''완전탐색 - 순열로 구현하겠습니다.'''

from itertools import permutations


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    idx_all = list(range(N))

    min_sum = float('inf')


    for case in permutations(idx_all, N):
        #print(f'이번에 각 행마다 더할 원소는 각각 {case}번째입니다.')
        now_sum = 0


        for rdx in range(N):
            now_sum += big_arr[rdx][case[rdx]] 
            #print(f'{rdx}행에서 {big_arr[rdx][case[rdx]] }더할게요.')

            '''아래의 if문(백트래킹 코드)를 넣지 않아도 답은 정상적으로 구할 수 있습니다.
            다만, 시간 초과가 나기 때문에 제출시에는 필수적으로 구현해야 합니다.'''
            if now_sum >= min_sum:   # 백트래킹 하나
                break

        if now_sum < min_sum:
            min_sum = now_sum
      

    print(f'#{test_case} {min_sum}')