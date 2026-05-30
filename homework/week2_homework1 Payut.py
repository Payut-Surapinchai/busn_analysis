# Answer to Question 1

# Constant profit rate.
PROFIT_RATE = 0.23

# Get user's input for the projected amount of total sales.
total_sales = float(input("Enter the projected amount of total sales: "))

# Calculate the annual profit.
annual_profit = total_sales * PROFIT_RATE

# Display the annual profit
print(f"The profit that will be made from the projected amount of total sales is {annual_profit:,.2f}.")

# Answer to Question 2

# Constant sales tax.
SALES_TAX = 0.07

# Get user's input for each item's price.
price_item1 = float(input("Enter the price of the first item: "))
price_item2 = float(input("Enter the price of the second item: "))
price_item3 = float(input("Enter the price of the third item: "))
price_item4 = float(input("Enter the price of the fourth item: "))
price_item5 = float(input("Enter the price of the fifth item: "))

# Calculate the subtotal.
subtotal = price_item1 + price_item2 + price_item3 + price_item4 + price_item5

# Calculate the subtotal's tax.
subtotal_tax = subtotal * SALES_TAX

# Calculate the total price.
total_price = subtotal + subtotal_tax

# Display the total price.
print(f"The final price of these 5 items including tax is {total_price:.2f}.")

# Answer to Question 3

# Calculate the distances of each hours.
car_6hrs = 70 * 6
car_10hrs = 70 * 10
car_15hrs = 70 * 15

# Display the distances.
print(f"In 6 hours, the car will travel {car_6hrs} miles.")
print(f"In 10 hours, the car will travel {car_10hrs} miles.")
print(f"In 15 hours, the car will travel {car_15hrs} miles.")

# Answer to Question 4

# Constant state & county sales tax.
STATE_SALES_TAX = 0.05 
COUNTY_SALES_TAX = 0.025

# Get user's input for the amount of their purchase.
purchase_amount = float(input("Enter the amount of your purchase: "))

# Calculate the state & county tax.
state_tax = purchase_amount * STATE_SALES_TAX
county_tax = purchase_amount * COUNTY_SALES_TAX

# Calculate the total tax.
total_tax = state_tax + county_tax

# Calculate the final amount(purchase + tax).
final_amount = purchase_amount + total_tax

# Display all the information calculated above and the user's input.
print(f"The amount of the purchase is {purchase_amount:.2f}.")
print(f"The amount of the state sales tax is {state_tax:.2f}.")
print(f"The amount of the county sales tax is {county_tax:.2f}.")
print(f"The amount of the total sales tax is {total_tax:.2f}.")
print(f"The amount of the total sale is {final_amount:.2f}.")

# Answer to Question 5

# Constant tip percentage and food sales tax.
TIP_PERCENT = 0.18
FOOD_SALES_TAX = 0.07

# Get user's input for the price of the food charged.
food_charged = float(input("Enter the price of the food charged: "))

# Calculate the food tip, food tax, and the total charges for the food.
food_tip = food_charged* TIP_PERCENT
food_tax = food_charged* FOOD_SALES_TAX
total_charges = food_charged + food_tip + food_tax

# Display all the information calculated above and the user's input.
print(f"The price of the food charged is {food_charged:.2f}.")
print(f"The cost for tipping is {food_tip:.2f}.")
print(f"The cost of the food tax is {food_charged:.2f}.")
print(f"The total price of the food is {total_charges:.2f}.")

# Answer to Question 6

# Get user's input for the temperature in Celsius.
celsius_temp = float(input("Enter the temperature(in Celsius) to convert to Fahrenheit: "))

# Calculate the temperature in Fahrenheit.
fahrenheit_temp = (9/5 * celsius_temp) + 32

# Display the result.
print(f"{celsius_temp} Celsius in Fahrenheit is {fahrenheit_temp:.2f}.")

# Answer to Question 7

# Constant number of shares, the buying price, the selling price, and the commission rate.
NUMBER_OF_SHARES = 2000
BUYING_PRICE = 40
SELLING_PRICE = 42.75
COMMISSION = 0.03

# Calculate the price for buying the stocks, broker's commission for buying the stocks, 
# and the total costs for buying the stocks.
buy_stocks = NUMBER_OF_SHARES * BUYING_PRICE
buy_commission = buy_stocks * COMMISSION
total_buy = buy_stocks + buy_commission

# Calculate the price for selling the stocks, broker's commission for selling the stocks, 
# and the total costs for selling the stocks.
sell_stocks = NUMBER_OF_SHARES * SELLING_PRICE
sell_commission = sell_stocks * COMMISSION
total_sell = sell_stocks - sell_commission

# Calculate the leftover money that Joe has.
money_left = total_sell - total_buy

# Display the information about buying the stocks, broker's commission for buying the stocks,
# selling the stocks, and broker's commission for selling the stocks.
print(f"Joe paid {buy_stocks:.2f} dollars for the stocks, excluding commission.")
print(f"Joe paid {buy_commission:.2f} dollars for the commission when he bought the stocks.")
print(f"Joe sold the stocks and got {sell_stocks:.2f} dollars, excluding commission.")
print(f"Joe paid {sell_commission:.2f} dollars for the selling commission to his broker.")

# I wanted to do else-if statements for this part.

# If the leftover money is positive, then Joe made a profit.
if money_left > 0:

    # Display the profit money that Joe made.
    print(f"Joe made a profit of {money_left:.2f} dollars after selling his stocks.")

# If the leftover money is 0, then Joe did not make any profit. 
elif money_left == 0:

    # Display that Joe did not make any money.
    print(f"Joe did not make any money.")

# If the leftover money is less than 0, then Joe lost his money.
else:
    # Make sure the money does not have a negative sign infront because I want to display in the print function
    # and I don't want a negative sign infront of it.
    # abs() is used to remove the negative sign(absolute value function).
    amt_money_lost = abs(money_left)

    # Display how much money Joe lost.
    print(f"Joe lost {amt_money_lost:.2f} dollars after selling his stocks.")

# Answer to Question 8

# Get user's input for the principal, interest rate, times per year that the interest rate is compounded
# and number of years to earn interest.
principal = float(input("Enter the principal deposited into your account: "))
interest_rate = float(input("Enter the annual interest rate: "))
times_compounded = float(input("Enter the number of times per year that the interest rate is compounded: "))
num_years = float(input("Enter the number of years to earn interest: "))

# Calculate the account balance after those number of years.
account_balance = principal * ((1 + (interest_rate / times_compounded)) ** (times_compounded * num_years))

# Display the final account balance after the years input by the user.
print(f"The account balance after {num_years} year(s) is {account_balance:.2f}.")