# https://www.acmicpc.net/problem/2688 문제 제목 : 줄어들지 않아 , 언어 : Python, 날짜 : 2020-03-05, 결과 : 성공

"""
    회고:
    오늘부터 알고리즘 수련에 들어갈거다. 소마 코테를 준비해야하기 때문이다. 이번에는 내가 스펙이 없어서
    붙을 확률은 높지 않겠지만 그래도 후회하고 싶지도 않고 코테의 과정 자체가 좋은 과정일것 같아서 준비해보기로 했다.
    DP는 언제나 새롭다. 이 문제도 다른분의 아이디어를 보고나서야 풀게되었다. 그전에 코드를 짜면서
    거의 비슷한 생각을 하고있었는데 상상중인 방법을 구현하지 못하고 결국 아이디어를 빌리게 되었다..
    앞으로는 찰나의 생각들 조차도 곱씹어보는 생각을, 안되면 필기도 시도해보며 공부를 시작해봐야겠다.
"""
import sys

list_memo= [[0]*10 for _ in range(65)]
list_memo[1] =[1]*10
for i in range(2,65):
    for j in range(10):
        for k in range(j,10):
            list_memo[i][k] += list_memo[i-1][j]

T = int(sys.stdin.readline())
for _ in range(T):
    print(sum(list_memo[int(sys.stdin.readline())]))
