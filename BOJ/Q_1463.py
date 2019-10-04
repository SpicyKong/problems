# https://www.acmicpc.net/problem/1463 문제 제목 : 1로 만들기 , 언어 : Python, 날짜 : 2019-08-03, 결과 : 실패
# https://www.acmicpc.net/problem/1463 문제 제목 : 1로 만들기 , 언어 : Python, 날짜 : 2019-10-04, 결과 : 성공
#-----------두번째 시도 코드(맞은 코드)------------#

X = int(input())
list_a = [0]*(X+1)
#print(len(list_a))
count = 1
while True:
    if count+1 <= X:
        if not list_a[count+1]:
            list_a[count+1] = list_a[count]+1
        elif list_a[count]+1 < list_a[count+1]:
            list_a[count+1] = list_a[count]+1
    if count*2 <= X:
        if not list_a[count*2]:
            list_a[count*2] = list_a[count]+1
        elif list_a[count]+1 < list_a[count*2]:
            list_a[count*2] = list_a[count]+1
    if count*3 <= X:
        if not list_a[count*3]:
            list_a[count*3] = list_a[count]+1
        elif list_a[count]+1 < list_a[count*3]:
            list_a[count*3] = list_a[count]+1
    if count == X:
        break
    count+=1
print(list_a[X])

#-----------첫시도 코드(틀린 코드)------------#
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
