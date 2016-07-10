#include <stdio.h>

int main(){

	int quant, i, j, aux;

	printf("Digite a quantidade de numeros a serem digitados: ");
	scanf("%d", &quant);

	int vetor[quant];

	printf("\n");

	printf("Digite os numeros a serem ordenados, um por vez:\n");
	for (i = 0; i < quant; ++i)
	{
		scanf("%d", &vetor[i]);
	}

	printf("\n");

	printf("Os numeros desordenados sao: ");

	for (i = 0; i < quant; ++i)
	{
		printf("%d ", vetor[i]);
	}

	printf("\n");

	for (i = 0; i < quant; ++i)
	{
		for (j = 0; j < (quant-1); ++j)
		{
			if(vetor[j] > vetor[j+1]){
				aux = vetor[j+1];
				vetor[j+1] = vetor[j];
				vetor[j] = aux;
			}
		}
	}

	printf("Os numeros ordenados sao: ");

	for (i = 0; i < quant; ++i)
	{
		printf("%d ", vetor[i]);
	}


	return 0;
}