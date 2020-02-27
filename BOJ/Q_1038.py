# https://www.acmicpc.net/problem/1038 문제 제목 : 감소하는 수 , 언어 : Python, 날짜 : 2020-02-27, 결과 : 성공
"""
    회고:
    어떻게 하면 시간초과를 해결할 수 있을까? 직접 시뮬돌리면 시간초과가 날거같아서 장애물은 리스트에 따로 저장해 두었는데
    아마도 insert하는 과정에서 시간초과가 나는것같다. 한번 다시 시도해봐야 할것같다.
"""

import sys
from collections import deque

def gravity(x,y):
    global list_ground, list_map
    #print("===")
    #[print(a) for a in list_map]
    for high in list_ground[x]:
        
        if y < high:
            #print("asdhjasdhkjasd")
            if high == R or list_map[high][x] == 'X':
                #print('a')
                #list_ground[x].appendleft(high-1)
                for k,num in enumerate(list_ground[x]):
                    if num >= high-1:
                        list_ground[x].insert(k,high-1)
                        break
                list_map[high-1][x] = 'O'
                break
            else:#elif list_map[high][x] == 'O':
                #print('b')
                #print("===")
                #[print(a) for a in list_map]
                #print(list_map[high-1][x-1], list_map[high][x-1])
                if x-1 >= 0 and list_map[high-1][x-1] == '.' and list_map[high][x-1] == '.':
                    #print("1")
                    gravity(x-1, high-1)
                elif x+1 < C and list_map[high-1][x+1] == '.' and list_map[high][x+1] == '.':
                    #print("2")
                    gravity(x+1, high-1)
                else:
                    
                    #print("===")
                    #[print(a) for a in list_map]
                    #print("3")
                    list_map[high-1][x] = 'O'
                    #list_ground[x].appendleft(high-1)
                    for k,num in enumerate(list_ground[x]):
                        if num >= high-1:
                            list_ground[x].insert(k,high-1)
                            break
                break
        





R, C = map(int, sys.stdin.readline().split())
list_ground = [[] for _ in range(C)]
list_map = []
count = 0
for k in range(R):
    input_map = list(sys.stdin.readline().strip())
    list_map.append(input_map)
    for i in range(C):
        if input_map[i] == 'X':
            list_ground[i].append(count)
        if k == R-1:
            list_ground[i].append(R)
    count += 1
N = int(sys.stdin.readline())
list_command = [int(sys.stdin.readline()) for _ in range(N)]
for command in list_command:
    #print("===")
    #[print(a) for a in list_map]
    gravity(command-1, 0)


#print("===")
[print(''.join(a)) for a in list_map]
#print(list_ground)
"""
5 4
....
....
.X..
....
....
4
2
2
2
2
2
2
"""
