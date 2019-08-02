# https://www.acmicpc.net/problem/1463 문제 제목 : 1로 만들기 , 언어 : Python, 날짜 : 20190803, 결과 : 실패

n=int(input())
list_dp = [0 for _ in range(n+1)]
if len(list_dp)>2:
    list_dp[2]=1
if len(list_dp)>3:
    list_dp[3]=1
list_dp[n]=n
def dpf(num):
    test = []
    if num==1:
        return 0
    elif num==2:
        return 1
    elif num==3:
        return 1

    if num%2==0:
        if list_dp[int(num/2)] ==0:
            test.append(dpf(int(num/2)))
        else:
            test.append(list_dp[int(num/2)])
    if num%3==0:
        if list_dp[int(num/3)] ==0:
            test.append(dpf(int(num/3)))
        else:
            test.append(list_dp[int(num/3)])
    if num>3:
        if list_dp[num-1] ==0:
            test.append(dpf(num-1))
        else:
            test.append(list_dp[num-1])
    list_dp[num] = min(test) +1
    return list_dp[num]
    #print(list_dp)
print(dpf(n))
