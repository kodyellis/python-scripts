print ('How many pets?')

nump = input()
try:
	if int(nump) >= 4:
		print('wow')
	else:
		print('None')

except ValueError:
	print( 'no number')
 
