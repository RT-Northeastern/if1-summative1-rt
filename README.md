# **Solving the Equation Program Game**

## Table of Contents 
- [**Introduction**](#Introduction)
- [**Purpose of the program**](#purpose-of-the-program)
- [**Main Features of the program**](#main-features-of-the-program)
- [**Installation Requirements**](#installation-requirements)
- [**Installation & Setup**](#installation--setup)
- [**Running the Program**](#running-the-program)
- [**How to Play the Program**](#how-to-play-the-program)
- [**Example Game Run**](#example-game-run)
- [**Video Example Game Run**](#example-game-run)
- [**Program Code Breakdown**](#program-code-breakdown)
   - [**number_generator.py**](#number_generatorpy)
        - [**Primary Points**](##primary-points-1)
   - [**main.py**](#mainpy)
        - [**Primary Points**](##primary-points-2)
- [**Troubleshooting & Issues**](#troubleshooting-&-issues)
- [**Future Improvements**](#future-Improvements)
- [**License**](#licenses)
- [**Contact**](#contact)

---
      




## Introduction 

Welcome to my **Solving the Equation Program**! This project is a **Python** based program that involves challenging users to solve equations strengthening their numerical skills. The program primarily generates 5 random numbers which are then formulated into a random equation. This is then displayed to the user where they will need to solve the unknown constant variable **I**. Alongside this the program provides immediate feedback to the user and keeps count of the score displaying the results at the end making the entire experience interactive and fun for the user. This user manual will guide you through the program and its features designed by myself. 


---

## Purpose of the program
The program allows users to experience a fun learning environment for all who are wanting to develop their numerical algebra skills. The program designed is to generate 5 random numbers between 1-10 and then used to generate 5 equations for the user to solve. The program shows the results of each answer to help the user evaluate their answers in real-time. The program can also be targeted to those who are early beginners to python programming as they can use this as influence to learn how fundamental functions and statements are used to formulate an equation based program. 


---

## Main Features of the program
The main features of **Solving the Equation Program** include: 

- Random Generation: The program generates 5 random multiplication equations hence the user will not know what the next equation will be.
- Counting Score: The program keeps count of the score and tracks the number of right and wrong questions with displaying the users results at the end.
- ValueError: The program ensures that the users input is strictly integers only with using **Try & Except** statements. If strings are used the user will be given a message to enter a valid number.
- Developers can customize: The program gives python developers and teachers to edit the python code once downloaded and change the number of total questions or change the random number generator range (currently set between 1 and 10).
- Immediate feedback: Users answers are marked immediately displaying either "Correct!" or "Incorrect!"
- Simple user-friendly interface
  

---


## Installation Requirements 

For the program to run successfully you will need the following: 

1. **[Python Version 3.9+](https://www.python.org/downloads/)**
2. **[Visual Studio Code](https://code.visualstudio.com/Download)**
3. **[main.py](https://github.com/RT-Northeastern/if1-summative1-rt/blob/main/main.py)** & **[number_generator.py](https://github.com/RT-Northeastern/if1-summative1-rt/blob/main/number_generator.py)** files

   
   

## Installation & Setup
1. Create a file folder called if1-task1
2. Download the files main.py from **[if1-summative1-rt repository](https://github.com/RT-Northeastern/if1-summative1-rt)**  and save in if1-task1
3. Download the files number_generator.py from **[if1-summative1-rt repository](https://github.com/RT-Northeastern/if1-summative1-rt)**  and save in if1-task1
4. Open Visual Studio Code
5. Press File > Open Folder > Select if1-task1 folder
6. Select the main.py file tab
7. Run the program by pressing ▶ on the top right

---

## Running the Program 

As you follow the last step of Installation & Setup, running the program will begin launching the Solve the Equation Game starting with you now the user to enter your name. I have instilled this feature to strengthen the engagement of the program. Please note that once you have inputted your name the program will recognise you as the given name throughout till the 5 questions have been answered. 

---

## How to Play the Program
- You will be asked to **"Enter your name"** as a string format.
- My program will then welcome you by your name and will give an introduction to the game.
- My program will then ask you 5 simple equations where you need to solve I by inputting an integer (E.g. 12 * I = 24, Answer is 2)
- As you enter your answer you will get an immediate message "Correct!" or "Incorrect!". If correct you will progress to the next question. If incorrect the program will reveal the correct answer and continue. 
- At the end of the game your results will be displayed


---


### Example Game Run

![Example of Game](https://github.com/RT-Northeastern/if1-summative1-rt/blob/main/image-equation_game-example.png)


---

### Video Example Game Run 

To watch a visual example of the code being run please download the file [Video Example Game Run](https://github.com/RT-Northeastern/if1-summative1-rt/raw/refs/heads/main/video_equation_example.mp4)

---

## Program Code Breakdown

This is how the code works breaking down the python code in the files: 

### number_generator.py 

This module file defines the function to generate the random numbers used in simple equations in the game.

Below is a Code Block which illustrates the program file. 

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
- **in-line comments** are noted throughout the code as seen in comments starting with ***#***
- **import Random** allows to use the built-in python module from the Python Library which includes the ability to generate random numbers
- **random.randint(1,10)** generates two random integers between the numbers in brackets, 1 and 10.
- **multiplier** & **missing_value** are named variables created where **random numbers** are assigned to the variables which will be used to generate the equation questions
- **result** is the final result of **multiplier** multiplied by **missing_value**
- Finally the function **returns** the 3 values **multiplier, missing_value and result**
  

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
- **in-line comments** are used seen after **#** throughout the code to help the user understand the code better. 
- From the **number_generator.py** file the defined function: **generate_simple_equation** is imported into our main program.
- The **"program_intro(name)"** function is first defined which includes calling the arguement **name** to introduce the users name and then prints the games intro and explains the game.
        - Defined functions includes the use of **f-strings** to help use different parameters alongside **literal strings via {}**.
- **displayed_question(question_number)** function is then defined to help display the **questions** and **question number** itself to the user.
        - A variable is then included in the defined function to ensure **mutliplier, missing_value and result** is = **generate_simple_equation**
              - When called the function should return: e.g. "Question 1: Solve I in 4 * I = 8
- The code then progresses to using while TRUE statements to **handles errors** where the user has to input their answer as an **integers** when are asked the question. This is achieved through **Try** & **Except** statements.  
         - Using **"Try** & "**Except"** in the code allows to ensure only integers are inputted by the user as if the **"Try"** is not met then it will follow with the **"Except ValueError"** path which displays an error message: **"Please enter a valid number".**
- **"if"** & **"else"** statements are used to let the user know if their answer inputted was correct or incorrect. If correct the statements return a +1 to score.
- **"main_program"** function runs the entire code starting the game and looping through the 5 random questions tracking the score throughout. The function ends with printing the final score and congratulating the user.
- **score** is = 0
  


####
---
# Troubleshooting & Issues

Below I have listed a few common troubleshooting issues and solutions to solve them: 

1. The correct version of python not installed

Please note to use the correct version of python 

2. Inputting a string as an answer

Your answer must be in integer format so when solving the equations please ensure you are entering a numeric value.

3. Clearing the program for multiple attempts


To reset the program please clear the terminal in visual stuido code and run the program again. 




---

# Future Improvements 
Areas of focus to improve the program for future projects  include: 

- Giving users the ability to choose how many questions
- Having multiple difficulty levels for the user to choose from
- Implementing the ability for users to share their results directly
- Having a mixture of addition, subtraction, division and multiplication equations included in the random generator
- Be able to test the program using pytest or unittesting methods

---

# Licenses 
Python Version 3.12.3 was used and this GitHub project is licensed under the MIT License.

---

# Contact 
For any questions or feedback please contact: 

rt4373a@nulondonstudents.org

---
