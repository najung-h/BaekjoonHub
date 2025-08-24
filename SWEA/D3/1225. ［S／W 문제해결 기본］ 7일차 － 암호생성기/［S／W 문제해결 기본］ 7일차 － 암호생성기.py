from collections import deque


def one_cycle(que):
    
    ''' 연산의 종류를 리스트로 구성 '''
    minus_what_lst = [1, 2, 3, 4, 5]

    while True:
            
        for minus in minus_what_lst:

            left = que.popleft()
            if left-minus > 0:
                que.append(left-minus)
            
            else: #0이면
                que.append(0)
                return que






T = 10

for tc in range(1, T+1):
    TC = int(input())
    arr = list(map(int, input().split()))

    que = deque(arr)

    print(f'#{tc}',*one_cycle(que))
    #print(" ".join(map(str, one_cycle(que))))