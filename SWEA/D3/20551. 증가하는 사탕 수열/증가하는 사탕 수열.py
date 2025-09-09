def candy(A, B, C):
    # 절대적으로 불가능 -> -1 리턴
    if C < 3 or B < 2:
        return -1

    # 가능은 하다면, cnt 해보자.
    cnt = 0
    while B >= C:
        cnt += 1
        B -= 1

    while A >= B:
        cnt += 1
        A -= 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    A, B, C = list(map(int, input().split()))
    ans = candy(A, B, C)

    print(f'#{tc} {ans}')
