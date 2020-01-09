# https://www.acmicpc.net/problem/1914 문제 제목 : 하노이 탑 , 언어 : Python, 날짜 : 2020-01-09, 결과 : 성공
# 하노이탑 알고리즘이 워낙 유명해서
# 간단할줄알았는데 머리가 굳어서 그런지 결국 인터넷을 찾아봤는데도
# 이해가 바로 되지않았다..
import sys
N = int(sys.stdin.readline())

def hanoi(n, now_pole, sup_pole, des_pole):
    if n == 1:
        print("asdf :",now_pole, des_pole)
        return
    hanoi(n-1, now_pole, des_pole, sup_pole)
    print("qwer :",now_pole, des_pole)
    #hanoi(1, now_pole, sup_pole, des_pole)
    hanoi(n-1, sup_pole, now_pole, des_pole)
print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)
