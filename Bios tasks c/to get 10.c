// to get 10 ques 
#include <stdio.h>
int main () {
    int n ;
    printf("Enter no of grades received: ");
    scanf("%d", &n) ;
    int a[n];
    for (int i=0 ; i < n ; i++) {
        printf("Enter the grades received : ");
        scanf("%d" , &a[i]);
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum+=a[i];
    }
    int k = (19*n) - (2*sum);
    printf("%d", k);
    return 0;
}