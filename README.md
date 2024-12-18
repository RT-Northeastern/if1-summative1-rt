# **Solving the Equation Program Game**

## Introduction 

Welcome to my **Solving the Equation Program** ! This project is created using **Python** and includes challenging users to solve equations whilst keeping count of the score and displaying the results at the end. This user manual will guide you through the program and its features. 

---

## Purpose of the program
The program allows users to: 

- Test their numerical skills
- Check if their answers are correct or incorrect
- Understand the fundamental strucutre of a python code.

## Main Features of the program
Main features of **Solving the Equation Program** include: 

- Generating 5 random multiplication equations using random numbers
- Users answers are marked immediately displaying either "Correct!" or "Incorrect!"
- Simple user-friendly interface
- Counts score and displays results and end of program

---

## Installation Requirements 
For the program to run you will need the following: 

1. **[Python Version 3.9+](https://www.python.org/downloads/)**
2. **[Visual Studio Code](https://code.visualstudio.com/Download)**
3. **main.py** & **number_generator.py** files
   

## Installation & Setup
1. Create a file folder called if1-task1
2. Download the files main.py from if1-summative1-rt repository and save in if1-task1
3. Download the files number_generator.py from if1-summative1-rt repository and save in if1-task1
4. Open Visual Studio Code
5. Press File > Open Folder > Select if1-task1 folder
6. Select the main.py file tab
7. Run the program by pressing ▶ on the top right

---

## Program Instructions
- You will be asked to **"Enter your name"**
- The program will ask you 5 simple equations where you need to solve I (E.g. 12 * I = 24)
- You will get be aware if your answer is "Correct!" or "Incorrect!"
- At the end of the game your results will be displayed

---


## Example Game Run

![Example of Game](https://github.com/RT-Northeastern/if1-summative1-rt/blob/main/image-equation_game-example.png)


---

## Program Code Breakdown
This is how the code works breaking down the python code in the files: 

### number_generator.py 

This module file defines the function to generate the random numbers used in simple equations for the game. 

```python

# importing the random module from the Python Library which generates random numbers
import random 

def generate_simple_equation():
    multiplier = random.randint(1,10)           # Random number for multiplier 
    missing_value = random.randint(1,10)        # Random number for missing values
    result = multiplier * missing_value         # Result of the two random generated numbers
    return multiplier, missing_value, result    # Function returns all three values 


```

#### Primary Points 
- **in-line comments** are noted throughout the code as seen in comments starting with **#**
- **import Random** allows to use the built-in python module from the Python Library which includes the ability to generate random numbers
- **random.randint(1,10)** generates two random integers between the numbers in brackets, 1 and 10.
- **multiplier** & **missing_value** are named variables created where <u>random numbers</u> are assigned to the variables which will be used to generate the equation questions
- **result** is the final result of multiplier multiplied by missing_value
- Finally the function returns the 3 values **multiplier, missing_value and result**
  

### main.py

This module file is the main file that the program is run which gets the users input, generates questions and keeps count of the score. 

``` python

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

```
#### Primary Points 
- From the **number_generator.py** file the defined function: **generate_simple_equation** is imported to our main program.
- The **"program_intro(name)"** function calls the arguement **name** to introduce the users name and explain the game.
- Defined functions includes the use of **f-strings** to help use different parameters alongside literal strings via {}. 
- "**displayed_question(question_number)"** function is used to display the questions to the user by calling the **generate_simple_equation**.
- The code handles errors where the user has to input their answer as integers only through **Try** & **Except** statements.
- Using **"Try** & "**Except"** in the code allows to ensure only integers are inputted by the user as if the **"Try"** is not met then it will follow with the **"Except ValueError"** path which displays an error message.
- **"if"** & **"else"** statements are used to let the user know if their answer inputted was correct or incorrect. If correct the statements return a +1 to score.
- **"main_program"** function runs the entire code starting the game and looping through the 5 random questions tracking the score throughout. The function ends with printing the final score and congratulating the user. 


####
---

# Contact 
For any questions or feedback please contact: 

rt4373a@nulondonstudents.org

---
