# Case-Study-Classification

Mid-Bootcamp-Project

by Ümmühan Demir and Thomas Maechler November 2021

We want to be able to predict which client will **accept** credit card offers. 📈💰💸

![Picture](images/banking-project.jpeg)





## Table of Contents


- [Project Brief](https://github.com/thomasmaechler/Case-Study-Classification#Project-Brief)
- [Data](https://github.com/thomasmaechler/Case-Study-Classification#Data)
- [Process](https://github.com/thomasmaechler/Case-Study-Classification#Process)
- [Tools](https://github.com/thomasmaechler/Case-Study-Classification#Tools)
- [Key Take Aways](https://github.com/thomasmaechler/Case-Study-Classification#Key-Take-Aways)


Kml
## Project Brief


**Scenario**: We are working as a risk analyst with a bank. Apart from the other banking and loan services, the bank also provides credit card services that are a very important source of revenue for the bank. The bank wants to understand the demographics and other characteristics of its customers that accept a credit card offer and that do not accept a credit card.


**Objective**: Build a model that will provide insight into why some bank customers accept credit card offers. There are also other potential areas of opportunities that the bank wants to understand from the data.



## Data 


**The data set**: 18,000 current bank customers in the study. 

**Features**: Customer Number | Offer Accepted | Mailer Type | Income Level | Bank Accounts Open | Overdraft Protection | Credit Rating  | Credit Cards Held | Homes Owned | Household Size | Own Your Home | Average Balance | Q1 Balance | Q2 Balance | Q3 Balance | Q4 Balance



## Process: 


- 1 - We tried to visualize how the data looks like in [SQL Workbench](https://github.com/thomasmaechler/Case-Study-Classification/blob/main/SQL/mid_bootcamp_project.sql).

- 2 - We used [Tableau](https://public.tableau.com/app/profile/thomas.maechler/viz/Case-Study-Classification_16369900928240/Dashboard1) to get some graphs to better understand how the data is set. We noticed that we had the imbalance data problem.

- 3 - After understanding better how the data looks like, we started to manipulate the data in Python through this process: 

<img width="461" alt="Screenshot 2021-11-18 at 14 56 12" src="https://user-images.githubusercontent.com/90766942/142428776-2e0dd4b0-d0a8-4b8f-9606-54d19facf517.png">


  - After we read our data in **Python**, as we had already seen in **Tableau**, it was an imbalanced data so it was noted that we had to be careful about minority class.
  - Then started to exploratory data analysis (EDA). 
  - First standardized column names were obtained to make coding easier later.
  - We removed nulls because they are not a lot and most of them are from majority class.
  - We removed 'customer number' as it is quite irrelevant. 
  - We converted some numerical columns into categorical since they are too discrete in a restricted range.
  - We checked correlations between numerical columns, and noticed that they are highly correlated. Because of that, we also checked out variation inflation factors(VIFs) for those columns to go further. 
  - Then we decided to remove some of them to keep VIFs in acceptable range (1-5).
  - We tried a lot of different combination of categorical columns, at the end decided to remove 'no_of_bank_accounts_open', 'q2_balance',  'q3_balance', 'q4_balance', 'no_of_homes_owned', 'no_of_credit_cards_held', 'household_size'.
  - When we were on dealing the outliers part, a dilemma came out. If we removed the outliers, it would diminish our minority class even more. 
  - Because of that we created two jupyter notebooks, with and without outliers, to see the effect of them.
  - As we suspected, we get a bit worse results without outliers.
  - Then we continued with the preprocessing numerical and categorical columns. 
  - We used **Normalizer()**, **StandardScaler()** and **MinMaxScaler** to scale numerical columns and tried all of them for our models to see which one will give us better accuracy scores. We decided to go with **Normalizer** with outliers, and **MinMaxScaler** without outliers.
  - Categorical columns converted into numerical by using **pd.get_dummies()**. 
  - After Concatanating scaled numerical columns and now-numeric categorical columns, we were ready to apply some models.
  - We applied five models on with/without outliers. As it was an imbalanced data, we had to implement sampling methods.
    * Model 1: Logistic Regression
    
<img width="376" alt="Screenshot 2021-11-18 at 15 59 26" src="https://user-images.githubusercontent.com/90766942/142440217-e03a01e0-c683-4416-9809-50d41c7290cd.png">


    * Model 2: Logistic Regression + SMOTE
    
   <img width="372" alt="Screenshot 2021-11-18 at 16 01 16" src="https://user-images.githubusercontent.com/90766942/142440282-ff7d2440-e8a5-4bb8-9437-cba8ff35424c.png">

    
    * Model 3: Logistic Regression + Tomek Links
    
    <img width="364" alt="Screenshot 2021-11-18 at 16 01 42" src="https://user-images.githubusercontent.com/90766942/142440376-95e08255-7379-4aaa-942e-6f73ff3b45b6.png">

    
    * Model 4: Logistic Regression + SMOTE + Tomek Links 
    
    <img width="374" alt="Screenshot 2021-11-18 at 16 02 13" src="https://user-images.githubusercontent.com/90766942/142440461-95e45151-b73b-4cc6-b20a-00be4481b28b.png">

    
    * Model 5: Logistic Regression + KNN Classifier
    
    <img width="369" alt="Screenshot 2021-11-18 at 16 02 27" src="https://user-images.githubusercontent.com/90766942/142440498-19415d03-038f-45b0-975c-09a087443319.png">

 - We evaluated the results by looking at confusion matrix, AUC scores and F1 scores to decide which model would be the best at predicting offer responses.

  
  
  
## Tools 


- **Database**: [MySQLWorkbench](https://github.com/thomasmaechler/Case-Study-Classification/tree/main/SQL) 

- **Vizualizations**: [Tableau](https://public.tableau.com/authoring/Case-Study-Classification_16369900928240/Dashboard1#1) / Seaborn / matplotlib

- **Code**: Jupyter Notebook



## Useful Links about This Repo

You can find the data that we tried to analyze [here](https://github.com/thomasmaechler/Case-Study-Classification/tree/main/Data%20Sources)

[This](https://public.tableau.com/app/profile/thomas.maechler/viz/Case-Study-Classification_16369900928240/Dashboard1) leads you to the Tableau public workbook and the dashboard we created to get some insight about the data.

[This folder](https://github.com/thomasmaechler/Case-Study-Classification/tree/main/SQL) is dedicated for **SQL** part of this project.

[Here](https://github.com/thomasmaechler/Case-Study-Classification/tree/main/Jupyter%20Notebooks) we collected our jupyter notebooks, feel free to work on them.

Thank you for checking our repo.
