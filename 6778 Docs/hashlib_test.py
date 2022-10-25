import secrets
import hashlib

a_string = ''
hashed_string = ''
a_stringWithSixZeros = 'false'
a_stringWithSevenZeros = 'false'
a_stringWithEightZeros = 'false'
a_stringWithNineZeros = 'false'
a_stringWithTenZeros = 'false'

while hashed_string[:11] != '00000000':
	a_string = 'Anna Liam Nicholas Zachary ' + str(secrets.token_bytes(10))
	hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
	if hashed_string.startswith('000000') and a_stringWithSixZeros == 'false':
		a_stringWithSixZeros = 'true'
		print('Six Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('0000000') and a_stringWithSevenZeros == 'false':
		a_stringWithSevenZeros = 'true'
		print('Seven Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('00000000') and a_stringWithEightZeros == 'false':
		a_stringWithEightZeros = 'true'
		print('Eight Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('000000000') and a_stringWithNineZeros == 'false':
		a_stringWithNineZeros = 'true'
		print('Nine Zeros:')
		print(a_string)
		print(hashed_string)
	if hashed_string.startswith('0000000000') and a_stringWithTenZeros == 'false':
		a_stringWithTenZeros = 'true'
		print('Ten Zeros:')
		print(a_string)
		print(hashed_string)
