import secrets
import hashlib

a_string = ''
hashed_string = ''
a_stringWithSixZeros = False
a_stringWithSevenZeros = False
a_stringWithEightZeros = False
a_stringWithNineZeros = False
a_stringWithTenZeros = False

while hashed_string[:11] != '0000000000':
	a_string = 'Anna Liam Nicholas Zachary ' + str(secrets.token_bytes(10))
	hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
	if hashed_string.startswith('000000') and a_stringWithSixZeros == False:
		a_stringWithSixZeros = True
		print('Six Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('0000000') and a_stringWithSevenZeros == False:
		a_stringWithSevenZeros = True
		print('Seven Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('00000000') and a_stringWithEightZeros == False:
		a_stringWithEightZeros = True
		print('Eight Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('000000000') and a_stringWithNineZeros == False:
		a_stringWithNineZeros = True
		print('Nine Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('0000000000') and a_stringWithTenZeros == False:
		a_stringWithTenZeros = True
		print('Ten Zeros:')
		print(a_string)
		print(hashed_string)