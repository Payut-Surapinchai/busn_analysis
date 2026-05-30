# STILL NEEDS CONFIGURATION AND MAKE GRAPH PRETTIER

# Answer to Question 1

# Create a main function
def main():

    # Ask the user for the baseball team name
    bb_team = input("Enter the name of a baseball team: ")

    # Initiate a counter variable
    win = 0

    # Open the WorldSeriesWinners.txt file with read mode and name the file object as winners
    with open("WorldSeriesWinners.txt", "r") as winners:

        # Read a line from the file
        line = winners.readline()

        # While the line is not empty
        while line != "":

            # Strip the newline character in the end
            line = line.rstrip()

            # If the line that was read is the same as the user input, increase counter variable by 1
            if line == bb_team:
                win += 1

            # Read the next line
            line = winners.readline()

    # If the counter variable is more than 0, then show how many games the team won in the World Series
    if win > 0:
        print(f"The {bb_team} has won {win} World Series games between the year 1903 and 2009(excluding 1904 and 1994).")

    # If the counter variable is 0, then the team has never won the World Series
    else:
        print("The team never won the World Series.")

# Call the main function.
if __name__ == '__main__':
    main()


# Answer to Question 2

# Import matplotlib.pyplot as plt for plotting the pie chart
import matplotlib.pyplot as plt

# Create a main function
def main():

    # Open the expenses.txt file with read mode and name the file object as expenses
    with open("expenses.txt", "r") as expenses:

        # Read the lines in the file (this will be stored as a list)
        line = expenses.readlines()

    # Convert every element in the file as an int
    for i in range(len(line)):
        line[i] = int(line[i])

    # Create a categories list for each number in the list
    categories = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Miscellaneous"]

    # Plot the pie chart and use the labels as the categories above
    plt.pie(line, labels = categories)

    # Show the plot
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()

# Answer to Question 3

# Import the matplotlib.pyplot as plt to plot the line chart
import matplotlib.pyplot as plt

# Create a main function
def main():

    # Open the 1994_Weekly_Gas_Averages.txt file with read mode and name the file object as weekly
    with open("1994_Weekly_Gas_Averages.txt", "r") as weekly:

        # Read the lines from the file (this will be stored in a list)
        line = weekly.readlines()

    # Convert every list element to a float
    for i in range(len(line)):
        line[i] = float(line[i])
    
    # Create a list that ranges from 1 to 52 to symbolizes the weeks
    weeks = list(range(1,53))

    # Plot the line chart where the weeks is on the x-axis and the gas prices are on the y-axis
    plt.plot(weeks, line)

    # Label the x-axis
    plt.xlabel("Week Number")

    # Label the y-axis
    plt.ylabel("Average Price in USD")

    # Limit the x-axis range from 1 to 52
    plt.xlim(1, 52)

    # Create a title for the plot
    plt.title("Weekly Gas Price of the Year 1994")

    # Show the plot
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()