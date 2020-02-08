# https://www.acmicpc.net/problem/5046 문제 제목 : 전국 대학생 프로그래밍 대회 동아리 연합 , 언어 : Python, 날짜 : 2020-02-08, 결과 : 성공
# 바쁜하루. 오랜만에 고등학교 친구들과 만났다.

import sys

N, B, H, W = map(int, sys.stdin.readline().split())
list_price = []
list_info_weeks = []
for _ in range(H):
    list_price.append(int(sys.stdin.readline()))
    list_info_weeks.append(list(map(int, sys.stdin.readline().split())))
result = 500001
for hotel in range(H):
    for week in list_info_weeks[hotel]:
        if week >= N and result > N*list_price[hotel] and N*list_price[hotel] <= B:
            result = N*list_price[hotel]
if result==500001:
    print('stay home')
else:
    print(result)
