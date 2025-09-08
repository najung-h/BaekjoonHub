N = int(input())

big_arr = [list(map(int, input().split())) for _ in range(N)]

# print(big_arr)

# 뒷날부터 돌면서,
# 1. 상담이 가능하다면,
# 2. 누적합 저장
# 3. 새로운 가능 상담 일정이 나오면
# 4. 기존 누적합과 비교하면서 누적합 리스트 갱신

# dp[0] 은 버림. 
dp = [0] * (N+1)
# 상담 리스트
# cons = [False] * N

# (1 ≤ N ≤ 15)
# (1 ≤ 기간 Ti ≤ 5, 1 ≤ 금액 Pi ≤ 1,000)
for i in range(N-1, -1, -1):
    # 뒤에서부터 볼게요
    t, p = big_arr[i]
    # -1, -2, -3
     
    # 절대적 상담 가능  
    if i <= N-t:
        # 비교적 상담 가능(상담끼리 겹쳐서, 이익을 따져봐야한다.)
        # 겹치는 기간의 상담 다 취소해버리고
        # 지금 상담을 진행하는 이익이 크다면,
        dp[i] = max(p + dp[i + t], dp[i + 1])
    
    # 상담 불가능
    else:
        dp[i] = dp[i + 1]
        
print(dp[0])