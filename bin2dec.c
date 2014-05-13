/* A primer on how to do binary to decimal conversions.
/* Let's say a we have a binary number 11001. To convert
/* it to binary, we just write it as the sum of some 
/* numbers multiplied by powers of 10. For 11001, it
/* would be,(in reverse order) 
/* 1 * 10^0 +
/* 0 * 10^1 +
/* 0 * 10^2 +
/* 1 * 10^3 +
/* 1 * 10^4
/* Then you just multiply the pre-exponential part
/* of each binary placewith 2 raised to the power its 
/* corresponding ten's exponent, and add up.
/* And just like that you get the number in 
/* 		*drumroll*
/* decimal. So that's it. Hope the code is legible.
/* Cheers!
*/











#include<stdio.h>

void main() //Don't believe an int is really needed.
{
	int n, nsave, rem, temp_dec; 
	int pow2 = 1 , dec = 0;
	
	
	printf("The binary number, if ye will.\n");
	scanf("%d", &n);
	nsave = n;
	
/* The loop extracts individual digits from the binary
/* using modulus 10, multiplies it with the corresponding
/* power of 2, holds the result in temp_dec. The next 
/* digit is 'broyght forward'by division with 10.
/* We then add all values to get the final result.
*/


	while(n > 0)
	{
		rem = n % 10;
		temp_dec = rem * pow2;
		dec = dec + temp_dec;
		pow2 *= 2;
		n = n/10;
	}
	
	
	printf("The decimal equivalent"
	       " of %d is %d.\n", nsave, dec);
}
		
