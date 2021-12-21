
# Lab | Customer Analysis Round 1

#### Remember the process:

1. Case Study
2. Get data
3. Cleaning/Wrangling/EDA
4. Processing Data
5. Modeling
6. Validation
7. Reporting

### Abstract

The objective of this data is to understand customer demographics and buying behavior. Later during the week, we will use predictive analytics to analyze the most profitable customers and how they interact. After that, we will take targeted actions to increase profitable customer response, retention, and growth.

For this lab, we will gather the data from 3 _csv_ files that are provided in the `files_for_lab` folder. Use that data and complete the data cleaning tasks as mentioned later in the instructions.

### Instructions

- Read the three files into python as dataframes
- Show the DataFrame's shape.
- Standardize header names.
- Rearrange the columns in the dataframe as needed
- Concatenate the three dataframes
- Which columns are numerical?
- Which columns are categorical?
- Understand the meaning of all columns
- Perform the data cleaning operations mentioned so far in class

  - Delete the column education and the number of open complaints from the dataframe.
  - Correct the values in the column customer lifetime value. They are given as a percent, so multiply them by 100 and change `dtype` to `numerical` type.
  - Check for duplicate rows in the data and remove if any.
  - Filter out the data for customers who have an income of 0 or less.




# Lab | Customer Analysis Round 2

For this lab, we will be using the `marketing_customer_analysis.csv` file that you can find in the `files_for_lab` folder. Check out the `files_for_lab/about.md` to get more information if you are using the Online Excel.

**Note**: For the next labs we will be using the same data file. Please save the code, so that you can re-use it later in the labs following this lab.

### Dealing with the data

1. Show the dataframe shape.
2. Standardize header names.
3. Which columns are numerical?
4. Which columns are categorical?
5. Check and deal with `NaN` values.
6. Datetime format - Extract the months from the dataset and store in a separate column. Then filter the data to show only the information for the first quarter , ie. January, February and March. _Hint_: If data from March does not exist, consider only January and February.
7. BONUS: Put all the previously mentioned data transformations into a function.

