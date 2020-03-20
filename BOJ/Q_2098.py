# https://www.acmicpc.net/problem/2098 문제 제목 : 외판원 순회 , 언어 : Python, 날짜 : 2020-03-20, 결과 : 성공
"""
    회고:
    이 문제도 정답코드를 참고했다. 일단 내가 이해한 코드의 흐름은 이렇다.
    1. 출발점은 0으로 정한다. (어차피 사이클이므로 어느정점에서 시작해도 상관없다.)
    2. (현재위치, 방문했던장소들)을 인자로 가지는 TSP함수를 만든다. (이때 방문했던 장소를 비트마스크를 이용하면 된다.)
        2-1. 만약 모든 정점을 방문했다면 현재정점에서 0으로 가는 비용을 추가한뒤 반환, 만약 경로가 없다면(가는 비용이 0이면 경로가 없음) 아주 큰값을 반환해 최소값으로 선택이 안되게 한다.
        2-2. 만약 list_memo[현재정점][지나온경로]의 값이 존재하면 탐색을 종료하고 저장된 값을 반환(메모이제이션을 한 이유다)
        2-3. 현재 정점에서 갈수있는 경로들을 탐색하고 탐색이 완료된 경우에 메모이제이션한다.
    
    아직은 완벽히 내 코드인 느낌이 들지는 않는다..ㅠㅠ 특히 자꾸만 이상하게도 재귀함수는 햇갈린다. 열심히 공부해서 내 코드로 만들어야 겠다.
    그동안 리스트를 선언해서 체크하던것들을 비트마스킹을 배우니 정수하나로 표현하는것들을 보면 정말 신기하다.
"""
import sys
N = int(sys.stdin.readline())
chech_end = (1 << N) - 1
list_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
list_memo = [[0]*(1 << N) for _ in range(N)]

#list_stack = [[i,0,0] for i in range(1,N)]

def TSP(now_num, now_visit):
    global list_map, list_memo, N
    #print('asdhjdashjkasdhk')
    now_visit |= (1 << now_num)
    if now_visit == chech_end:
        if list_map[now_num][0] > 0:
            return list_map[now_num][0]
        else:
            return 22222222222222222
    if list_memo[now_num][now_visit]:
        return list_memo[now_num][now_visit]
    ret = 22222222222222222
    for i in range(N):
        if not i == now_num and not (now_visit >> i & 1) and list_map[now_num][i] > 0:
            temp = TSP(i, now_visit) + list_map[now_num][i]
            if temp < ret:
                ret = temp
                list_memo[now_num][now_visit] = ret
    return ret
print(TSP(0,0))
