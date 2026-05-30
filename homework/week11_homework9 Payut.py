# Answers to Homework 9

# Import pandas library as pd
import pandas as pd

# Use pd.read_csv to read in the PCSales.csv file
PCSales = pd.read_csv("PCSales.csv")

#
# For prompt a)
#

# Print the first 5 rows of the dataframe (you can also use PCSales.head(5))
PCSales[:5]

#
# For prompt b)
#

# Print out the column names
print(PCSales.columns)

#
# For prompt c)
#

# Calculate the average profit
profit_mean = PCSales["Profit"].mean()

# Print out the average profit
print(f"The average profit is {profit_mean:.2f}.")

#
# For prompt d)
#

# In this prompt, I wanted to try both ways of filtering using .loc and dataframe slicing
# I also wasn't sure if you wanted Product Type or ID, so I gave both

# Find the max profit
max_profit = PCSales["Profit"].max()

# Find the index or indexes that contains the value the same as max_profit
max_index = PCSales.index[PCSales["Profit"] == max_profit]

# Filter the profit column where it equals to max_profit and show the Product Type column with the filtered rows
prod_max_type = PCSales[PCSales["Profit"] == max_profit]["Product Type"]

# Use the index to filter the rows where profit is equal to max_profit, but this time, choose Product ID as the column
prod_max_id = PCSales.loc[max_index, "Product ID"]

# Print out the results
print(prod_max_type)
print(prod_max_id)

#
# For prompt e)
#

# Filter rows where state is West Virginia and count the occurences
# (["State"] at the end can be any other columns, I used it so it only shows one column
# and count only from that column)
wv_count = PCSales[PCSales["State"] == "WV"]["State"].count()

# Print out the result
print(f"The number of purchases from West Virgina is {wv_count}.")

#
# For prompt f)
#

# Filter rows where Year is equal to 2019 and count the occurences
# ["Product ID"] is used for the same reason as the ["State"] from prompt e)
purchase_2019 = PCSales[PCSales["Year"] == 2019]["Product ID"].count()

# Print out the result
print(f"The number of purchases from 2019 is {purchase_2019}.")

#
# For prompt g)
#

# Use groupby to group the product types and count the occurences in each type
# ["Product ID"] is used for the same reason as the ["State"] and ["Product ID"] from
# prompt e) and prompt f)
PCSales.groupby("Product Type")["Product ID"].count()

#
# For prompt h)
#

# Get the list of customers where the product id that they bought was M01-F0024
PCSales[PCSales["Product ID"] == "M01-F0024"]["Contact"]

#
# For prompt i)
#

# Count the Website purchases that made the profit over 150

# Filter the rows where Lead is equal to Website
lead_web = PCSales[PCSales["Lead"] == "Website"]

# Filter the previous data frame where its profit is more than 150
prof_150 = lead_web[lead_web["Profit"] > 150]

# Count how many rows were in the "Contact" column (we can use any column, but I chose this column)
count_filtered = prof_150["Contact"].count()

# Print out the results
print(f"The number of website purchases that had a profit over 150 is {count_filtered}.")