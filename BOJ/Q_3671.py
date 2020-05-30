# https://www.acmicpc.net/problem/3671 문제 제목 : 산업 스파이의 편지 , 언어 : Python, 날짜 : 2020-05-30, 결과 : 성공
"""
    회고:
    그냥 평범한 DFS문제인데, 자꾸 틀렸다.. 그래서 질문글을 올리기 위해 주석을 달던 도중 set_check.add(0) 이 문장이 함수 호출 뒤에 있길레,
    순서를 바꾸어 주었더니 맞았다.. 왜 그런건지 모르겠다..

    몇일전 파이썬 중간고사를 보았다. 대충 이런 문제처럼 풀 수 있었다. 근데 실수를 했다. 가지치기를 안해서 수가 좀만 커져도 결과를 내지 못했다.
    멍청한 실수였다.. 물론 원래 문제를 dfs로 푸는것은 아니었지만 나름(?) 지식을 뽐내고 싶어서 + 바로 눈에 보인 방법이 그거여서 그렇게 풀었다.
    물론 내 잘못만 있는건 아니었지만, 내 실수가 있음은 분명했다. 무조건 100점이라 생각했던 파이썬 시험이 날아가버렸다.
    아쉽지만 지나갔다. 그래서 어제부터 하나의 새로운 규칙을 만들었다.
    백엔드를 위해 웹 프로그래밍 공부하기, 깃허브에 단순 커밋을 위해 1일 1알고 하지 않기(이게 은근 도움이 안되는것 같다.), 체계적으로 살기 등 여러가지 규칙을 정했다.
    오늘부터 실천중이다. 어쨋거나 그래서 오늘부터는 1일 1커밋을 지키지 않을수도 있을거 같다. 다만, 이제부터는 조금 더 개발자 스러운 활동들을 하기 위해
    노력해야겠다.
"""

import sys
def getNum(num, bit): # num: 현재 완성된 수, bit: 수 목록 중 사용된 수
    global result, lenN
    if not list_sosu[num]: # 현재 수가 소수라면 result를 +1해줌
        result+=1
    for i in range(lenN): # 숫자의 개수 만큼 반복
        if not bit>>i & 1: # i번째 숫자가 사용되지 않았다면(비트가 꺼져 있다면)
            if not (num*10+list_num[lenN-i-1] in set_check): # num*10+list_num[lenN-i-1] : 다음에 만들어 지는 수
                # 위에서 set_check는 방문 여부를 확인하는 set자료형
                set_check.add(num*10+list_num[lenN-i-1]) # 방문 체크
                getNum(num*10+list_num[lenN-i-1], bit | 1<<i) # 재귀
                

a = 10000000
# 에라토스 테네스의 체로 소수 목록  구해두기
list_sosu = [1]*2 + [0]*(a-2)
for i in range(2, int(a**0.5)+1):
    if not list_sosu[i]:
        k = 2
        while k * i < a:
            list_sosu[i*k]=1
            k+=1

T=int(sys.stdin.readline()) # 테스트 케이스의 수
for _ in range(T):
    set_check = set() # 방문 체크를 할 set 자료형
    result = 0 # 최종 결과
    N = sys.stdin.readline().strip() # 입력을 개행이 제거된 문자열 자료형으로 저장
    lenN = len(N) # 숫자의 개수
    list_num = list(map(int, list(N))) # 각각의 숫자를 사용하기 편하게 각각 int형으로 바꾸고 배열에 저장
    set_check.add(0)
    getNum(0, 0) # dfs 함수
    print(result) # 결과 출력
