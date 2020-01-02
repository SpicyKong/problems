# https://www.acmicpc.net/problem/18248 문제 제목 : 제야의 종 , 언어 : Python, 날짜 : 2020-01-01, 결과 : 실패
# 문제가 있따는것은 확실히 알겠는데 어디부터 손대야 할지 모르겟다..
# 테스트 케이스를 세우면서 테스트를 해보며 어떤 경우에서 문제가 생기는지 계속 관찰해봤다.
# 그냥 코드를 갈아 치웠다ㅋㅋ
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

# https://www.acmicpc.net/problem/18248 문제 제목 : 제야의 종 , 언어 : Python, 날짜 : 2020-01-02, 결과 : 성공
import sys

def Q_18248():
    N, M = map(int, sys.stdin.readline().split())
    people_sound_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    list_people_memo1 = [[0]*N for _ in range(N)] # 0 0 0 0처럼 자료 표현
    list_people_memo2 = [[] for _ in range(N)] # 이건 그냥 표현
    for i in range(M):
        New_list = []
        else_list = []
        test_list = [0]*N 
        for j in range(N):
            if people_sound_infos[j][i]:
                New_list.append(j)
                test_list[j] = 1
            else:
                else_list.append(j)
        for test in New_list:
            for people_priority in list_people_memo2[test]:
                if not test_list[people_priority]:
                    return "NO"
        #print(test_list)



        for last2first in else_list:
            for first2last in New_list:
                if not list_people_memo1[last2first][first2last]:
                    list_people_memo1[last2first][first2last] = 1
                    list_people_memo2[last2first].append(first2last)
    return "YES"
print(Q_18248())
