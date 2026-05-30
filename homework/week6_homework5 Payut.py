# Answer to Question 1

# Create a main function
def main():

    # Initialize the counter variable to be 0
    counter = 0

    # Open the names.txt file using "with" (in read mode) as name_file
    # I use "with" because I won't have to manually close the file using .close()
    with open("names.txt", "r") as name_file:

        # Read a line from the file
        line = name_file.readline()

        # While the line is not at the end or empty
        while line != "":

            # Increment the counter variable by 1
            counter += 1

            # Read the next line
            line = name_file.readline()

    # Print out the result of how many names were in the names.txt file
    print(f"There are {counter} names in the names.txt file")

# Call the main function.
if __name__ == '__main__':
    main()

# Answer to Question 2

# Create a main function
def main():

    # Initialize the total variable to be 0
    total = 0

    # Open the numbers.txt file using "with" (in read mode) as num_file
    # I use "with" because I won't have to manually close the file using .close()
    with open("numbers.txt", "r") as num_file:

        # Read a line from the file
        line = num_file.readline()

        # While the line is not at the end or empty
        while line != "":
            
            # Convert the data that we read from the line to an integer using int()
            num_line = int(line)

            # Add the integer to the total
            total += num_line

            # Read the next line
            line = num_file.readline()
        
    # Print out the total
    print(f"The total that is calculated from adding the series of integers in the file is {total}.")
    
# Call the main function.
if __name__ == '__main__':
    main()

# Answer to Question 3

# Import numpy library as "np", so whenever I use NumPy functions, I can just type "np" 
# and so I could access the functions in the NumPy library
import numpy as np

# Create a main function
def main():

    # Ask the user for how many random numbers they want in the file
    num_rand = int(input("Enter the number of random numbers that the file will hold: "))

    # Open the randnum.txt file using "with" (in write mode) as rand_file
    # I use "with" because I won't have to manually close the file using .close()
    # If the user does not have randnum.txt file, then this code will create a randnum.txt file for you
    # If the user has an existing randnum.txt file, this code will overwrite all the data in the file
    with open("randnum.txt", "w") as rand_file:

        # Create a for loop that loops depending on the number of times that the user input
        for i in range(num_rand):

            # Generate a random number from 1 to 500
            random_int = np.random.randint(1, 501)

            # Write the number to the file
            # You can only write string to the file so convert the number to string usingn str()
            rand_file.write(str(random_int))

            # Write a newline so the numbers don't stick to each other 
            # and each number will have their own line in the file
            rand_file.write("\n")

    # Let the user know that the random integers that they want have been written to the file
    print(f"All {num_rand} random integers have been written to the randnum.txt file successfully.")

# Call the main function.
if __name__ == '__main__':
    main()

# Answer to Question 4

# Create a main function
def main():

    # Initialize the total variable to be 0
    total = 0

    # Initialize the counter variable to be 0
    counter = 0

    # Open the randnum.txt file using "with" (in read mode) as num_file
    # I use "with" because I won't have to manually close the file using .close()
    with open("randnum.txt", "r") as num_file:

        # Read a line from the file
        line = num_file.readline()

        # While the line is not at the end or empty
        while line != "":

            # Convert the data that we read from the line to an integer using int()
            num_line = int(line)
            
            # Add the integer to the total
            total += num_line

            # Increment the counter variable
            counter += 1

            # Read the next line
            line = num_file.readline()
        
    # Print out how many random integers were in the file and the total that was calculated
    print(f"There were {counter} integers in the randnum.txt file.")
    print(f"The total that is calculated from adding the series of integers in the randnum.txt file is {total}.")
    
# Call the main function.
if __name__ == '__main__':
    main()

# Answer to Question 5

# I'm aware that the question did not state what to do with the file
# In this case, I'm just calculating the total from adding all the integers in the file
# I'm still handling the errors as specified from the question

# Create a main function
def main():

    # Create a try block
    try:

        # Initialize the total variable to be 0
        total = 0

        # Open the numbers.txt file using "with" (in read mode) as num_file
        # I use "with" because I won't have to manually close the file using .close()
        with open("numbers.txt", "r") as num_file:

            # Read a line from the file
            line = num_file.readline()

            # While the line is not at the end or empty
            while line != "":

                # Convert the data that we read from the line to an integer using int()
                num_line = int(line)

                # Add the integer to the total
                total += num_line

                # Read the next line
                line = num_file.readline()
        
        # Print out the total from adding the numbers in the file
        print(f"The total that is calculated from adding the series of integers in the file is {total}.")
    
    # Create an except block that handles IOError
    except IOError:

        # If an IOError occurs, print this out
        print("An error occured while reading the file.")

    # Create an except block that handles ValueError
    except ValueError:

        # If a ValueError occurs, print this out
        print("An error occured while trying to convert the items in the file to an integer.")

# Call the main function.
if __name__ == '__main__':
    main()
