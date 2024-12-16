# Import the  random function which is stored in number_generator.py file
from number_generator import generate_simple_equation

# Key variables of my program
total_questions = 5  
line_break = ("")

# Defines what the user will see and instructions on what to do wwhen they first load the program
def program_intro(name): 
    print(line_break)
    print(f"Hello {name}!") 
    print(line_break)
    print("Welcome to my Solving the Equation game! ")
    print(line_break)
    print(f"{name}, there will be a total of {total_questions} questions. ")
    print(line_break)
    print("You will need to solve I in the equations presented like 12 * I = 24" )
    print(line_break)


# Defines the equation questions and what will the user see 
def displayed_question(question_number):
    multiplier, missing_value, result = generate_simple_equation()
    print(f"Question {question_number}: Solve I in {multiplier} * I = {result}")

# When True the user will need to input their answer in integer format
    while True: 
        try: 
            user_answer = int(input("Your answer: "))
            break # Ends the loop if input is an integer
        except ValueError:  # Loop continues till an integer is inputted
            print("Please enter a valid number.")
    
# If the user answer is the right answer 
    if user_answer == missing_value:
        print("Correct!") 
        print(line_break) 
        return 1  # adds 1 to users score

# If incorrect the program will reveal the answer
    else:   
         print(f"Incorrect! The correct answer was {missing_value}.")
         print(line_break)
         return 0  # Score not changed if incorrect
    


# Defines the main code of the program
def main_program():
    name = input("What is your name? ") # User can add their name
    program_intro(name) # Takes program into and implements users name

    score = 0  #  score will start at 0 

# Loop to generate questions and checking answers
    for i in range(1, total_questions +1): 
        score += displayed_question(i)  # Score will add 1 if the displayed_question is True
    

# End of game. Shows total score
    print(f"Well Done {name}!!! Your total score is {score} out of {total_questions}.")
    print(line_break)


# Runs the entire code 
main_program()