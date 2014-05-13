#include<stdio.h>

void main()
{
	int n, nsave, rem, temp_dec;
	int pow2 = 1 , dec = 0;
	printf("The binary number, if ye will.\n");
	scanf("%d", &n);
	nsave = n;
	while(n > 0)
	{
		rem = n % 10;
		temp_dec = rem * pow2;
		dec = dec + temp_dec;
		pow2 *= pow2 * 2;
		n = n/10;
	}
	printf("The decimal equivalent"
		   " of %d is %d.\n", nsave, dec);
}
		
