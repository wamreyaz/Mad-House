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
		printf("Exactly one command line argument allowed.\n");
		return 1;
	}
	
	
	int size_keyW = strlen(argv[1]);
	for(int i = 0; i < size_keyW; i++)
	{	
		if(isalpha(argv[1][i])){}
		else
		{
			printf("Keyword should be alphabetical\n");
			return 1;
		}
	}
	
	
	string input = GetString();
	int size = strlen(input);
	int count = 0;
	int key;
	string keystring = argv[1];
		
	/* The following block of code first brings the alphabet down 
	 * to between 0 and 26. Then we add the key and use modulo
	 * 26 to wrap around 'z' and continue back from 'a'. Then we
	 * again get it up to its ASCII value and save it.
	*/
		
	for(int i = 0; i < size; i++)
	{	
		if(isalpha(input[i]))
		{	
			if(count >= size_keyW)
			{	
				count %= size_keyW;
			}	
			if(isupper(keystring[count]))
			{
				key = (int) keystring[count] - (int) 'A';
			}	
			else
			{
				key = (int) keystring[count]- (int) 'a';
			}
			count++;
			
			
						
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
