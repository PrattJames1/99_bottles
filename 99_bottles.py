''' 
This program prints every line to the song "99 Bottles of Beer".
'''

for number in reversed(range(0, 100)):
	new_number = number - 1
	message = (str(number) + " bottles of beer on the wall, " + 
		str(number) + " bottles of beer, \ntake one down, pass it around, " +
		str(new_number) + " bottles of beer on the wall!\n")
	message2 = (str(number) + " bottles of beer on the wall, " + 
		str(number) + " bottles of beer, \ntake one down, pass it around, " +
		str(new_number) + " bottle of beer on the wall!\n")
	message3 = (str(number) + " bottle of beer on the wall, " + 
		str(number) + " bottle of beer, \ntake one down, pass it around, " +
		"no more bottles of beer on the wall!\n")
	if new_number == 1:
		print(message2)
	elif new_number == 0:
		print(message3)
		break
	else:
		print(message)