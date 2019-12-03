# https://www.acmicpc.net/problem/10828 문제 제목 : 스택 , 언어 : C, 날짜 : 2019-12-03, 결과 : 성공

#include <stdio.h>
#include <string.h>

int main()
{
 	int list_stack[10000] = {-1};
	int X = 0;
	int N=0;
	int count = 0;
 	
	scanf("%d", &N);
	
	for(;N > 0; N--)
	{
	
		char input[6];
		scanf("%s", &input);
		if(strcmp(input,"push") == 0)
		{
			scanf("%d", &X);
			list_stack[count] = X;
			count+=1;
		}
		else if(strcmp(input,"pop") == 0)
		{
			if(count == 0)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", list_stack[count-1]);
				list_stack[count-1] = -1;
				count-=1;
			}
		}
		else if(strcmp(input,"size") == 0)
		{
			printf("%d\n", count);
		}
		else if(strcmp(input,"empty") == 0)
		{
			if(count==0)
			{	
				printf("1\n");
			}
			else
			{
				printf("0\n");
			}
		}
		else if(strcmp(input,"top") == 0)// top
		{
			if(count == 0)
			{
				printf("-1\n");
			}
			else
			{
				printf("%d\n", list_stack[count-1]);
			}
		}
	}
}
