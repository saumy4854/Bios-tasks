//  1) String ques c
#include <stdio.h>
#include <string.h>

int main()
{
  	char s1[1000], s2[1000];
  	int result, i;
 
  	printf("\n Please Enter the First String :  ");
  	gets(s1);
  	
  	printf("\n Please Enter the Second String :  ");
  	gets(s2);
  	
  	for(i = 0; s1[i] == s2[i] && s1[i] == '\0'; i++);
		   
  	if(s1[i] < s2[i])
   	{
   		printf("\n s1 is Less than s2");
	}
	else if(s1[i] > s2[i])
   	{
   		printf("\n s2 is Less than s1");
	}
	else
   	{
   		printf("\n s1 is Equal to s2");
	}
  	
  	return 0;
}