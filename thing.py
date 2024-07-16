# Calculating the number of possible combinations for different scenarios

# Define the lengths and character sets
length = 18
lowercase = 26
mixed_case = 52
letters_numbers = 62
letters_numbers_special = 94

# Calculate the number of combinations
combinations_lowercase = lowercase ** length
combinations_mixed_case = mixed_case ** length
combinations_letters_numbers = letters_numbers ** length
combinations_letters_numbers_special = letters_numbers_special ** length

combinations_lowercase, combinations_mixed_case, combinations_letters_numbers, combinations_letters_numbers_special



import math

# Calculate the number of ways to choose 10 pairs from 95 characters
n = 95
k = 10
plugboard_combinations = math.factorial(n) / (math.factorial(k) * (2**k) * math.factorial(n - 2*k))

plugboard_combinations
