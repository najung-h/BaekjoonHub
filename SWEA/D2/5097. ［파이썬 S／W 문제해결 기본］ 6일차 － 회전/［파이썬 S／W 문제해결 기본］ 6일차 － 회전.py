'''
뒤에 있는 걸 앞으로 데리고 오는 게 M이고

앞에 있는 걸 뒤로 보내는 게 -M이라는 것을 이용했습니다.
'''

from collections import deque


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr = deque(arr)
    
    arr.rotate(-M)


    print(f'#{tc} {arr[0]}')


    '''gpt의 조언
    N이 20 이하이고 M이 최대 1000이므로 rotate를 그냥 써도 충분히 빠릅니다.
    하지만 최적화하려면 M % N만큼만 회전해도 결과가 같아요:
    arr.rotate(-(M % N))

    '''