# https://www.acmicpc.net/problem/11652 문제 제목 : 카드 , 언어 : Python, 날짜 : 2020-02-14, 결과 : 성공
# 오늘부터 문제를 풀어보면 회고를 적는 시간을 가져야겠다.

""" 
회고 : 
1. 딕셔너리를 이용해 새로운값이면 추가한다. 기존에 있었다면 +1 해준다.
2. 카드개수의 최댓값을 저장해둔다
3. 문제의 조건인 카드의 개수가 같을경우 더 작은값을 출력해야하므로 한번 dict_nums를 루프를 통해 검사한다.
4. result와 같은 빈도수의 더작은카드가 있다면 갱신한다.

파이썬의 딕셔너리는 반칙인것 같다..
이 문제는 카테고리 분류에는 정렬이라고 되어있었는데 정렬로도 풀어봐야겠다.
"""

import sys
dict_nums = {}
result = 0
N = int(sys.stdin.readline())
for _ in range(N):
    num_now = int(sys.stdin.readline())
    try:
        dict_nums[num_now]+=1
    except:
        dict_nums[num_now]=1
    
    
    if dict_nums[num_now] > result:
        result = dict_nums[num_now]
#print(result)
result_num = 0
token = 0
for num in dict_nums:
    if not token and result == dict_nums[num]:
        result_num = num
        token = 1
    elif result == dict_nums[num] and num < result_num:
        result_num = num
print(result_num)
    #if dict_nums[num] == result and num 
