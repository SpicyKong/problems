# https://www.acmicpc.net/problem/1461 문제 제목 : 도서관 , 언어 : Python, 날짜 : 2020-03-14, 결과 : 실패
"""
    일기:
    오늘 소마 코테가 있었다. 자세한 문제내용을 언급할수는 없지만 많이 아쉽다.
    내가 평소 익숙하지 않았던 분야의 문제들도 나와서 속성으로 급하게 공부하느냐
    준비가 부족했던것 같다. 알고리즘 문제들도 있었는데 한가지를 못풀어서 많이 아쉽다.
    내년에는 제대로 준비해서 도전해야겠다.
"""
import sys
N, M = map(int, sys.stdin.readline().split())
list_inputs = list(map(int, sys.stdin.readline().split()))
list_minus = []
len_minus = 0
list_plus = []
len_plus = 0
while list_inputs:
    num = list_inputs.pop()
    if num >0:
        list_plus.append(num)
        len_plus+=1
    else:
        list_minus.append(num)
        len_minus+=1
list_minus.sort()
list_plus.sort()
m_point = len_minus%M
p_point = len_plus%M
count = M
result = 0
while list_minus:
    num = list_minus.pop()
    if count == M:
        result += abs(num)*2
    count -= 1
    if count == 0:
        count = M
count = p_point-1
while list_plus:
    num = list_plus.pop()
    if count == M:
        result += num*2
    count -= 1
    if count == 0:
        count = M
print(result-num)
'''
11 + 11
28 + 28
37 + 37
39
'''
#######################################################################
# https://www.acmicpc.net/problem/1461 문제 제목 : 도서관 , 언어 : Python, 날짜 : 2020-03-15, 결과 : 성공
"""
    회고:
    어제는 집중이 안되서 오늘 다시풀었다. 
    먼저 양수와 음수를 구분하고 각각의 리스트들을 정렬시켜주었다. 이때 음수는 내림차순으로 정렬시켜준다.
    음수를 내림차순으로 정렬시키면 가장끝 인덱스에는 절댓값이 가장 큰 값이 온다.
    그리고 M개의 책마다 result에 현재 책의 거리를 더해주면 거의 답에 근접하게 된다.
    하지만 문제의 조건에 명시되어 있듯이 마지막 책을 두고 시작지점인 0으로 돌아오지 않아도 된다고 있으므로
    가장 멀리 이동했던 값을 result에서 빼주면 된다.
"""
import sys
def go(list_a):
    global result
    count = M
    while list_a:
        num = list_a.pop()
        if num<0:
            num*=-1
        if count==M:
            result+=num*2
        count-=1
        if count==0:
            count=M
    
N, M = map(int, sys.stdin.readline().split())
list_inputs = list(map(int, sys.stdin.readline().split()))
list_minus = []
list_plus = []
result = 0
for num in list_inputs:
    if num > 0:
        list_plus.append(num)
    else:
        list_minus.append(num)
list_minus.sort(reverse=True)
list_plus.sort()
imsi_list = [0]
if list_minus:
    imsi_list.append(abs(list_minus[-1]))
if list_plus:
    imsi_list.append(list_plus[-1])
result-=max(imsi_list)

go(list_minus)
go(list_plus)
print(result)
