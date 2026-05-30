# Import the necessary libraries for this assignment
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

# Read the NBA201516.csv file (I had to configure the directory, please change when you are running from
# your own environment)
nba201516 = pd.read_csv(r"C:/Users/vyduo/OneDrive/Desktop/Python BANA/PythonCodes/PythonCodes/homework/NBA201516.csv")

# Check if the csv file was loaded in properly
nba201516.head()

#
# 1)
#

# Let PS/G column from nba201516 be my y column (response variable)
y = nba201516["PS/G"]
y.head()

#
# 2)
#

# Select three predictors from the data frame: AST, STL, and MP
x = nba201516[["AST", "STL", "MP"]]
x.head()

#
# 3)
#

# Check if the dataframe really does have 476 rows
num_rows = len(nba201516)

# Print the results
print(f"This dataset has {num_rows} rows.")

#
# 4)
#

# Create random training and testing datasets where random_state = 1 and test data is 30% of total data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

x_train.shape
x_test.shape

#
# 5)
#

# Create a linear regression model object
model = LinearRegression()

# Fit the model using the training datasets
model.fit(x_train, y_train)


# Predict the response variable using both training dataset and testing dataset
y_train_hat = model.predict(x_train)
y_test_hat = model.predict(x_test)

# Store the coefficients from the fitted model (including the intercept)
coef_AST = model.coef_[0]
coef_STL = model.coef_[1]
coef_MP = model.coef_[2]
intercept = model.intercept_

# Print out the result of each coefficients (including the intercept)
print(f"The beta_0(intercept) coefficient for the fitted model is {intercept:.2f}.")
print(f"The beta_1(AST) coefficient for the fitted model is {coef_AST:.2f}.")
print(f"The beta_2(STL) coefficient for the fitted model is {coef_STL:.2f}.")
print(f"The beta_3(MP) coefficient for the fitted model is {coef_MP:.2f}.")

# These are the results:
# intercept = -2.3
# AST = 0.46
# STL = 0.11
# MP = 0.48

#
# 6)
#

# Interpret Intercept:
# When other predictors are 0 (meaning this person had no assists per game, no steals, and no minutes played), 
# then average predicted value for points per game would be -2.3. (This interpretation for intercept- 
# is not really significant because you can't score negative points in a game and it's impossible to- 
# have no minutes in a game.)

# Interpret beta_1 or AST's coefficient:
# When holding other predictors constant and this person had 1 assist per game, then the-
# average predicted value for their points per game would go up by 0.46 points per game.

# Interpret beta_2 or STL's coefficient:
# When holding other predictors constant and this person had 1 total steal per game, then the-
# average predicted value for their points per game would go up by 0.11 points per game.

# Interpret beta_3 or MP's coefficient:
# When holding other predictors constant and this person had 1 minute played per game, then the-
# average predicted value for their points per game would go up by 0.48 points per game.

#
# 7)
#

# Calculate evaluation metrics for training dataset
rmse_train = root_mean_squared_error(y_train, y_train_hat)
r2_train = r2_score(y_train, y_train_hat)

print(f"Training dataset's Root Mean Squared Error (RMSE): {rmse_train:.2f}")
print(f"Training dataset's R-squared Score: {r2_train:.2f}")

# Calculate evaluation metrics for testing dataset
rmse_test = root_mean_squared_error(y_test, y_test_hat)
r2_test = r2_score(y_test, y_test_hat)

print(f"Test dataset's Root Mean Squared Error (RMSE): {rmse_test:.2f}")
print(f"Test dataset's R-squared Score: {r2_test:.2f}")

# Both datasets evaluation's were very similar which suggests that this model is consistent.
# In addition, the R-squared score for the model is good and the RMSE is not high, 
# this indicates that this is model is a good fit for this dataset.