from sys import argv
import sys
import string

# Raise exception for no, or more than 1 argument.
if(len(argv) != 2):
	print 'Only one command line argument allowed.'
	exit(1)

"""
We unpack the argument vector so that 'key' holds the
(numeric) key used for implementing the cipher.
Since it is a string we convert it to an int.
"""
script, key = argv
key = int(key)
string = raw_input('Enter the string you want encrypted\n')
size = len(string)

"""
To maintain numbers as they are, and to maintain case,
we implement some if-constructs. After filtering out
the aplhabetic portion of the string, we change
the characters to their respective ASCII values.
Begin counting from 0, to 26. Add the key, using
modulo arithmetic in the process, and then get
it back upto ASCII values and print them.
"""
for i in range(0,size):
	# Check if alphabet.
	if(string[i].isalpha()):
		# Check if lowercase.
		if(string[i].islower()):

			temp = ord(string[i])
			temp -= ord('a')
			temp += key
			temp %= 26
			temp += ord('a')
			sys.stdout.write(chr(temp))

		else:

			temp = ord(string[i])
			temp -= ord('A')
			temp += key
			temp %= 26
			temp += ord('A')
			sys.stdout.write(chr(temp))
	else:

		sys.stdout.write(string[i])

print '\n'

exit(0)
