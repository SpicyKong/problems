# https://www.acmicpc.net/problem/1107 문제 제목 : 리모컨 , 언어 : Python, 날짜 : 2019-12-05, 결과 : 실패
# ㄴ아ㅣ롼ㄹ오ㅓㅏㅣㄴㅇ로ㅓㅏㅣ넝라ㅣㅓㄴㅇ라ㅣㅓㄴㅇ리ㅏㅏㅣㄴㄹ어ㅏㅣㄴㅇ러ㅏㄴㄹ어ㅣㅏ
# 난 웰케 코딩을 못하는건지
# https://www.acmicpc.net/problem/1107 문제 제목 : 리모컨 , 언어 : Python, 날짜 : 2019-12-07, 결과 : 성공
# 시행착오끝에 문제를 맞추긴했지만 코드의 상태를 보면 매우찝찝하다..


import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
list_buttons = [1] * 10
result = 0

if M > 0:
    for a in sys.stdin.readline().split():
        list_buttons[int(a)] = 0

search  = 1 # 바로 채널을 검색할수있는지 체크
for a in str(N):
    search *= list_buttons[int(a)]




if N == 100: # 만약에 현재 채널인 100이 입력으로 주어졌다면
    print(0)
else: # 이외
    end = 0
    for i in range(1,N+1+100):
        num_plus = N + i
        num_minus = N - i
        B_for1 = 0
        B_for2 = 0

        if num_minus == 100 or num_plus == 100:
            result = abs(N - 100)
            break

        for j1 in str(num_plus):
            if not list_buttons[int(j1)]:
                B_for1 = 1
                break
        if not B_for1:
            result = len(str(num_plus)) + abs(N - num_plus)
            end = 1
            
        
        
        if num_minus >= 0:
            for j2 in str(num_minus):
                if not list_buttons[int(j2)]:
                    B_for2 = 1
                    break
            if not B_for2:
                result = len(str(num_minus)) + abs(N - num_minus)
                end = 1
        if end:
            break
        #print(num_minus, num_plus)
    result = min(result, abs(100-N))
    if search: # 만약에 바로 검색이 가능한 채널이라면
        result = min(len(str(N)), result)
    print(result)
