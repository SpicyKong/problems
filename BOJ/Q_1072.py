# https://www.acmicpc.net/problem/1072 문제 제목 : 게임 , 언어 : Python, 날짜 : 2020-01-24, 결과 : 성공
# 약간 꼼수로 그냥 우직하게 반복문돌려서 풀었다ㅋㅋ
import sys
X, Y = map(int, sys.stdin.readline().split())
# 승률 = int(Y/X*100)
win_rate_first = int(Y*100/X)
if win_rate_first >= 99:
    print(-1)
else:
    count = 100
    while win_rate_first == int((Y + count)*100/(X + count)):
        count += 100
    for i in range(count - 100 + 1, count + 1):
        if not int((Y + i)*100/(X + i)) == win_rate_first:
            print(i)
            break
