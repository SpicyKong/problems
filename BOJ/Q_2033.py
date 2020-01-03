# https://www.acmicpc.net/problem/2033 문제 제목 : 반올림 , 언어 : Python, 날짜 : 2020-01-03, 결과 : 실패
# 오늘은 하루종일 밖이라 코딩을 못한다..
import sys
N = list(sys.stdin.readline()[:-1])
#test_buffer = 2
#print(len(N)-2)
def reload(len_a, list_a):
    for i in range(1,len_a+1):
        if 0 == len_a - i and int(list_a[len_a - i]) >= 10:
            list_a[len_a - i] = str(int(list_a[len_a - i]) - 10)
            list_a = ['1'] + list_a
            
            #list_a[len_a - i -1] = str(int(list_a[len_a - i -1]) + 1)
        elif int(list_a[len_a - i]) >= 10:
            list_a[len_a - i] = str(int(list_a[len_a - i]) - 10)
            list_a[len_a - i -1] = str(int(list_a[len_a - i -1]) + 1)
    return list_a

#print(list_a[len_a - i])
#if int(list_a[len_a - i]) >= 10:
#    
#    pass


#len_a = len(N)
#for i in range(len_a):
#    #list_a
#    print(N[len_a - i - 1]) 
#    

    
    
    
    
        

    
length = len(N)
for i in range(length-1):
    #print(N[length-1 - i])
    if int(N[length-1 - i]) >= 5:
        N[length-1 - i] = '0'
        N[length-1 - i - 1] = str(int(N[length-1 - i - 1]) + 1)
    else:
        N[length-1 - i] = '0'
    N = reload(length, N)
#print(N)   
print(int("".join(N)))
