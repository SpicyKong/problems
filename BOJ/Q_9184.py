# https://www.acmicpc.net/problem/9184 문제 제목 : 신나는 함수 실행 , 언어 : Python, 날짜 : 2019-12-28, 결과 : 성공
# 이 문제는 맨첨에 딕셔너리로 풀었다가 틀리길레 
# 리스트로도 메모이제이션을 해줬는데 안되서 멘붕왔다..
# 알고보니 출력형식을 지키지 않은것이였는데 거의 30분동안 삽질한거같다..


import sys

list_memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    global list_memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        list_memo[20][20][20] = w(20, 20, 20)
        return list_memo[20][20][20]

    elif list_memo[a][b][c] > 0: # a <= 20 and b<=20 and c<=20 and  
        return list_memo[a][b][c]

    elif a < b and b < c:
        list_memo[a][b][c-1] = w(a, b, c-1)
        list_memo[a][b-1][c-1] = w(a, b-1, c-1)
        list_memo[a][b-1][c] = w(a, b-1, c)
        return list_memo[a][b][c-1] + list_memo[a][b-1][c-1] - list_memo[a][b-1][c]

    else:
        list_memo[a-1][b][c] = w(a-1, b, c)
        list_memo[a-1][b-1][c] = w(a-1, b-1, c)
        list_memo[a-1][b][c-1] = w(a-1, b, c-1)
        list_memo[a-1][b-1][c-1] = w(a-1, b-1, c-1)

        return list_memo[a-1][b][c] + list_memo[a-1][b-1][c] + list_memo[a-1][b][c-1] - list_memo[a-1][b-1][c-1]
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w("+str(a)+", "+str(b)+", "+str(c)+")","=",w(a,b,c))

memo = {}
def w(a,b,c):
    global memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1


    if a > 20 or b > 20 or c > 20:
        test_s = w(20,20,20)
        memo[str([20,20,20])] = test_s
        return test_s
    
    elif str([a,b,c]) in memo:
        return memo[str([a,b,c])]
    elif a < b and b < c:
        test_a = w(a, b, c-1)
        test_b = w(a, b-1, c-1)
        test_c = w(a, b-1, c)
        memo[str([a, b-1, c-1])] = test_a
        memo[str([a, b, c-1])] = test_b
        memo[str([a, b-1, c])] = test_c
        
        return test_a + test_b - test_c
    else:
        test_d = w(a-1, b, c)
        test_e = w(a-1, b-1, c)
        test_f = w(a-1, b, c-1)
        test_g = w(a-1, b-1, c-1)
        memo[str([a-1, b, c])] = test_d
        memo[str([a-1, b-1, c])] = test_e
        memo[str([a-1, b, c-1])] = test_f
        memo[str([a-1, b-1, c-1])] = test_g
        return test_d + test_e + test_f - test_g
#d,f,g = map(int, sys.stdin.readline().split())
#print(w(d,f,g))

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w("+str(a)+", "+str(b)+", "+str(c)+")","=",w(a,b,c))
