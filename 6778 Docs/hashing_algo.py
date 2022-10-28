import os
import secrets
import hashlib

a_string = ''
hashed_string = ''

max_leading_zeros = 0
iterations = 0

most_zero_string = ''

# while the first 10 characters of the hashed string are not 0000000000
while hashed_string[:11] != '0000000000':
		# generate a random string
		a_string = 'Anna Liam Nicholas Zachary ' + str(secrets.token_bytes())
		# hash the string
		hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()

		iterations += 1

		os.system('clear')
		print("Iterations:", iterations)
		print('Max leading zeros:', max_leading_zeros)
		print(hashed_string)
		print(most_zero_string)
		
		if hashed_string.startswith('0'):
				leading_zeros = len(hashed_string) - len(hashed_string.lstrip('0'))
				if leading_zeros > max_leading_zeros:
					most_zero_string = a_string
					max_leading_zeros = leading_zeros
                        