# 아직 푸는중인데 할게 많아서 미완성으로 올립니다..ㅠ
# 2차원 리스트를 복사하니 자꾸만 얕은복사가되서 삽질했습니다..


import sys

#a = list(map(int,sys.stdin.readline().split()))
#b = a[:]
#b[1] = 'asdf'
#print(a)
N,M = map(int,sys.stdin.readline().split())
list_map = [list(map(int,sys.stdin.readline().split())) for _ in range(int(N))]

list_map_copy =  [a[:] for a in list_map]
#list_map = [a[:] for a in list_map]
num = 0

while(True):
    count_a = 0
    for n in range(N):
        for m in range(M):
            count=0
            c_b = 0
            if list_map[n][m] > 0:
                try:
                    if list_map[n-1][m] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n+1][m] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n][m-1] == 0:
                        count+=1
                except:
                    pass
                try:
                    if list_map[n][m+1] == 0:
                        count+=1
                except:
                    pass
                if count>0:
                    #print(list_map[n][m], list_map_copy[n][m])
                    list_map_copy[n][m]=list_map_copy[n][m] - count
                    #print(list_map[n][m], list_map_copy[n][m])
                    if list_map_copy[n][m]<0:
                        list_map_copy[n][m]=0
                    count_a+=1
    num+=1

    if count_a == 0:
        [print(fdsa) for fdsa in list_map]
        print(" ")
        [print(asdf) for asdf in list_map_copy]
        print("------------------------------------")
        break
    list_map= [b[:] for b in list_map_copy]
    
print(num-1)

