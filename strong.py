# Python3 program for the
# above approach

# Store the factorial of
# all the digits from [0, 9]
factorial = [1, 1, 2, 6, 24, 120,
			720, 5040, 40320, 362880]

# Function to return true
# if number is strong or not
def isStrong(N):

	# Converting N to String
	# so that can easily access
	# all it's digit
	num = str(N)

	# sum will store summation
	# of factorial of all
	# digits of a number N
	sum = 0

	for i in range (len(num)):
		sum += factorial[ord(num[i]) -
						ord('0')]

	# Returns true of N
	# is strong number
	if sum == N:
	return True
	else:
	return False

# Function to print all
# strong number till N
def printStrongNumbers(N):
	
	# Iterating from 1 to N
	for i in range (1, N + 1):
	
		# Checking if a number is
		# strong then print it
		if (isStrong(i)):
			print (i, end = " ")

# Driver Code
if __name__ == "__main__":

	# Given number
	N = 1000

	# Function call
	printStrongNumbers(N)
	
# This code is contributed by Chaithanya

