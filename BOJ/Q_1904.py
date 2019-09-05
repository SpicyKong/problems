# https://www.acmicpc.net/problem/1904 문제 제목 : 01타일 , 언어 : Python, 날짜 : 2019-09-05, 결과 : 실패

# 기본적인 dp문제인데 못풀었다.. 자소서쓰느냐 너무 바쁘다..
import sys
N = int(sys.stdin.readline())
N_1 = N//2
result = 0
def Modern_Life(num):
    num_a = 1
    for a in range(2,num+1):
        num_a*=a
    return num_a
result = 0
for a in range(N_1+1):
    N_2 = N-a*2
    #print
    result += Modern_Life(N_2+a)/(Modern_Life(a) * Modern_Life(N_2))
print(int(result%15746))
