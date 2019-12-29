# https://www.acmicpc.net/problem/1837 문제 제목 : 암호제작 , 언어 : Python, 날짜 : 2019-12-29, 결과 : 성공
# 문제의 조건을 잘 
import sys
def find(num):
    list_sosu = [1]*(num+1)
    num_a = int(num**0.5) + 1
    for i in range(2, num+1):
        if list_sosu[i]:
            n=2
            while i*n <= num:
                list_sosu[i*n] = 0
                n+=1
    return [i for i in range(1,num+1) if list_sosu[i]]

def Is_good():
    P, K = map(int, sys.stdin.readline().split())
    for i in find(K-1):
        if not i == 1 and not i == 0 and P%i == 0:
            print("BAD", i)
            return
    print("GOOD")
    return
Is_good()
