# https://www.acmicpc.net/problem/12015 문제 제목 : 가장 긴 증가하는 부분 수열 2 , 언어 : Python, 날짜 : 2020-03-29, 결과 : 성공
"""
    회고:
    드디어 아주 유명한 LIS문제를 접해보았다. 물론 저번에 한번 쉬운문제를 접해본적이 있지만,
    그때의 DP알고리즘은 시간복잡도가 N^2이라 이 문제에선 시간초과가 난다. 그래서 도저히 어떻게 풀어야할지 감이 안잡혀서
    또 풀이를 참고했다. 우선 이 알고리즘의 시간복잡도는 NlogN이라고 한다.
    알고리즘은 이렇다.
    1. 수열을 만들어둘 배열을 하나 만들어 둔다.
    2. 입력받은 값들을 하나씩 탐색한다.
        2-1. 현재 탐색중인 값이 수열의 마지막 값보다 크다면 수열의 마지막에 push해준다.
        2-2. 작다면 이분탐색을 한 뒤 현재 탐색중인 값보다 큰 값중 가장 작은값의 위치에 덮어씌운다(?).
        2-3. 같다면 아무행동 안한다.
    3. 이렇게 해서 완성된 수열의 최종 길이는 LIS의 길이와 같다고 한다.
    
    한가지 문제점은 솔직히 3번의 결론이 직관적으로 와닿지가 않는다. 왜 그런건지 공부좀 해봐야겠다.
    그래도 이 문제를 풀면서 LIS의 개념과 이분탐색을 상기시켜보았다. 좋은 문제인것 같다.
"""

import sys


def binary_search(num):
    global list_s,count
    start = 0
    end = count-1
    while start <= end:
        index = (start + end)//2

        if list_s[index] > num:
            end = index - 1
        elif list_s[index] < num:
            start = index + 1
        else:
            return index
    if list_s[index] > num:
        return index
    return index+1

N = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))
list_s = [-1]
count = 0

for num in list_num:
    if list_s[-1] < num:
        list_s.append(num)
        count += 1
    elif list_s[-1] > num:
        list_s[binary_search(num)] = num
print(count)
