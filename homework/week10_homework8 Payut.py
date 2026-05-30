# Answer to homework 8

# Note: My answers to each prompt would be in the form of comments.

# import NumPy library
import numpy as np

# b)

# Read in the csv file using np.genfromtxt
weatherData = np.genfromtxt("weatherData.csv", delimiter = ",")

# c)

# Max value of all columns
max_data = weatherData.max(axis = 0)

# Min value of all columns
min_data = weatherData.min(axis = 0)

# Mean value of all columns
mean_data = weatherData.mean(axis = 0)

# Print the max, min, and mean for the first column
print(f"The maximum value for average temperature(in F) for a given day is {max_data[0]:.2f}.")
print(f"The minimum value for average temperature(in F) for a given day is {min_data[0]:.2f}.")
print(f"The mean value for average temperature(in F) for a given day is {mean_data[0]:.2f}.")
print("\n")

# Print the max, min, and mean for the second column (doesn't have much meaning because this is a boolean column)
print(f"The maximum value for if it rained/snow that day is {max_data[1]:.2f}.")
print(f"The minimum value for if it rained/snow that day  is {min_data[1]:.2f}.")
print(f"The mean value for if it rained/snow that day is {mean_data[1]:.2f}.")
print("\n")

# Print the max, min, and mean for the third column
print(f"The maximum value for number of sales (in U.S. Dollars) for a given day is {max_data[2]:.2f}.")
print(f"The minimum value for number of sales (in U.S. Dollars) for a given day is {min_data[2]:.2f}.")
print(f"The mean value for number of sales (in U.S. Dollars) for a given day is {mean_data[2]:.2f}.")
print("\n")

# You can access the max for sales specifically by indexing the array that is storing the max, min, and mean.
# The syntax would be the same for all three values. You would be indexing the max_data, min_data, and
# mean_data, at the 3rd element ([2]) which contains the max, min, and mean for sales.

# Max for sales only
print(f"Max sales: {max_data[2]}.")

# Min for sales only
print(f"Min sales: {min_data[2]}.")

# Mean for sales only
print(f"Mean sales: {mean_data[2]}.")

# d)

# This command will return a list that only contains True/False
print(weatherData[:,2]>500000)

# What this command will do is it will sum up all the True/False values in this list(True = 1, False = 0)
print(f"The sum is {np.sum(weatherData[:,2]>500000)}.")

# e)

# This command will find the values in the sales column that are more than 500,000, and the day wasn't snowing
# or raining and store it in more_than_500k.
more_than_500k = np.multiply(weatherData[:,2]>500000, weatherData[:, 0])

# Calculate the mean average average temperature of the days where sales are more than 500,000 and it was a dry day.
average_temp_500k = np.mean(more_than_500k)

# Print out the result
print(f"The average temperature(in F) for days where sales are more than 500,000 is {average_temp_500k:.2f}.")

# The average temperature on days that sales exceed 500,000 is lower than the average temperature
# on all days in the dataset.

# f)

# Convert Fahrenheit to Celsius
celsius = (weatherData[:,0] - 32) * (5/9)

# Check if the conversion worked by checking the first few elements
print(celsius[0:3])

# g)

# import Matplotlib.pyplot library
import matplotlib.pyplot as plt

# This plot tells about the trends of the sales, depending on the average temperature (in F) of that day.
# It seems like the higher the average temperature is on that day, the higher the sales would be too.
plt.scatter(weatherData[:,0],weatherData[:,2])

# This plot tells you the amount of sales made, depending if that day rained/snowed or not.
# It seems like more sales were made on the days where it was raining/snowing.
plt.scatter(weatherData[:,1],weatherData[:,2])

# h)

# To make plotting easier, I will store each column to a variable
avg_temp = weatherData[:,0]
weather = weatherData[:,1]
sales = weatherData[:,2]

# Plot the weather on x-axis and sales on y-axis, but if there was rain/snow on that day, use * marker,
# otherwise, use "o" marker.
for i in range(len(weatherData)):
    if weather[i] == 1:
        plt.scatter(avg_temp[i], sales[i], marker = "*")
    else:
        plt.scatter(avg_temp[i], sales[i], marker = "o")

# Plot the weather on x-axis and sales on y-axis, but if there was rain/snow on that day, use red color,
# otherwise, use green color.
for i in range(len(weatherData)):
    if weather[i] == 1:
        plt.scatter(avg_temp[i], sales[i], marker = "o", color = "r")
    else:
        plt.scatter(avg_temp[i], sales[i], marker = "o", color = "g")


# Analysis Answers

# 1) Both of the plots have the same trend and data points, just different color and shapes.
#    In both of the plots, there is a "positive association" between the two variables.
#    This means that when the average temperature increases, the sales would increase too. 
#    Additionally, dry days generally has higher sales than snowy/rainy days. However, because there are more
#    snowy/rainy days, their overall sales would be higher than dry days, despite dry days having higher sales.
# 2) The marker shapes and colors help me see the distinction between the days where it's 
#    raining/snowing very clearly. It also gives us extra information about the plot even though
#    the plot only has 2 variables. By having the markers and the colors be based on weather condition,
#    we gain more information about the plot where we can see trends on dry days and rainy days with respect to 
#    average temperature and sales where the plot doesn't look too messy.
# 3) Strength for markers: When the data point overlaps, you can still see the points clearly. Markers also
#    make the plot looks more interesting and aesthetically more beatiful and eye-catching.
#    Limitation for markers: In my opinion, markers seems a little too messy and are too much for a plot, especially
#    because they are in different colors(for this plot). They are also not too practical because some shapes can be small 
#    or similar which makes it hard to notice when presenting or just looking at the plot in general.
#    Strength for colors: Colors make a clear distinction between the two types of data and is very easy to see. Colors are generally
#    nicer when you are trying to present or just looking at the plot because of the clear distinction and how easy it is to notice the difference.
#    Limitation for colors: When the data point overlaps, you would not be able to see the data point because it's the same shape. The color that is
#    on the top will be the only one showing. Colors are not as aesthetically nice as shapes which may make the plot uninteresting or too boring for audiences.