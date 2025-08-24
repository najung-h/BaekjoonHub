
'''
deque를 이용해서 구현했습니다.

왼쪽이 출구고 오른쪽이 입구라고 생각했을 때

매번 que의 가장 왼쪽 원소를 빼서 반 녹여주고,

다 녹았다면 새로운 원소를 오른쪽으로 넣어줬습니다.

다 녹지 않았다면, 기존의 원소를 다시 넣어줬습니다.

que의 길이가 1이 되었다면, 남아있는 애를 출력해주었습니다.

'''

from collections import deque

T = int(input())


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ##print('arr에요 : ', arr)  #[7, 2, 6, 5, 3]
    new_arr = [[0,0] for _ in range(M)]
    
    for idx, i in enumerate(arr):
        new_arr[idx][0] = idx
        new_arr[idx][1] = i

    ##print('new_arr에요 : ', new_arr)
    #  [[0, 7], [1, 2], [2, 6], [3, 5], [4, 3]]

    que = deque(new_arr[:N])

    new_pizza_cnt = 0

    while True:
        
        #print('현재 화덕 안에는 : ', que)
        now_pizza = que.popleft()
        #print('방금 막 한바퀴 돌은 피자 : ', now_pizza)
        now_pizza = [now_pizza[0], now_pizza[1] //2]
        #print('녹음 처리: ', now_pizza)


        if now_pizza[1] ==0:
            # 피자가 녹았어
            # 이제 (가능하다면) 다음 피자 넣고 
            #print('피자가 다 녹았어.')
            if new_pizza_cnt < M-N :
                que.append(new_arr[N+new_pizza_cnt])
                new_pizza_cnt += 1
                #print('새로운 것을 넣어보니, 현재 화덕 안에는 : ', que)
        
        else:
            # 아직 피자가 덜 녹았어. 
            #print('피자가 덜 녹았어. 더 돌리자')
            # 다시 넣고
            que.append(now_pizza)
            # 한 바퀴 더 돌려야해
            #print('다시 넣고 돌리니, 현재 화덕 안에는 : ', que)


        if len(que) == 1:
            print(f'#{tc} {que[0][0]+1}')
            break


        


    