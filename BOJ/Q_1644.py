# https://www.acmicpc.net/problem/1644 문제 제목 : 소수의 연속합 , 언어 : Python, 날짜 : 2020-04-09, 결과 : 성공
"""
    회고:
    맨 처음에는 DP로 풀려고 했지만 N의 범위가 너무 커 메모리 초과가 날것 같았다. 
    시간초과를 해결할 방법을 모색해봐도 보이지 않아서 결국 질문게시판을 이용했다. 거기에선 투 포인터라는 개념을 언급했다.
    투포인터알고리즘은 수열의 원소들이 자연수임이 보장될 경우에만 사용 가능한 알고리즘이다.
    알고리즘의 내용을 살펴보자면, 이 알고리즘 역시 수열의 구간합을 이용하지만 자연수의 수열의 합은 원소를 하나씩 늘려감에 따라
    당연히 구간합의 합이 늘어나는데 이를 이용한다. 투 포인터라는 이름답게 두개의 위치를 저장할 변수를 선언한다. 보통 s(start), e(end)로 사용하나보다.
    그리고 현재의 구간합이 우리가 목표로 하는 합보다 작다면 e라는 포인터의 값을 늘려 구간합의 범위를 늘리고 만약 같아지거나 커졌다면 s의 값을 늘려 다시 구간합을 줄인다.
    이 과정을 반복하면 구간합 중에서도 특히 우리가 원하는 합을 가지고있는 구간합을 구할 수 있다.
    신기하다.

    p.s.오늘 미분적분학에서 배우는 입실론 델타 논법에 대한 내용들을 공부했는데 아직 아리송 하다..
    특히 델타의 범위를 임의로 지정하는 풀이를 보고 나니 뭔가 더 아리송해진것 같다.

"""

import sys
N = int(sys.stdin.readline())
list_sosu = [0]*(4000000+1)
list_sosu[0]= 1
list_sosu[1]= 1
for num in range(2,int(4000000**0.5)+1):
    if not list_sosu[num]:
        i = 2
        while i * num <= 4000000:
            list_sosu[i * num] = 1
            i+=1
count = 0
list_result = []
for i in list_sosu:
    if not i:
        list_result.append(count)
    count += 1
start = end = 0
list_sosu = []
s=e=0
now_sum = 0
result = 0
while s < 283146 and list_result[s] <= N:
    if now_sum < N and e < 283146:
        now_sum+=list_result[e]
        e+=1
        continue
    
    if now_sum == N:
        result += 1
    
    now_sum-=list_result[s]
    s+=1
print(result)
