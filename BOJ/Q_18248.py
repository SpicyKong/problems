# https://www.acmicpc.net/problem/18248 문제 제목 : 제야의 종 , 언어 : Python, 날짜 : 2020-01-01, 결과 : 실패
# 문제가 있따는것은 확실히 알겠는데 어디부터 손대야 할지 모르겟다..
import sys

def q_18248():
    N, M = map(int, sys.stdin.readline().split())
    list_sound = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    list_memo = [[] for _ in range(M)]
    list_check = [0]*(N)
    people_list = []
    people_num = 0
    for i in range(M): 
        wrong_list = []
        for j in range(N):
            if list_sound[j][i]:
                list_memo[i].append(j)
                if not list_check[j]:
                    wrong_list.append(j)
        if wrong_list:
            for people in people_list:
                if not people in list_memo[i]:
                    return "NO"
            people_list += wrong_list
            people_num += len(wrong_list)
        if people_num >= N:
            list_check = [0]*N
            people_list = []
            people_num = 0
    return "YES"

print(q_18248())
