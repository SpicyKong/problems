# https://www.acmicpc.net/problem/1660 문제 제목 : 캡틴 이다솜 , 언어 : Python, 날짜 : 2019-10-13, 결과 : 실패
# 아래에 성공 코드가 있다.
# 틀린 이유 : dp로 풀어야 했는데 그리디알고리즘을 사용했다.
#             고쳐야하는데 낼모레가 모의고사다..
import sys

N = int(sys.stdin.readline())
need_list = [0,1]
dp_list = [1]*(N+2)

n=2
count = 0
while need_list[n-1] < N:
    need_list.append(need_list[-1] + n*(n+1)//2)
    n+=1
print(need_list)
"""
while N:
    if need_list[n-1] < N:
        need_list.append(need_list[-1] + n*(n+1)//2)
        n+=1
    else:
        while need_list[n-1] > N:
            n-=1
        N-=need_list[n-1]
        count += 1
"""
print(count)

"""
N = int(sys.stdin.readline())
need_list = [0,1]# + [0]*(N-1)
n=2
count = 0
while N:
    if need_list[n-1] < N:
        need_list.append(need_list[-1] + n*(n+1)//2)
        n+=1
    else:
        while need_list[n-1] > N:
            n-=1
        N-=need_list[n-1]
        count += 1
print(count)
1 4 10 20

1 1+2 1+2+3 1+2+3+4
1 1+3 1+3+6 1+3+6+10
dp[n] = dp[n-1] + n(n+1)/2 

"""

# https://www.acmicpc.net/problem/1660 문제 제목 : 캡틴 이다솜 , 언어 : Python, 날짜 : 2019-12-22, 결과 : 성공
# 최근 풀었던 dp문제의 유형이 모두 비슷한것같다. 별다른 검색없이 몇가지 테스트케이스를 직접 만들어보며 풀었다!
# 위의 예전에 짠 코드를 보니 성장한 느낌이 든다ㅋㅋ
# 아 도움을 받은 부분이 있는데 질문게시판에서 동전과 유사하게 생각하면 된다는 글이 접근법을 생각할때 크게 도움이 되었다.
import sys
N = int(sys.stdin.readline())
list_depo = [1]
list_dp = [0] * (N+1)
list_dp[1] = 1
for i in range(2, N+1):
    count_depo = i*(i+1)//2 + list_depo[-1]
    if count_depo <= N:
        list_depo.append(count_depo)
#print(list_depo)
for i in range(N+1):
    for j in list_depo:
        if i + j <= N:
            if list_dp[i+j] == 0:
                list_dp[i+j] = list_dp[i] + 1
            elif list_dp[i+j] > list_dp[i] + 1:
                list_dp[i+j] = list_dp[i] + 1
print(list_dp[-1])



