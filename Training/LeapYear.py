year = int(input("Input a year here: "))

if (year % 4 == 0):
	if not(year % 100 == 0):
		print("It's a leap year!")
	else:
		if (year % 400 == 0):
			print("It's a leap year!")
		else:
			print("Not a leap year.")
else:
	print("Not a leap year.")