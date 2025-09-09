#import sys
#sys.stdin = open('input_20551.txt', 'r')


def candy(A, B, C):
    # 절대적으로 불가능 -> -1 리턴
    if C < 3 or B < 2:
        return -1

    # 가능은 하다면, cnt 해보자.
    # cnt 1 은 B를 먹는 개수
    # cnt 2 는 A 를 먹는 개수
    cnt = 0

    if B >= C:
        cnt1 = B - C +1
        cnt += cnt1
        B -= cnt1

    if A >= B:
        cnt2 = A - B +1
        cnt += cnt2
        A -= cnt2

    return cnt

T = int(input())
for tc in range(1, T+1):
    A, B, C = list(map(int, input().split()))
    ans = candy(A, B, C)

    print(f'#{tc} {ans}')
