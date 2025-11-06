import ast

T = int(input().strip())


for tc in range(1, T+1):
    func = list(input())
    # p가 최대 100000까지이면 되게 기네요.
    # RR이 연속해서 두 개나오면 의미없으니 무시하고,
    # R -> D로 바뀌는 순간이나 ,D->$R로 바뀌는 순간에만 카운트 해주면 된다.
    n = int(input().strip())
    lst = ast.literal_eval(input().strip())
    # 예외처리하다가 화나서 검색해봤는데, 이런 방법이 있대요
    '''lst = list(input().strip())
    lst = lst[1::2]
    lst = list(map(int, lst))'''
    # print(lst)
    # print(func)
    
    # 초기값 설정.
    is_reversed = 0
    start_idx = 0
    end_idx = n - 1
    is_errored = False
    
    for f in func:
        
        if f == "R":
            is_reversed = 1 - is_reversed 
            
        else:
            # 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
            if start_idx > end_idx:
                print("error")
                is_errored = True
                break
            if is_reversed:
                end_idx -= 1
            else:
                start_idx += 1
        
    if not is_errored: # 에러 아닌 경우에만 
        if not is_reversed:
            print("[" + ",".join(map(str, lst[start_idx:end_idx+1])) + "]")
        else:
            print("[" + ",".join(map(str, lst[start_idx:end_idx+1][::-1])) + "]")