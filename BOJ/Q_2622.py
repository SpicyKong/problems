// https://www.acmicpc.net/problem/2622 문제 제목 : 삼각형만들기 , 언어 : C, 날짜 : 2019-12-02, 결과 : 실패
// C언어를 시작할겸 쉬운문제를 잡았는데 못풀었다..
#include <stdio.h>
int main(){
	int n = 0,  side1 = 0, side2 = 0, count = 0;
	
	scanf("%d", &n);
	
	if(n == 1 || n == 2 || n==4){
		printf("0");
	}
	else{
		
	side1 = n/3;
	side2 = n - side1;
	for(;side1>0;side1--){
		side2++;
		count+=1;
	}
	printf("%d", count);
	}
}
