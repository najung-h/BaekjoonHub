#import sys
#sys.stdin = open('input_5643.txt', 'r')

'''노드 각각에서 출발했을 때, 
모든 노드를 탐색할 수 있으면 됨
굳이 무향 / 유향 노드를 구분할 필요도 없음

아니네, 구분해야하네 ㅎㅎ

런타임 에러가 나서, dfs를 하나로 합쳐봤습니다.

그런데도 아직 5 / 15이라서

dfs 구현법을 바꿨습니다.
'''

from collections import deque

def dfs(start_node, lst):
    stack1 = deque()
    # 나 보다 큰 애 누구?

    # 첫 번째 노드 방문 처리 후 스택에 삽입
    visited = [0] * (N+2)
    visited[start_node] = 1

    # 굳이 경로를 추적할 필요 없이, 방문 여부만 확인하면 됨.
    stack1.append((start_node))

    while stack1:
        current_node = stack1.pop()
        # print('스택에서 노드를 꺼내봅시다 : ', current_node)

        # 나보다 큰/작은 놈 찾기
        for new_node in lst[current_node]:
            if not visited[new_node]:
                visited[new_node] = 1
                stack1.append((new_node))
                # print('다시 넣을게요 : ', new_node + [new_node])

    return visited.count(1)
    # 혹시나 나보다 다 크다면, 난 꼴등이야. 종료/



T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 노드의 개수
    M = int(input())  # 간선의 개수

    # 입력 받으면서 바로 노드 정보 채우기
    node_info_lst = [[] for _ in range(N+1)]
    node_info_lst_reverse = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = list(map(int, input().split()))
        node_info_lst[a].append(b) # 작은 친구에서 큰 친구로 이어지게끔 설정.
        node_info_lst_reverse[b].append(a)  # 큰 친구에서 작은 친구로 이어지게끔 설정.

    # print(node_info_lst)  
    # print(node_info_lst_reverse)

    # [[], [5], [], [4], [2, 6], [4, 2], []]
    # [[], [], [4, 5], [], [3, 5], [1], [4]]

    result_cnt = 0

    for n in range(1, N+1):
        if dfs(n, node_info_lst) + dfs(n, node_info_lst_reverse) > N:  #start_node가 중복으로 되어있으니까 등호 허용 x
            result_cnt += 1
    

    print(f'#{tc} {result_cnt}')