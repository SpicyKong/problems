# https://www.acmicpc.net/problem/1978 문제 제목 : 소수 찾기 , 언어 : Python, 날짜 : 2018-10-19, 결과 : 성공

def prime_number(N,N_list):
    primeNum_all_list=[]
    for i in N_list:
        primeNum_this_list=[]
        max_primeNum= int(i**0.5)
        for j in range(1,max_primeNum+1):
            if i%j==0:
                primeNum_this_list.append(int(j))
                if j!=i/j:
                    primeNum_this_list.append(int(i/j))
        
        if len(primeNum_this_list)==2:
            primeNum_all_list.append(i)
    print(len(primeNum_all_list))
a=input()
b=[int(i) for i in input().split()]
prime_number(a,b)
