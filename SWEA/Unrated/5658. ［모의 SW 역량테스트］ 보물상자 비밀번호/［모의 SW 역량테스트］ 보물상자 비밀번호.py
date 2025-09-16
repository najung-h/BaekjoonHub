#import sys
#sys.stdin = open('input_5658.txt', 'r')

'''9시방향부터 시작해서, 시계방향으로 회전'''
'''어차피 n은 4의 배수니까. 그냥 rotate는 최대 n//4번 하지 않나? 

그걸 set에다가 add 하고,
마지막에 싹 다 십진수로 바꿔주고
list 형변환 -> sort 해서 K번째 원소를 print해주면 되겠는데요

rotate 자체는 q에서 append popleft해주면 되고
아니지 rotate가 아예 있었던 것 같은데
이거 그냥 백준 톱니바퀴 하위호환'''

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    q = deque(arr)
    
    num_set = set()
    
    for n in range(N//4):
        nq = q.rotate(1)
        
        for a in range(4):
            s, e = (N // 4) * a , (N // 4) * (a+1)
            num = ''.join(list(q)[s:e])
            num_set.add(num)
            #print(f'{a+1}번째 숫자는 {num}')
    
    num_lst = sorted([int(num, 16) for num in num_set])
    print(f'#{tc} {num_lst[len(num_lst) - K]}')