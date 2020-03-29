# https://www.acmicpc.net/problem/1074 문제 제목 : Z , 언어 : Python, 날짜 : 2020-03-30, 결과 : 성공
"""
    회고:
    이 문제는 문제에서 나와있는대로 재귀적 성질을 이용하면 된다.
    간단히 말하자면 계속 테이블을 4등분 해서 생각하면 된다.
    1. 현재 위치가 몇사분면인지 체크 (이 문제를 풀때 만큼은 Z의 획순 대로 사분면을 체크했다.)
        1-1. 1사분면이면 암것도 안함
        1-2. 2사분면이면 2^(N-1)*1 만큼 결과를 더해줌.
        1-3. 3사분면이면 2^(N-1)*2 만큼 결과를 더해줌.
        1-3. 3사분면이면 2^(N-1)*3 만큼 결과를 더해줌.
        (이미 지나온 거리이므로 그냥 더해준다.)
    2. N을 1씩 줄여주면서 N이 0이 될때까지 반복한다.

    문제 자체는 간단한데 실수를 많이했다.ㅋㅋ 
    r을 빼야하는데 사분면을 체크할때 쓰는 True값을 뺀다던지, 2**(N-1)을 N**(2)-1이라고 쓴다던지..ㅠㅠ
"""

import sys
def return_harf(num,N):
    global count
    if 2**(N-1) <= num:
        return True
    else:
        return False
def where(c,r):
    if r and c:
        return 4
    elif not r and not c:
        return 1
    elif r:
        return 3
    else:
        return 2

N,r,c = map(int, sys.stdin.readline().split())
count = 0
while N > 0:
    block = 2**(2*N-2)
    test_r = return_harf(r,N)
    test_c = return_harf(c,N)
    sa_boon_myeon = where(test_c, test_r)
    if sa_boon_myeon == 2:
        count += block
        c-=2**(N-1)
    elif sa_boon_myeon == 3:
        count += block*2
        r-=2**(N-1)
    elif sa_boon_myeon == 4:
        count += block*3
        r-=2**(N-1)
        c-=2**(N-1)
    N-=1
print(count)
