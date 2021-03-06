#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{	

	// Raise exception for no, or more than 1 arguments.
	if(argc != 2)
	{
		printf("Exactly one numeric command line argument allowed.\n");
		return 1;
	}
	
	// Convert char to int.			
	int key = atoi(argv[1]);
	string input = GetString();
	int size = strlen(input);
	
	/* The following block of code first bring the alphabet down 
	 * to between 0 and 26. Then we add the key and use modulo
	 * 26 to wrap around 'z' and continue back from 'a'. Then we
	 * again get it up to its ASCII value and save it.
	*/
		
	for(int i = 0; i < size; i++)
	{
		if(isalpha(input[i]))
		{	
			if(islower(input[i]))
			{
				input[i] = input[i] - 'a';
				input[i] += key;
				input[i] %= 26;
				input[i] += 'a';
				//printf("%c", input[i]); // DEBUG POINT
			}
			else
			{
				input[i] = input[i] - 'A'; 
				input[i] += key;
				input[i] %= 26;
				input[i] += 'A';
			}
		}
	}
	
	// Print the ciphered text.
	for (int i = 0; i < size; i++)
	{
		printf("%c", input[i]);
	}
	
	printf("\n");
	
	return 0;
	
}
