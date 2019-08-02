# https://www.acmicpc.net/problem/2747 문제 제목 : 피보나치 수 , 언어 : Python, 날짜 : 20190802, 결과 : 성공

n = int(input())
dp_list = [0 for _ in range(n+1)]
def fi(num):
    if num == 0:
        dp_list[num] = 0
        return dp_list[num]
    elif num == 1:
        dp_list[num]=1
        return dp_list[num]
    else:
        if dp_list[num] > 0:
            return dp_list[num]
        else:
            dp_list[num] = fi(num-1) + fi(num-2)
            return dp_list[num]

print(fi(n))
