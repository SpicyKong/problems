# https://www.acmicpc.net/problem/2836 문제 제목 : 수상 택시 , 언어 : Python, 날짜 : 2020-05-08, 결과 : 성공
"""
    회고:
    아이디어를 구상하는데에는 그렇게 오래 걸리지 않았는데 코드를 구현하다 잠깐씩 생각하는 시간이 많았다..
    우선 이 문제의 입력중 a < b인 경우는 생각을 안해줘도 된다. 어차피 택시는 M으로 가야하니깐 말이다.
    그래서 나는 b > a인 경우일때만 배열에 추가하고 정렬을 해 주 었다. 그리고 이어져 있는(?) 모든 범위들의 길이를 결과값어 더해주면된다.
    이때 더해주는 값은 *2를 해줘야 한다. 갔다가 다시 방향을 틀어서 돌아와야 하니깐 말이다.

    사실 내일 소마 면접이다. 다른 분들처럼 스펙이 있는게 아니라 붙기는 힘들겠지만 동기부여를 받고 와야겠다.
"""
import sys

N, M = map(int, sys.stdin.readline().split())
list_graph = []
check = set()
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        list_graph.append([a, i])
        list_graph.append([b, i])
list_graph.sort()
start = list_graph[0][0]
result = M
for now, num in list_graph:
    if num in check:
        check.remove(num)
        if not check:
            result += (now - start)*2
    else:
        if not check:
            start = now
        check.add(num)
print(result)


"""
for now, num in list_graph:
    print(now, num, start)
    if num in check:
        check.remove(num)
        if not check:
            if not start == -1:
                result+=(now-start)*2
    else:
        check.add(num)
        start = now
        """
    
    

"""
3 10
3 1
4 2
8 6

6 10
0 2
3 1
4 2
4 9
7 10
8 6
"""
