import numpy as np
import streamlit as st
import pandas as pd

a = int(input("How many past exams' data do you intend to share, it is recomended to provide as many as possible for a more accurate analysis"))
b=[]

for i in range(a):
  print("enter results for exam ", {i+1})

subject=i

import numpy as np
import pandas as pd

# 1. Ask the user how big the table should be
num_rows = int(input("How many rows of data do you want to enter? "))

rows_list = []

# 2. Collect data row by row using a loop ('i' keeps track of the current row)
for i in range(num_rows):
    print(f"\n--- Entering data for Row {i+1} ---")
    
    # Take user inputs as integers
    age = int(input("Enter Age: "))
    salary = int(input("Enter Salary: "))
    score = int(input("Enter Score: "))
    
    # Store this row as a small list
    current_row = [age, salary, score]
    rows_list.append(current_row)

# 3. Convert the collected list into a strict NumPy integer array
numpy_table = np.array(rows_list, dtype=int)

# 4. Throw it into a clean Pandas DataFrame
df = pd.DataFrame(numpy_table, columns=['Age', 'Salary', 'Score'])

print("\nHere is your final Integer DataFrame:")
print(df)

