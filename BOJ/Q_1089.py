# https://www.acmicpc.net/problem/1089 문제 제목 : 엘리베이터 , 언어 : Python, 날짜 : 2020-05-21, 결과 : 실패
"""
    회고:
    원래는 시간초과가 나던 코드였는데 시간초과를 해결하려고 보니깐 틀렸습니다가 뜬다.. 총합을 구하고 평균내는 과정을
    좀 더 효율적으로 짤 수 있을거 같은데(사실 어떤 숫자가 불가능 하지 않는 부분도 조금 더 효율적으로 구상 할 수 있었지만)
    뭔가 안된다.. 쉬운 문제같았는데 못풀었다.

    떡꼬치 레시피
    고추장 : 물엿(or올리고당) : 설탕 : 간장 : 케첩 : 다진마늘
    = 1 : 3 : 1.5 : 0.5 : 2 : 1~2(취향) 여기에 msg조금 추가해도 좋다.
"""
import sys
def check(n):
    global check_list, list_map, N, list_num, list_count
    now_n = 4*n
    for num in range(10):
        add_token = 0
        for xy in check_list[num]:
            x = now_n + xy[0]
            if list_map[xy[1]][x] == '#':
                add_token = 1
                break
        if not add_token:
            #print(num)
            list_num[n].append(num*10**(N-1-n))
            list_count[n]+=1
    
#def get_sum(now_depth, now_sum):
#    global N, total, count, list_count, check_set
#    if now_depth == N:
#        if not now_depth in check_set:
#            count+=1
#            total+=now_sum
#        return
#    for next_num in list_count[now_depth]:
#        get_sum(now_depth+1, now_sum+next_num)
def get_sum():
    global list_num, list_count, N
    total = 0
    count = 0
    for k in range(N):
        for num in list_num[k]:
            for j in range(N):
                if k==j:
                    continue
                total+=list_count[j]*num
        count+=list_count[k]
    print(count, total)
    return total/count
    

def solve():
    global check_list, list_map, N, list_num, check_set, list_count
    N = int(sys.stdin.readline())
    list_num = [[] for _ in range(N)]#]][0]*N
    list_count = [0]*N
    check_list = [[(1, 1), (1, 2), (1, 3)], [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (1, 4)], [(0, 1), (1, 1), (1, 3), (2, 3)], [(0, 1), (1, 1), (0, 3), (1, 3)], [(1, 0), (1, 1), (0, 3), (1, 3), (0, 4), (1, 4)], [(1, 1), (2, 1), (0, 3), (1, 3)], [(1, 1), (2, 1), (1, 3)], [(0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (1, 4)], [(1, 1), (1, 3)], [(1, 1), (0, 3), (1, 3)]]
    list_map = [list(sys.stdin.readline().strip()) for _ in range(5)]
    check_set = set()
    [check(i) for i in range(N)]
    for c in list_num:
        if not c:
            print(-1)
            return
    print(get_sum())
solve()
"""
0
80
8
88
4

0
8
80
88

800
808
880
888

8000
8008
8080
8088

8800
8808
8880
8888

###.###.###.###
#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#
#.#.#.#.#.#.#.#
###.###.###.###



###.
..#.
###.
#...
###.

###.
..#.
###.
..#.
###.

#.#.
#.#.
###.
..#.
..#.

###.
#...
###.
..#.
###.

###.
#...
###.
#.#.
###.

###.
..#.
..#.
..#.
..#.

###.
#.#.
###.
#.#.
###.

###
#.#
###
..#
###



"""
