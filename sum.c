#include <stdio.h>

int main(){

	int x, y;

	printf("Digite dois numeros : ");

	scanf("%d %d", &x, &y);

	x = x+y;

	printf("\nA soma dos dois numeros e :%d\n", x);

	getchar();
	return 0;
}