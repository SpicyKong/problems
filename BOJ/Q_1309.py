# https://www.acmicpc.net/problem/1309 문제 제목 : 동물원 , 언어 : Python, 날짜 : 2020-02-16, 결과 : 성공
""" 
  회고:
  오늘은 내가 지금 하고있는 문제풀이의 효율성에대해 생각해보는 시간을 가졌었다.
  결론은 이렇다.
  1) 너무 오래 고민하지 말것.(안풀리면 다른분들의 AC코드를 힌트삼아 고민하는 시간을 가질것.)
  2) 좀더 기초적이고 대중적인 부분을 공부해볼것.(그래서 오늘은 DP문제를 풀어보았다.)
  3) 좀더 많이 풀어볼것.(하루 한 문제로 언제 따라잡겠나..)
  4) 종만북을 장식용으로 쓰지말것.ㅋㅋ
  5) 내가 공부하는 이유에 대해 좀더 생각해볼것.(코테? 대회? 무엇이든 지금처럼 해선 안된다.)
  
  세상은 넓다.
"""
import sys

N = int(sys.stdin.readline())
list_memo = [1,1,1]
while N-1 > 0:
    list_memo=[list_memo[0] + list_memo[1] + list_memo[2], list_memo[0] + list_memo[2], list_memo[0] + list_memo[1]]
    N -= 1
print(sum(list_memo)%9901)
