# Answer to Question 1

# Create a convertMiles function that accepts kilometers as an argument
def convertMiles(km):
    
    # Calculate the miles from the given kilometers
    miles = km * 0.6214

    # Print the result
    print(f"The conversion of {km} kilometers to miles is {miles:.2f} miles.")

# Create a main function
def main():

    # Ask the user for kilometers that they want to convert to miles
    km_input = float(input("Enter a distance in kilometers to convert to miles: "))

    # Convert the kilometers to miles using the convertMiles function
    convertMiles(km_input)

# Run the main function
main()

# Answer to Question 2

# Create a maximum function that takes two integer values as its arguments
def maximum(num1, num2):
    
    # If the first number is bigger than the second number, then return the first number
    if num1 > num2:
        return num1
    
    # If the second number is bigger than the first number, then return the second number
    elif num1 < num2:
        return num2
    
    # If both values are equal, then return "both values are equal"
    # I know this is not required by the question, but I just wanted to do it
    # It felt wrong not having a case that ensures what happens when both values are equal
    else:
        return "both values are equal"
    
# Create a main function
def main():

    # Ask the user for the first integer 
    int1 = int(input("Enter the first integer: ")) 

    # Ask the user for the second integer
    int2 = int(input("Enter the second integer: "))

    # Determine the larger number between the first integer and the second integer using maximum() 
    max_num = maximum(int1, int2)

    # Print out the result of which value is larger
    print(f"Between the values {int1} and {int2} the bigger number is {max_num}.")

# Run the main function
main()

# Answer to Question 3

# 3.1

# Import numpy library as "np", so whenever I use NumPy functions, I can just type "np"
import numpy as np

# Create a function that displays the question
# Takes 2 numbers as its arguments and display them in a question format
def displayNum1PlusNum2(num1, num2):

    # Display the question
    print(f"{num1} + {num2}")

# Create a function that gets the user's answer, this function takes no argument
def getAnswer():

    # Get the user's answer
    user_answer = int(input("Enter your answer: "))

    # Return the user's answer
    return user_answer

# Create a function that determines if your answer was correct or not, if not display the correct answer
# Takes 2 arguments; the correct answer and the user's answer
def showResult(correctAnswer, userAnswer):

    # If the user answered correctly, then display that they got the correct answer
    if correctAnswer == userAnswer:

        # Display that they got the correct answer
        print("You got the correct answer!")

    # If the user didn't answer correctly, then display that they got the question wrong
    # and also display the correct answer for the question
    else:

        # Display that they got the wrong answer and show the correct answer
        print("Unfortunately, your answer is wrong.")
        print(f"The correct answer is {correctAnswer}.")

# Create a main function
def main():

    # Use np.random.randint(0,101) to generate random numbers between 0 and 100
    rand1 = np.random.randint(0, 101)
    rand2 = np.random.randint(0, 101)

    # Display the question
    displayNum1PlusNum2(rand1, rand2)

    # Calculate the answer
    answer = rand1 + rand2

    # Ask the user for their answer
    user_answer = getAnswer()

    # Check if the user got the answer correctly
    showResult(answer, user_answer)

# Run the main function
main()

# 3.2

# Create a main function
def main(): 
    
    # Initiate user_choice as "y" so the while loop starts running
    user_choice = "y"

    while user_choice != "n":

        # Use np.random.randint(0,101) to generate random numbers between 0 and 100
        rand1 = np.random.randint(0, 101)
        rand2 = np.random.randint(0, 101)

        # Display the question
        displayNum1PlusNum2(rand1, rand2)

        # Calculate the answer
        answer = rand1 + rand2

        # Ask the user for their answer
        user_answer = getAnswer()

        # Check if the user got the answer correctly
        showResult(answer, user_answer)

        # Ask if the user wants to continue the quiz, if the user types 'n' the while loop will stop
        # If the user types anything else, the while loop will keep running
        user_choice = input("Do you want to continue the quiz? type 'n' to stop, type anything to continue: ")

    # Thanking the user for using the program, letting them know that the program has been sucessfully stopped
    print("Thank you for using my program!")

# Run the main function
main()