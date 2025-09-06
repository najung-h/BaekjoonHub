N = int(input())
score = [0]
for i in range(N):
    score.append(int(input()))
# print(score_lst)
# 동적 프로그래밍 사용하겠습니다

# 시작점은 계단이 아님
# 각 계단까지의 최소 거리를 구하되,  


if N == 1:
    print(score[1])
elif N == 2:
    print(score[1] + score[2])
else:
    # dp i번째 원소의 의미는 i번째 계단까지 가기 위한 

    dp = [0] * (N + 1)
    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + score[i],
                    dp[i - 3] + score[i - 1] + score[i])

    print(dp[N])