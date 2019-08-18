
#처음 생각했던 알고리즘 ----------------
import sys
num = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
for list_a in num_list:
    average = sum(list_a[1:])/list_a[0]
    str_a = round(sum([1 for a in list_a[1:] if a > average])/list_a[0]*100, 3)
    print("%0.3f" % str_a+"%")

#코드수 줄여보기 근데 이상하게 아래의 코드가 실행시간이 세배가까이 길다.. 이유는 잘 모르겠지만 찾아봐야겠다
num = int(sys.stdin.readline())
for _ in range(num):
    list_a = list(map(int, sys.stdin.readline().split()))
    print("%0.3f" % round(sum([1 for a in list_a[1:] if a > sum(list_a[1:])/list_a[0]])/list_a[0]*100, 3)+"%")
