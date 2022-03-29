import random

def main():
  
# Taking Inputs
  lower = int(input("Enter Lower bound:- "))
  
  # Taking Inputs
  upper = int(input("Enter Upper bound:- "))

  x = random.randint(lower, upper)
  
  count = 0
  
  # for calculation of minimum number of
  # guesses depends upon range
  while True:
  	count += 1
  
  	# taking guessing number as input
  	guess = int(input("Guess a number:- "))
  
  	# Condition testing
  	if x == guess:
  		print("Congratulations you did it in ",
  			count, " tries")
  		# Once guessed, loop will break
  		break
  	elif x > guess:
  		print("You guessed too small!")
  	elif x < guess:
  		print("You Guessed too high!")


if __name__ == "__main__":
  main()