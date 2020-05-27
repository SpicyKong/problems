# https://www.acmicpc.net/problem/2140 문제 제목 : 지뢰찾기 , 언어 : Python, 날짜 : 2020-05-27, 결과 : 성공
"""
    회고:
    구현 문제가 뭔가 재미있는것 같아서 풀어보았다. 이 문제는 간단하다.
    우선 입력으로 주어지는 모서리의 값을 이용해 차례대로 탐색해 나가면 되는 문제다.
    아 그리고 다른 분들 코드를 보니깐 지뢰의 관점?에서 탐색하는 코드도 있었지만
    나는 그냥 숫자를 이용해 탐색해 나갔다.
    1. 0,0부터 사각형의 모서리를 시계방향으로 탐색한다.
    2. 만약 숫자가 0이면 주위의 '#'을 모두 'X'로 바꾼다.
    3. 만약 숫자가 0이 아니면 주위의 'X'개수를 모두 확인한 뒤 지뢰가 더 있다고 판단하면 지뢰를 채워나간다.
    아 그리고 열려있지 않은 부분의 영향이 안가는 가운데 부분은 모두 채워져 있다고 생각한다.(지뢰의 최대값을 구해야하므로)

    오늘 조개 2kg을 주문했다. 봉골레를 만들어 먹어야겠다. 그리고 오늘 된장찌개를 끓여봤는데
    맛있었다.
"""
import sys

def solve():
    global N
    N = int(sys.stdin.readline())
    list_map = [list(sys.stdin.readline().strip()) for _ in range(N)]
    if N <=2:
        print(0)
        return
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    if N-4>0:
        result = (N-4)**2
    else:
        result = 0
    x, y = 0, 0
    list_next = []
    for i in range(4):
        for j in range(N-1):
            count = int(list_map[y][x])
            for cx, cy in ((1,-1), (1,0), (1,1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):
                nx = x+cx
                ny = y+cy
                if 0<=nx<N and 0<=ny<N:
                    if list_map[ny][nx]=='#':
                        list_next.append((nx, ny))
                    elif list_map[ny][nx]=='O':
                        count-=1
            

            while list_next:
                nx, ny = list_next.pop()
                if count > 0:
                    list_map[ny][nx] = 'O'
                    result += 1
                    count -= 1
                else:
                    list_map[ny][nx] = 'X'

            x+=dx[i]
            y+=dy[i]
    print(result)
    #[print(a) for a in list_map]
                    

            
solve()
"""
3
000
0#0
000
1110
1##1
1##1
0111

1221
2##2
2##2
1221

5

0112110
0#.#.#1
1####.2
1.###.3
2####.3
1.###.2
1110111

0112110
0#####1
1#####2
1#####3
2#####3
1#####2
1110111

7
0111000
0#####0
0#####1
0#####1
0#####1
0#####0
0111000
"""
