import random

#arg_c = len(sys.argv)
#print(arg_c)

def welcome():
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	print("You have 5 chances to guess the correct number.\n")

def choose_dif():
	print("Please select the difficulty level:")
	print("1. Easy (10 chances)")
	print("2. Medium (5 chances)")
	print("3. Hard (3 chances)\n")
	choice = input("Enter your coice: ")
	try:
		r = int(choice)
		if(0<r<4):
			return r
		else:
			#print(r)
			print("Please enter a number from [1,2,3]")
			return choose_dif()
	except:
		#print(r)
		print("Please enter a number from [1,2,3]")
		return choose_dif()

def start_game(dif):
	diff = ""
	chance = 0
	if(dif == 1):
		diff = "Easy"
		chance = 10
	elif(dif == 2):
		diff = "Medium"
		chance = 5
	elif(dif == 3):
		diff = "Hard"
		chance = 3
	print("Great! You have selected the {} difficulty level.".format(diff))
	print("Let's start the game!")
	num = random.randint(1,100)
	guess = 0
	i = 0
	while(i < chance):
		print("")
		print("{} chances left.".format(chance - i))
		try:
			guess = int(input("Enter your guess: "))
		except:
			print("Please only enter numbers.")
			continue
		if(guess > 100 or guess < 0):
			print("Number is between 1-100, please guess resonably.")
		else:
			i += 1
		if(guess > num):
			print("Incorrect! The number is less than {}.".format(guess))
		elif(guess < num):
			print("Incorrect! The number is greater than {}.".format(guess))
		else:
			print("Congratulations! You guessed the correct number in {} attempts.".format(i))
			break
	if(i == chance):
		print("All chances used up, better luck next time.")
	return i

if(__name__ == "__main__"):
	welcome()
	dif = choose_dif()
	start_game(dif)
