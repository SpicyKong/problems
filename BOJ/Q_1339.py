# https://www.acmicpc.net/problem/1339 문제 제목 : 단어 수학 , 언어 : Python, 날짜 : 2020-02-28, 결과 : 성공
"""
  회고:
  오늘 마스크 구매하려고 다른 모니터에 마스크 판매 사이트를 왕창 켜두고 문제를 푸느냐 집중이 잘 안되었다.
  맨 처음 이 문제를 보고 각각의 계수를 어떻게 부여할까 생각을 했다. 그래서 맨처음 생각했던 방식은 높은 자릿수에 있는 자리수 별로 높은 계수를 부여하는
  생각을 해 보았지만 이리저리 생각해봐도 여러가지 고려해야할것이 참 많아 보였다.
  그래서 문자별로 계수를 더해둔 뒤 더해진 계수들을 기준으로 정렬하고 앞에있는 순서대로 9 8 7 ... 1을 곱해주는 방법을 생각하게 되었다.
  처음부터 이렇게 생각했으면 좋았을텐데
"""
import sys
N = int(sys.stdin.readline())
list_integer = [sys.stdin.readline().strip() for _ in range(N)]
word_count = [0 for i in range(26)]
for integer in list_integer:
    len_int = len(integer)
    count = 0
    for i in range(len_int-1, -1, -1):
        word_count[ord(integer[i])-65]+=10**count
        count += 1
a = 9
result = 0
for c in list(reversed(sorted(word_count))):
    result+=c*a
    if c == 0:
        break
    a-=1
print(result)
