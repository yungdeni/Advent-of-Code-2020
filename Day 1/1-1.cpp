#define _CRT_SECURE_NO_DEPRECATE 
#include <stdio.h>
#include <stdlib.h>

int sum(int myArray[]);

int main()
{
	
	FILE *fp;
	fp = fopen("path to inputs", "r");
	if (NULL == fp) {
		perror("Error: :");
		exit(EXIT_FAILURE);
	}

	int inputArray[200];
	for (int i = 0; i < 200; i++) {
		fscanf(fp, "%i", &inputArray[i]);
	}

	printf("%d", sum(inputArray));

	return 0;
}

int sum(int myArray[])
{
	//very ineffecient (worst case O(n^3))
	//hash table implementation would be O(n^2)
	for (int i = 0; i < 200; i++) {
		for (int j = 0; j < 200; j++) {
			//if (myArray[i] + myArray[j] == 2020) {
			//	return myArray[i] * myArray[j];
			//}
			for (int k = 0; k < 200; k++) {
				if ((myArray[i] + myArray[j] + myArray[k]) == 2020) {
					return myArray[i] * myArray[j] * myArray[k];
				}
			}
		}
	}
}
