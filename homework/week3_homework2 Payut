# Answer to Question 1

# Get the user input for the person's age.
age = float(input("Enter the person's age: "))

# If age is equal or less than 1 then, he/she is an infant.
if age <= 1:

    print("He or she is an infant.")

# If age is less than 13 then, he/she is a child.
elif age < 13:
    
    print("He or she is a child.")

# If age is equal or less than 13 and less than 20 then, he/she is a teenager.
elif age >= 13 and age < 20:

    print("He or she is a teenager.")

# If age is more than 20, then he/she is an adult.
# You can use "else" because the only condition left is when the age is more than 20 years old.
else:

    print("He or she is an adult.")

# Answer to Question 2

# Get user input for amount of pennies, nickels, dimes, and quarters.
pen_input = int(input("Enter the number of pennies: "))
nick_input = int(input("Enter the number of nickels: "))
dimes_input = int(input("Enter the number of dimes: "))
quart_input = int(input("Enter the number of quarters: "))

# Calculate the pennies, nickels, dimes, and quarters into cents.
pennies = pen_input
nickels = nick_input * 5
dimes = dimes_input * 10
quarters = quart_input * 25

# Sum up all the pennies, nickels, dimes, and quarters to find the number of cents.
total = pennies + nickels + dimes + quarters

# If the number of cents is 100, then you won the game.
if total == 100:

    print("Congratulations! You won this game!")

# If the number of cents is more than 100, then you lost the game.
elif total > 100:

    print("Unfortunately, you lost the game. You entered more than one dollar.")

# If the number of cents is less than 100, then you lost the game.
# I can use "else" because the last condition that can happen is when the total is less than 100.
else:

    print("Unfortunately, you lost the game. You entered less than one dollar.")


# Answer to Question 3

# Get the user input for number of packages that they purchased.
num_packages = int(input("Enter the number of packages you purchased: "))

# If the number of packages are less than 10, then there are no discount available.
if num_packages < 10:

    # Display the discount.
    print("There is no discount.")

    # Calculate the purchase for the number of packages.
    purchase = num_packages * 99
    
    # Display the amount that the user has to pay.
    print(f"The total amount that you have to pay is {purchase}.")

# If the number of packages are less than 19 and more than 10, then there is a 10% discount.
elif num_packages <= 19:

    # Display the discount.
    print("The discount is 10%")

    # Calculate the purchase for the number of packages.
    purchase = num_packages * 99

    # Calculate the discount.
    discount = 0.1 * purchase

    # Calculate the final amount after the discount.
    final_amount = purchase - discount

    # Calculate the final amount after the discount.
    print(f"The total amount that you have to pay after the discount is ${final_amount:.2f}.")

# If the number of packages are less than 49 or equal to and more than 19, then there is a 20% discount.
elif num_packages <= 49:

    # Display the discount.
    print("The discount is 20%")

    # Calculate the purchase for the number of packages.
    purchase = num_packages * 99

    # Calculate the discount.
    discount = 0.2 * purchase

    # Calculate the final amount after the discount.
    final_amount = purchase - discount

    # Calculate the final amount after the discount.
    print(f"The total amount that you have to pay after the discount is ${final_amount:.2f}.")

# If the number of packages are less than or equal to 99 and more than 49, then there is a 30% discount.
elif num_packages <= 99:

    # Display the discount.
    print("The discount is 30%")

    # Calculate the purchase for the number of packages.
    purchase = num_packages * 99

    # Calculate the discount.
    discount = 0.3 * purchase

    # Calculate the final amount after the discount.
    final_amount = purchase - discount

    # Calculate the final amount after the discount.
    print(f"The total amount that you have to pay after the discount is ${final_amount:.2f}.")

# If the number of packages are more than or equal to 100, then there is a 40% discount.
elif num_packages >= 100:

    # Display the discount.
    print("The discount is 40%")

    # Calculate the purchase for the number of packages.
    purchase = num_packages * 99

    # Calculate the discount.
    discount = 0.4 * purchase

    # Calculate the final amount after the discount.
    final_amount = purchase - discount

    # Calculate the final amount after the discount.
    print(f"The total amount that you have to pay after the discount is ${final_amount:.2f}.")

# Answer to Question 4

# Get the user input for the weight(in pounds) and height(in inches).
weight = float(input("Enter your weight(in pounds): "))
height = float(input("Enter your height(in inches): "))

# Calculate the BMI using the given formula from the problem.
bmi = weight * (703 / (height ** 2))

# Display the person's BMI.
print(f"Your BMI is {bmi:.2f}.")

# According to the problem statement in the pdf file, there would be a problem if the BMI is 18.5 or 25 because 
# the problem did not state what to do when this happens. Therefore, I searched up the BMI standards and it said that 
# if the person's bmi is less than 25 or more than or equal to 18.5, the weight is optimal. And if the person's bmi
# is more than or equal to 25, then they are overweight.

# If the person's bmi is less than 25 and more than or equal to 18.5, then their weight is optimal.
if bmi < 25 and bmi >= 18.5:

    print("According to your BMI, your weight is optimal.")

# If the person's bmi is less than 18.5, then they are underweight.
elif bmi < 18.5:

    print("According to your BMI, you are underweight.")

# If the person's bmi is more than or equal to 25, then they are overweight.
# I use "else" because it's the only condition left.
else:

    print("According to your BMI, you are overweight.")

# Answer to Question 5

# Get the user input for the year.
year = int(input("Enter a year: "))

# If the year is divisible by 100 and divisible by 400, then it is a leap year.
if (year % 100) == 0 and (year % 400) == 0:
    
    # Display the result in the given format from the problem.
    print(f"In {year}, February has 29 days.")

# If the year is not divisible by 100, but is divisible by 4, then it is a leap year.
elif (year % 100) != 0 and (year % 4) == 0:

    # Display the result in the given format from the problem.
    print(f"In {year}, February has 29 days.")

# If the year did not fall into any of those if-elif statements, then it is not a leap year.
else:

    # Display the result in the given format from the problem.
    print(f"In {year}, February has 28 days.")