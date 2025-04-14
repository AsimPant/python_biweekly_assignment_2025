'''
8. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

'''

import pandas as pd

# Creating two Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([5, 4, 3, 2, 1])

# Addition
addition_result = series1 + series2
print("Addition of Series:\n", addition_result)

# Subtraction
subtraction_result = series1 - series2
print("\nSubtraction of Series:\n", subtraction_result)

# Multiplication
multiplication_result = series1 * series2
print("\nMultiplication of Series:\n", multiplication_result)

# Division
division_result = series1 / series2
print("\nDivision of Series:\n", division_result)
