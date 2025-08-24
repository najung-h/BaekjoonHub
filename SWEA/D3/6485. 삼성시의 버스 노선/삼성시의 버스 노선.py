'''
완전탐색으로 했더니, 런타임 에러가 발생하여
gpt와 함께 최적화 진행하였습니다.
원래의 코드대로 하면 런타임 에러가 뜰 것이라 해서
누적합 리스트를 작성하고, 한 방에 반영하는 느낌으로 코드를 재작성했어요
'''

#import sys
#sys.stdin = open("input_6485.txt", "r")


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    ab_lst = [tuple(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C_tu = tuple(int(input()) for _ in range(P))
    
    ''' 
    <input>
    
    N(버스 노선의 개수) : 2
    ab_lst(i번째 버스 정보, a이상 b이하의 모든 정류장만을 다님) :  [(1, 3), (2, 5)]
    C_tu(P개의 버스 정류장에 대해 몇 개의 버스 노선이 다니는지?) :  (1, 2, 3, 4, 5)
    
    <output>
    print(f'#{test_case} ''.join(map(str, *bus_lst'))
    '''
    
    ''' 원래코드
    cnt = 0
    bus_lst = [0] * 5001 # 입력 크기를 고려하여 배열 미리 생성
    
    for ab in ab_lst:
        adx = ab[0] -1
        bdx = ab[1] -1
        
        for i in range(adx, bdx+1):
            bus_lst[i] += 1
    
    print(f'#{test_case} {" ".join(map(str, [bus_lst[C] for C in C_tu]))}')
    '''
    
    diff = [0] * 5002
    for A,B in ab_lst:
        diff[A] += 1
        diff[B+1] -= 1
        
    bus_lst = [0] * 5001
    runn = 0
    
    for i in range(1, 5001): # 인덱스 말고 버스 번호로 접근
        runn += diff[i]
        bus_lst[i] = runn
        
    print(f'#{test_case} {" ".join(str(bus_lst[C]) for C in C_tu)}')
