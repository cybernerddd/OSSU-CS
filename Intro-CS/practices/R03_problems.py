# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

# x = float(input("Using bisection search calculate the forth root of: " ))
# epsilon = 0.01
# low = 0
# high = x
# ans = (low + high) / 2 # midpoint4

# while (ans**4-x) >= epsilon:
#     if ans**4 > x:
#         high = ans        
    
#     else:
#         low = ans
#     ans = (low + high) / 2
# print(f"Fourth root of {x} is approximately {ans}")


# print("Cyber"[0])



# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range.

def in_range(num, full):
    """"
    input:int
    find if num in range
    """
    return num in range(full+1)
    
# print(in_range(3, 4))




# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).

def is_perfect(n):
    """
    input: int.
    sum the proper divisors of n
    Returns True if n is a perfect number, False otherwise
    """
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

print(is_perfect(7))


# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0
x = float(input("Enter a number to find fourth root: "))
high = x
guess = (ans + high) / 2

while abs(guess**4-x) >= epsilon:
    if guess**4 > x:
        num_guesses += 1
        high = guess
    else:
        ans = guess

    guess = (ans + high) / 2

print(f"Number of counts: {num_guesses}")
print(f"The fourth root of {x} is approximately {guess}")





