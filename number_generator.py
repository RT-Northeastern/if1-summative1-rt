# importing the random module from the Python Library which generates random numbers
import random 

def generate_simple_equation():
    multiplier = random.randint(1,10)           # Random number for multiplier 
    missing_value = random.randint(1,10)        # Random number for missing values
    result = multiplier * missing_value         # Result of the two random generated numbers
    return multiplier, missing_value, result    # Function returns all three values 



