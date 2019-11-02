# 지금 풀고있는중..

import sys
from collections import deque
N = int(sys.stdin.readline())

list_a = [int(sys.stdin.readline()) for _ in range(N)]
list_b = deque([_+1 for _ in range(N)])
list_c = []
stack_a = []
end = False
count_i = 0
while True:
    num = list_b.popleft()
    stack_a.append(num)
    print('+')
    if num == list_a[count_i]:
        list_c.append(stack_a.pop())
        count_i+=1
        print('-')
    #print(count_i)
print(list_c)
