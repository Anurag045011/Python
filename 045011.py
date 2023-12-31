# -*- coding: utf-8 -*-
"""045011.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_5ijp6afABIuW5VtWm6lFMcmGXhjSNK
"""

'''
Solve the Equation
Eq1 : x + y + z = 2 | Eq2 : 6x - 4y + 5z = 31 | Eq3: 5x + 2y + 2z = 13

'''

import numpy as np
from numpy import linalg as npla

# Coefficients of the equations
coefficients = np.array([[1, 1, 1], [6, -4, 5], [5, 2, 2]])
constants = np.array([2, 31, 13])

# Solve the system of equations
solution = npla.linalg.solve(coefficients, constants)

x, y, z = solution
print("Solution using NumPy:")
print("x =", x)
print("y =", y)
print("z =", z)

'''
Q2
'''
emp_dict={'Name':['ABC','DEF','GHI','JKL','MNO','PQR','STU'],
          'Education':['Graduate','Postgraduate','Postgraduate','Graduate','Graduate','Postgraduate','Graduate'],
          'Gender':['Make','Female','Male','Other','Female','Female','Male']

}
emp_dict

'''
 Update the Employee Dictionary 'emp_dict' with following Information:
'''
emp_dict['Age']= 22,27,26,23,24,30,21 #added age as a key and different age as a value
emp_dict

#Ans 3
import pandas as pd

# 3.1 Create the DataFrame 'emp_df' from the Dictionary 'emp_dict'
emp_dict = {
    'Name': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU'],
    'Education': ['Graduate', 'Postgraduate', 'Postgraduate', 'Graduate', 'Graduate', 'Postgraduate', 'Graduate'],
    'Gender': ['Male', 'Female', 'Male', 'Other', 'Female', 'Female', 'Male'],
    'Age': [22, 27, 26, 23, 24, 30, 21]
}

emp_df = pd.DataFrame(emp_dict)

# 3.2 Update the DataFrame 'emp_df' with Salary_Lakhs and Bonus% information
salary_lakhs = [6, 15, 20, 5, 10, 18, 12]
bonus_percent = [12.50, 8.75, 6.25, 10.20, 13.60, 11.40, 9.80]

emp_df['Salary_Lakhs'] = salary_lakhs
emp_df['Bonus%'] = bonus_percent

# 3.3 Update the DataFrame 'emp_df' with additional information
new_data = {
    'Name': ['VWX', 'YZA', 'BCD'],
    'Education': ['Postgraduate', 'Graduate', 'Postgraduate'],
    'Gender': ['Male', 'Female', 'Other'],
    'Age': [35, 28, 32],
    'Salary_Lakhs': [14, 7, 8],
    'Bonus%': [5.50, 7.75, 14.80]
}

emp_df = emp_df.append(pd.DataFrame(new_data), ignore_index=True)

# 3.4 Create a Column 'Gross_Salary_Lakhs' using the formula
emp_df['Gross_Salary_Lakhs'] = emp_df['Salary_Lakhs'] * (1 + emp_df['Bonus%'] / 100)

# Print the updated 'emp_df'
print(emp_df)

#Q4
# Create a Subset 'emp_df_ss' with specified variables
emp_df_ss = emp_df[['Name', 'Age', 'Gross_Salary_Lakhs']]

# Print the subset DataFrame 'emp_df_ss'
print(emp_df_ss)

#Q5
# 5.1 Create a Copy of 'emp_df' Named as 'emp_df_age_sorted' and Sort by 'Age' (Highest to Lowest)
emp_df_age_sorted = emp_df.copy()
emp_df_age_sorted = emp_df_age_sorted.sort_values(by='Age', ascending=False)

# 5.2 Create a Copy of 'emp_df' Named as 'emp_df_age_salary_sorted' and Sort by 'Age' (Lowest to Highest) and 'Gross_Salary_Lakhs' (Highest to Lowest)
emp_df_age_salary_sorted = emp_df.copy()
emp_df_age_salary_sorted = emp_df_age_salary_sorted.sort_values(by=['Age', 'Gross_Salary_Lakhs'], ascending=[True, False])

# Print the sorted DataFrames
print("Sorted by Age (Highest to Lowest):")
print(emp_df_age_sorted)

print("\nSorted by Age (Lowest to Highest) and Gross_Salary_Lakhs (Highest to Lowest):")
print(emp_df_age_salary_sorted)

#Q6
# 6.1 Create a DataFrame 'emp_df_filtered' by filtering 'emp_df' based on 'Age' >= 25 and 'Gender' == 'Female'
emp_df_filtered = emp_df[(emp_df['Age'] >= 25) & (emp_df['Gender'] == 'Female')]

# 6.2 Create subsets 'emp_df_grad' and 'emp_df_postgrad' based on 'Education' column
emp_df_grad = emp_df[emp_df['Education'] == 'Graduate']
emp_df_postgrad = emp_df[emp_df['Education'] == 'Postgraduate']

# Print the filtered DataFrame and subsets
print("Filtered DataFrame (Age >= 25 and Gender = Female):")
print(emp_df_filtered)

print("\nSubset 'emp_df_grad' (Education == Graduate):")
print(emp_df_grad)

print("\nSubset 'emp_df_postgrad' (Education == Postgraduate):")
print(emp_df_postgrad)

#Q7
# 7.1 Inner Merge 'emp_df_grad' and 'emp_df_postgrad' on 'Gender' with selected variables
emp_df_merged = pd.merge(emp_df_grad[['Name', 'Gender', 'Age']],
                         emp_df_postgrad[['Name', 'Gender', 'Gross_Salary_Lakhs']],
                         on='Gender',
                         how='inner')

# Print the merged DataFrame 'emp_df_merged'
print(emp_df_merged)

#Q8
# 8.1 Group 'emp_df' by 'Gender' and 'Education' and count employees
emp_df_gen_edu = emp_df.groupby(['Gender', 'Education']).size().reset_index(name='Count')

# 8.2 Group 'emp_df' by 'Gender' and calculate the average of 'Age' and 'Gross_Salary_Lakhs'
emp_df_gen_age_sal = emp_df.groupby('Gender').agg({'Age': 'mean', 'Gross_Salary_Lakhs': 'mean'}).reset_index()

# Print the grouped tables
print("Table 'emp_df_gen_edu' (Count of Employees by Gender and Education):")
print(emp_df_gen_edu)

print("\nTable 'emp_df_gen_age_sal' (Average Age and Gross_Salary_Lakhs by Gender):")
print(emp_df_gen_age_sal)

#Q9
import pandas as pd

# Create the cross-sectional dataframe 'df_cross_section'
data = {
    'Company': ['ZYX', 'WVU', 'TSR'],
    '2023': [123, 456, 789],
    '2024': [321, 654, 987]
}

df_cross_section = pd.DataFrame(data)

# Melt the cross-sectional dataframe into a panel dataframe 'df_panel'
df_panel = pd.melt(df_cross_section, id_vars=['Company'], var_name='Year', value_name='Profit')

# Sort the panel dataframe by 'Company' and 'Year' if needed
df_panel = df_panel.sort_values(by=['Company', 'Year'])

# Reset the index
df_panel = df_panel.reset_index(drop=True)

# Print the panel dataframe 'df_panel'
print(df_panel)