# https://www.acmicpc.net/problem/2352 문제 제목 : 반도체 설계 , 언어 : Python, 날짜 : 2020-06-27, 결과 : 성공
"""
    회고:
    저번에 학교 기말 시험에 이 문제가 나왔다. 그래서 한번 풀어 보았다.
    분명 맨 처음에 떠올렸던 O(N^2)보다 빠른 코드가 있었던거 같았는데 잘 기억이 안나서 한번 다시 찾아보며 공부했다.
    알고리즘은 대충 이해했는데 소스코드를 구현하는데에 애먹었다.
    먼저 임시 리스트를 하나 만들어 lis의 정보를 저장하는데, 다음과 같이 저장한다. 
    list[i]는 길이가 i인 lis를 구할때 가장 끝에 오는 값이다. 그리고 이 정보를 최소화 시킬 수 있다면 최소화 시켜주면 된다.
    예를들어 4 5 1 2 3이라는 수가 있다고하면
    4
    4 5
    1 5
    1 2
    1 2 3
    이런식으로 갱신되는거다.

    정말 오랜만에 백준 사이트에 들어오고, vscode를 켜 문제를 풀어본다. 최근에 시험공부를 한다는 핑계로
    알고리즘을 안했는데, 시험공부는 무슨 매일매일 내일은 열심히 해야지만 하다가 기말고사가 끝나버렸다.
    진짜 역대급 한심한 한달이었던것 같다. 그래서 이제는 내일은 열심히 해야지가 아니라 지금이라도 열심히 하자로 바꾸려고 한다.
    우선 가장 첫번째 목표는 3일 내로 장고를 공부하면서 to do list사이트를 만들어볼것이다.
    이제 진짜 제대로 공부해야겠다. 시험도 망한거 같으니.
"""
import sys
def search(list_lis, count, num):
    s, e = 0, count
    while s<=e:
        if s == e:
            return s
        mid = (s+e)//2
        if list_lis[mid] == num:
            return mid
        elif list_lis[mid] < num:
            s=mid+1
        else:
            e=mid
    return -1

n = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))
#list_num = sorted([(i, num) for i, num in enumerate(list_num)], key=lambda x: x[1])
list_lis = []
count=0
for num in list_num:
    if not count:
        list_lis.append(num)
        count+=1
        continue
    if list_lis[count-1] < num:
        list_lis.append(num)
        count+=1
    else:
        list_lis[search(list_lis, count-1, num)] = num
print(count)
