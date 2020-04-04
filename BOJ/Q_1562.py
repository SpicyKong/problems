# https://www.acmicpc.net/problem/1562 문제 제목 : 계단 수 , 언어 : Python, 날짜 : 2020-04-04, 결과 : 성공
"""
    회고:
    질문 게시판을 탐색하던중 문제 조건을 잘못본것을 알았다. 0~9까지 모두 한번이상 나온 수만 카운트해야했는데 그냥 모든 계단수를 카운트 해 버렸다.
    그리고 질문 게시판에서 우연히 비트마스킹이라는 큰 힌트를 얻었다.. 생각하지도 않았던 비트마스킹이라 너무 큰 힌트가 되었던것 같다.
    이 문제는 쉬운 계단수라는 문제에서 비트마스킹을 이용해 0~9까지 1번이상 나온 여부만 체크해주면 크게 어려운 부분은 없다.
    솔직히 점화식 부분은 너무 간단해서 왜 골드1이지? 라는 의문을 품었었는데, 알고보니 비트마스킹을 이용해야 했던 문제여서 그런가 보다.
    오랜만에 비트마스킹을 다시 상기 시켜보았던 좋은 문제인것 같다.

"""
import sys
N = int(sys.stdin.readline())
list_memo = [[[0]*((1<<10)+1) for i in range(10)] for _ in range(N)]
for num in range(1,10):
    list_memo[0][num][1<<num] = 1
count = 0
for n in range(N-1):
    for num in range(10):
        for bit in range((1<<10) + 1):
            if list_memo[n][num][bit]:
                count=max(count, list_memo[n][num][bit])
                if num == 0:
                    list_memo[n+1][num+1][bit|1<<(num+1)] += list_memo[n][num][bit]
                elif num == 9:
                    list_memo[n+1][num-1][bit|1<<(num-1)] += list_memo[n][num][bit]
                else:
                    list_memo[n+1][num-1][bit|1<<(num-1)] += list_memo[n][num][bit]
                    list_memo[n+1][num+1][bit|1<<(num+1)] += list_memo[n][num][bit]

print(sum([a[(1<<10)-1] for a in list_memo[-1]])%1000000000)
