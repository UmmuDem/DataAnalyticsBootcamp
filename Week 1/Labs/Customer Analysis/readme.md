
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



# Lab | Customer Analysis Round 3
For this lab, we be using the marketing_customer_analysis.csv file. You can find the file in the files_for_lab folder. This is a combined file of the csv or excel files you combined yesterday for Customer Analysis round 1 and is the car insurance case study (possibly with more columns?)

### Get the data
Use the same jupyter file from the last lab, Customer Analysis Round 2 - if you didnt do round 2, you can also open a new jupyter notebook, and read in the csv data marketing_customer_analysis.csv and start from there.
### EDA (Exploratory Data Analysis) - Complete the following tasks to explore the data:
- Show DataFrame info.
- Describe DataFrame.
- Show a plot of the total number of responses (for each response type - "Yes"/"No").
- Show a plot of the rate of the response types by each Sales Channel.
- Show a plot of the distribution of the Total Claim Amount, broken down by response type. Try a boxplot and distribution plot, for each response type. For the distribution plot, try to plot both kinds of responses in one chart (seaborn's histplot, using the 'hue' parameter is very convenient here).
- Create similar plots like in the task before, but for Income.
- Create a scatterplot between Total Claim Amount and Income. Play around with the settings of the scatterplot (markersize, alpha level, ...) and in doing so try to identify more features within the data just visually. You can also try different seaborn plots. Check for example this link which explains how to avoid overplotting.



# Lab | Customer Analysis Round 4

In today's lesson we talked about continuous distributions (mainly normal distribution), linear regression and how multicollinearity can impact the model. In this lab, we will test your knowledge on those things using the `marketing_customer_analysis.csv` file. You have been using the same data in the previous labs (round 2 and 3). You can continue using the same jupyter file. The file can be found in the `files_for_lab` folder.

### Get the data 

Use the jupyter file from the last lab (Customer Analysis Round 3)

### Complete the following task 

- Check the data types of the columns. Get the numeric data into dataframe called `numerical` and categorical columns in a dataframe called `categoricals`.
(You can use np.number and np.object to select the numerical data types and categorical data types respectively)
- Now we will try to check the normality of the numerical variables visually
  - Use seaborn library to construct distribution plots for the numerical variables
  - Use Matplotlib to construct histograms
  - Do the distributions for different numerical variables look like a normal distribution 
- For the numerical variables, check the multicollinearity between the features. Please note that we will use the column `total_claim_amount` later as the target variable. 
- Drop one of the two features that show a high correlation between them (greater than 0.9). Write code for both the correlation matrix and for seaborn heatmap. If there is no pair of features that have a high correlation, then do not drop any features


# Lab | Predicting Claim Amount with ML Linear Regression

## Introduction

For this lab, we still keep using the [marketing_customer_analysis.csv file](marketing_customer_analysis.csv) - the US car insurance data set. You should be able to pick up where you left off in the previous rounds of customer behaviour analysis. However this time we will look to apply a linear regression machine learning model 

Review the previous rounds and follow the steps as shown in previous lectures.

## 01 - Problem (case study)
Familiarise yourself with Data Descriptions and the Goal.

## 02 - Getting Data
Read the .csv file into python

## 03 - Cleaning/Wrangling/EDA
Change headers names.
Deal with NaN values, replace with appropriate method. 

split categorical Features and Numerical Features.

Explore visually both sets of features, to identify next steps.

Look at potential multicollinearity using a correlation matrix or other approach. 

## 04 - Pre-Processing Data
Dealing with outliers.
Normalization - ie use chosen scaler to transform selected columns into normal distribution as needed for linear regression model. Propose: MinMax scaler on 'effective_to_date' and standard scaler on numerical columns.

Encoding Categorical Data fields using OHE.

Bring categorical and numerical columns back together using pd.concat.

Define X and y, the y value you are seeking to predict is claim amount.

Splitting into train set and test dataset using random state, eg 80%:20% .

## 05 - Modeling
Apply linear regression model from sklearn.linear_model.

Fit over your train data and predict against X test. 

## 06 - Model Validation
You should gather appropriate metrics to evaluate model accuracy over y_test- such as : 
R2.
MSE.
RMSE.
MAE.

## 07 - Reporting
Present results inside your notebook with appropriate annotation describing the accuracy of the model and business insight gained.

