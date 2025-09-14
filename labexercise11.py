#Question 1

import pandas as pd

data = {"name": ["Alice", "bob", "charlie"], "age": [24, 27, 22], "city": ["new york", "london", "paris"]}
s = pd.DataFrame(data)
print(s)


#Question 2

import pandas as pd
df = pd.read_csv('student.csv')
print(df)
print(df.to_string())


# Question 3

import pandas as pd
df = pd.read_csv('student.csv')
print(df.head(3))

print(df.columns.tolist())

print(df.dtypes)


#Question 4

import pandas as pd
df = pd.read_csv('student.csv')
k = df["Age"]
print(k)


#Question 5

import pandas as pd
df = pd.read_csv('student.csv')
k = df.loc[df['Age'] > 23]
print(k)


#Question 6

import pandas as pd
df = pd.read_csv('student.csv')
df['marks'] = [85, 90, 78, 99, 89]
print(df)


#Question 7

import pandas as pd

df = pd.read_csv('student.csv')
print(df['Age'].min())
print(df['Age'].max())
print(df['Age'].mean())


#Question 8 

import pandas as pd
df = pd.read_csv('student.csv')
df['marks'] = [85, 90, 78, 99, 89]
df.to_csv('student.csv', index=False)
k = df.sort_values(by='marks', ascending=False)
print(k)


# Question 9

import pandas as pd
df = pd.read_csv('student.csv')
arr = df.groupby('City')
arr1 = arr['Age'].mean()
print(arr1)


# Question 10

import pandas as pd
df = pd.read_csv('student.csv')
k = df.to_csv('output.csv', index= False)
print(k)


#Question 11

import pandas as pd
df = pd.read_csv('Salaries.csv')

CASE1
print(df.head())

CASE2
print(df.info())

CASE3
arr = pd.to_numeric(df['BasePay'], errors='coerce')
print(arr.mean())

CASE4
arr = pd.to_numeric(df['OvertimePay'], errors='coerce')
print(arr.max())

CASE5
arr = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
print(arr[['EmployeeName', 'JobTitle']])

CASE6
arr = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
print(arr[['EmployeeName', 'TotalPayBenefits']])

CASE7
arr = df.loc[df['TotalPayBenefits'].idxmax()]
print(arr[['EmployeeName','TotalPayBenefits']])

CASE8
arr = df.loc[df['TotalPayBenefits'].idxmin()]
print(arr[['EmployeeName','TotalPayBenefits']])

CASE9
df['BasePay'] = pd.to_numeric(df['BasePay'], errors='coerce')
group = df.groupby('Year')
arr = group['BasePay'].mean()
print(arr)

CASE10
arr = df['JobTitle'].value_counts()
print(len(arr))

CASE11
arr = df['JobTitle'].value_counts()
print(arr.head())

CASE12
arr = df[df['Year'] == 2013]
arr1 = arr['JobTitle'].value_counts()
arr2 = arr1 == 1
print(arr2.sum())

