# https://www.acmicpc.net/problem/11004 문제 제목 : K번째 수 , 언어 : Python, 날짜 : 2019-10-26, 결과 : 실패
# https://www.acmicpc.net/problem/11004 문제 제목 : K번째 수 , 언어 : Python, 날짜 : 2019-10-28, 결과 : 실패
# https://www.acmicpc.net/problem/11004 문제 제목 : K번째 수 , 언어 : Python, 날짜 : 2019-10-29, 결과 : 성공

# 이 문제는 질문글탭에 가보니 정렬문제가 아니라 선택 알고리즘에 관한 문제라고 한다
# 참고로 아래코드는 python3으로 제출시 시간초과, PyPy3로 제출시 메모리초과가 뜬다..

#--------- 1차 코드 ----------#
import sys

def qsorting(arr, len_arr):
    if len_arr<=1:
        return arr
    pivot = arr[len_arr//2]
    lesser, equal, bigger =[], [], []
    count_lesser, count_bigger = 0, 0
    for num in arr:
        if num > pivot:
            bigger.append(num)
            count_bigger+=1
        elif num < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)

    return qsorting(lesser, count_lesser) + equal + qsorting(bigger, count_bigger)

N, K = map(int, sys.stdin.readline().split())
list_num = list(map(int, sys.stdin.readline().split()))
print(qsorting(list_num, N)[K-1])


#--------- 2차 코드 ----------#
# 퀵셀렉트를 한번 구현해 보았다. 근데 이 코드는 16% 부근에서 런타임에러가 난다..
import sys
def qselect(arr, len_arr):
    global K
    if len_arr<=1:
        return arr
    key_index = len_arr//2
    pivot = arr[key_index]
    lesser, equal, bigger =[], [], []
    count_lesser, count_bigger, count_equal = 0, 0, 0
    for num in arr:
        if num > pivot:
            bigger.append(num)
            count_bigger+=1
        elif num < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)
            count_equal+=1

    if K == count_lesser:
        return equal
    elif K > count_lesser:
        K -= count_lesser+1
        return qselect(bigger, count_bigger)
    else:
        return qselect(lesser, count_lesser)
    
N, K = map(int, sys.stdin.readline().split())
K=K-1
list_num = list(map(int, sys.stdin.readline().split()))
print(qselect(list_num, N)[0])

#--------- 2차 코드 ----------#
# 우선 전의 코드가 틀린이유는 equal리스트를 제대로 처리해 주지않아 
"""
5 1
1 1 1 1 1 과 같은 입력에 오류가 났다.
또한 그것을 고친후에도 메모리 초과, 시간초과가 났는데 이는 pivot값을 랜덤으로 선택하게 했더니 해결되었다.
"""
import sys
import random
def qselect(arr, len_arr):
    global K
    if len_arr<=1:
        return arr
    pivot = arr[random.randint(0, len_arr-1)]
    lesser, equal, bigger =[], [], []
    count_lesser, count_bigger, count_equal = 0, 0, 0
    for num in arr:
        if num > pivot:
            bigger.append(num)
            count_bigger+=1
        elif num < pivot:
            lesser.append(num)
            count_lesser+=1
        else:
            equal.append(num)
            count_equal+=1
    if K == count_lesser or count_lesser <= K < count_lesser+count_equal:
        K -= count_lesser+count_equal
        return equal
    elif K > count_lesser:
        K -= count_lesser+count_equal
        return qselect(bigger, count_bigger)
    else:
        return qselect(lesser, count_lesser)
        
N, K = map(int, sys.stdin.readline().split())
K=K-1
list_num = list(map(int, sys.stdin.readline().split()))
print(qselect(list_num, N)[0])
