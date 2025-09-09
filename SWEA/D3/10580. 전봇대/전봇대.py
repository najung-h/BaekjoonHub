#import sys
#sys.stdin = open('input_10580.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 전선의 개수
    '''교차점 발생 규칙
    1. 새로운 선
    - 기존의 시작점보다 더 높음
    - 기존의 도착점보다 더 낮음
    
    2. 새로운 선
    - 기존의 시작점보다 더 낮음
    - 기존의 도착점보다 더 높음
    
    3. 하나의 새로운 선에서 여러 개의 교차점이 발생할 수 있다
    (기존의 전선이 여러 개라면)

    N이 최악인 경우 1000개이므로, 약 500,000번
    충분히 가능하다.
    '''
    start_point = [0] * N
    end_point = [0] * N

    ans = 0

    for i in range(N):
        start_point[i], end_point[i] = list(map(int, input().split()))
        
        for j in range(len(start_point)):
            if start_point[j] > start_point[i] and end_point[j] < end_point[i]:
                ans += 1
            elif start_point[j] < start_point[i] and end_point[j] > end_point[i]:
                ans += 1
    
    print(f'#{tc} {ans}')


