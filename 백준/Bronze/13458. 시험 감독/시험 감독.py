N = int(input()) # N개의 시험장
people_in_each_exam_room_lst = list(map(int, input().split()))
B, C = list(map(int, input().split()))

# 필요한 감독관 수의 최솟값
# 각각의 시험장에 총감독관은 오직 1명만, 
# 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수는 B명

# 하나의 시험장에 여러 명의 부 감독관이 있을 수 있으며, 
# 부감독관이 한 시험장에서 감시할 수 있는 응시자는 C 명,

'''문제 풀이 전략
B가 C보다 크다는 말이 아예 없음.

총 감독관을 무조건 둬야 하는 경우는
B > C 일때

B > C라면, 총감독관만큼을 빼주고, 나머지는 응시자//C+1

B<=C라면, 응시자 // C +1 

'''
# 디버깅
#print(f'{N}개의 시험장이 있어요. 총감독관은 {B}명을 감시할 수 있고, 부감독관은 {C}명을 감시할 수 있어요.')
''' 총감독관이 무조건 1 명 이상 들어가야 한다는 규칙이 있나봐요. 그것 고려하면 바로 통과됨.'''


'''if B>=C : '''
supervisor = 0
for room in people_in_each_exam_room_lst:
    #print(f'{room}명 중에 {B}명은 총감독관이 감시할거라 {room-B}명만 부감독관이 감시하면 돼요. 즉, 부감독관이 {(room-B)//C}명 필요해요.')
    supervisor += 1
    room -= B
    if room > 0:
        supervisor += (room + C -1 ) // C

        
'''else: 
    supervisor = 0
    for room in people_in_each_exam_room_lst:
        supervisor += room // C +1'''

print(supervisor) 


'''gpt의 코드리뷰
1) 아래와 같은 코드는 '(room + C -1 ) // C' 를 이용해서 안전하게 고치는 것이 좋다.

    <기존>
    if room > 0 and room // C != room/C:
        supervisor += room // C +1
    else:
        supervisor += room // C
        
    <또는 변경 방법 2>
    if room > 0:
    q, r = divmod(room, C)
    ans += q + (1 if r else 0)
        
'''