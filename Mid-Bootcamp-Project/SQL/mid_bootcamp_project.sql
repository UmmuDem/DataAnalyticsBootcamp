# SQL Questions - Classification


# 1. Create a database called `credit_card_classification`.

drop database if exists credit_card_classification ;
create database credit_card_classification;

# 2. Create a table `credit_card_data` with the same columns as given in the csv file. 
# Please make sure you use the correct data types for each of the columns.

use credit_card_classification;
drop table if exists credit_card_classification.credit_card_data;


CREATE TABLE credit_card_data (
    credit_card_data_id INT AUTO_INCREMENT NOT NULL,
    customer_number INT DEFAULT NULL,
    offer_accepted VARCHAR(5) DEFAULT NULL,
    reward VARCHAR(20),
    mailer_type VARCHAR(10),
    income_level VARCHAR(10),
    no_of_account_open INT,
    overdraft_protection VARCHAR(10),
    credit_card_rating VARCHAR(10),
    no_of_credit_cards_held INT,
    homes_owned INT,
    household_size INT,
    own_your_home VARCHAR(10),
    average_balance FLOAT DEFAULT NULL,
    q1_balance FLOAT DEFAULT NULL,
    q2_balance FLOAT DEFAULT NULL,
    q3_balance FLOAT DEFAULT NULL,
    q4_balance FLOAT DEFAULT NULL,
    PRIMARY KEY (credit_card_data_id)
);

# 3. Import the data from the csv file into the table. 
# Before you import the data into the empty table, make sure that you have deleted the headers from the csv file. 
# To not modify the original data, if you want you can create a copy of the csv file as well. 
# Note you might have to use the following queries to give permission to SQL to import data from csv files in bulk:

SHOW VARIABLES LIKE 'local_infile'; -- This query would show you the status of the variable ‘local_infile’. 
                                    -- If it is off, use the next command, otherwise you should be good to go
SET GLOBAL local_infile = 1;


LOAD DATA LOCAL INFILE 'creditcardmarketing.csv' 
INTO TABLE credit_card_data             
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


# 4.  Select all the data from table `credit_card_data` to check if the data was imported correctly.

SELECT 
    *
FROM
    credit_card_data;


# 5.  Use the _alter table_ command to drop the column `q4_balance` from the database, as we would not use it in the analysis with SQL. Select all the data from the table to verify if the command worked. Limit your returned results to 10.

ALTER TABLE credit_card_data 
DROP q4_balance;

SELECT 
    *
FROM
    credit_card_data
LIMIT 10;


# 6.  Use sql query to find how many rows of data you have.

SELECT 
    COUNT(customer_number) AS 'Number of customer'
FROM
    credit_card_data;


# 7.  Now we will try to find the unique values in some of the categorical columns:

    # - What are the unique values in the column `Offer_accepted`?
    
SELECT DISTINCT
    offer_accepted AS 'Offer Accepted'
FROM
    credit_card_data;
    
    
    # - What are the unique values in the column `Reward`?
    
SELECT DISTINCT
    reward AS 'Type of rewards'
FROM
    credit_card_data;
    
    
    # - What are the unique values in the column `mailer_type`?
    
	SELECT 
    DISTINCT mailer_type as 'Type of mail'
FROM
    credit_card_data;
    
    
    # - What are the unique values in the column `credit_cards_held`?
    
	SELECT DISTINCT
    no_of_credit_cards_held AS 'n° of credit cards held'
FROM
    credit_card_data;

    
    # - What are the unique values in the column `household_size`?
    
	SELECT DISTINCT
    household_size AS 'Size of household'
FROM
    credit_card_data;


# 8. Arrange the data in a decreasing order by the `average_balance` of the house. Return only the `customer_number` of the top 10 customers with the highest `average_balances` in your data.

SELECT 
    customer_number AS 'customer n°'
FROM
    credit_card_data
ORDER BY average_balance DESC
LIMIT 10;


# 9.  What is the average balance of all the customers in your data?

SELECT 
    AVG(average_balance) AS 'Average of the average balance'
FROM
    credit_card_data;


# 10. In this exercise we will use simple group by to check the properties of some of the categorical variables in our data. Note wherever `average_balance` is asked, please take the average of the column `average_balance`: <!-- 🚨🚨🚨 @himanshu - can we rephrase this? -->

    # - What is the average balance of the customers grouped by `Income Level`? 
    # The returned result should have only two columns, income level and `Average balance` of the customers. 
    # Use an alias to change the name of the second column.
  
SELECT 
    income_level AS 'Income level',
    ROUND(AVG(average_balance), 2) AS 'Average balance'
FROM
    credit_card_data
GROUP BY income_level;
  
    
    # - What is the average balance of the customers grouped by `number_of_bank_accounts_open`? 
    # The returned result should have only two columns, `number_of_bank_accounts_open` and `Average balance` of 
    # the customers. Use an alias to change the name of the second column.

SELECT 
    no_of_account_open AS 'Number of account open',
    ROUND(AVG(average_balance), 2) AS 'Average balance'
FROM
    credit_card_data
GROUP BY no_of_account_open;
    
    
    # - What is the average number of credit cards held by customers for each of the credit card ratings? 
    # The returned result should have only two columns, rating and average number of credit cards held. 
    # Use an alias to change the name of the second column.
    
SELECT 
    credit_card_rating AS 'Credit card rating',
    ROUND(AVG(no_of_credit_cards_held), 2) AS 'avg number of credit cards held'
FROM
    credit_card_data
GROUP BY credit_card_rating;
    
 
    # - Is there any correlation between the columns `credit_cards_held` and `number_of_bank_accounts_open`? 
    # You can analyse this by grouping the data by one of the variables and then aggregating the results of 
    # the other column. Visually check if there is a positive correlation or negative correlation or no correlation
    # between the variables.
    
SELECT 
    no_of_account_open AS 'Number of account open',
    AVG(no_of_credit_cards_held) AS 'avg number of credit cards held'
FROM
    credit_card_data
GROUP BY no_of_account_open;


# 11. Your managers are only interested in the customers with the following properties:
    # - Credit rating medium or high
    # - Credit cards held 2 or less
    # - Owns their own home
    # - Household size 3 or more
    
SELECT 
    customer_number AS 'customer n°'
FROM
    credit_card_data
WHERE
    credit_card_rating IN ('medium' , 'high')
        AND no_of_credit_cards_held <= 2
        AND own_your_home = 'yes'
        AND household_size >= 3;
    
    

# For the rest of the things, they are not too concerned. Write a simple query to find what are the options available for them? Can you filter the customers who accepted the offers here?

SELECT 
    customer_number AS 'customer n°'
FROM
    credit_card_data
WHERE
    credit_card_rating IN ('medium' , 'high')
        AND no_of_credit_cards_held <= 2
        AND own_your_home = 'yes'
        AND household_size >= 3
        AND offer_accepted = 'Yes';


# 12. Your managers want to find out the list of customers whose average balance is less than the average balance of all the customers in the database. Write a query to show them the list of such customers. You might need to use a subquery for this problem.

SELECT 
    customer_number  AS 'customer n°'
FROM
    credit_card_data
WHERE
    average_balance < (SELECT 
            AVG(average_balance)
        FROM
            credit_card_data)
ORDER BY average_balance DESC;


# 13. Since this is something that the senior management is regularly interested in, create a view of the same query.

drop view if exists less_average_balance;
CREATE VIEW less_average_balance AS
    SELECT 
        *
    FROM
        credit_card_data
    WHERE
        average_balance < (SELECT 
                AVG(average_balance)
            FROM
                credit_card_data)
    ORDER BY average_balance DESC;


# 14. What is the number of people who accepted the offer vs number of people who did not ?

SELECT DISTINCT
    (SELECT 
            COUNT(customer_number)
        FROM
            credit_card_data
        WHERE
            offer_accepted = 'yes') AS 'Accepted offers',
    (SELECT 
            COUNT(customer_number)
        FROM
            credit_card_data
        WHERE
            offer_accepted = 'no') AS 'Rejected offers'
FROM
    credit_card_data;


# 15. Your managers are more interested in customers with a credit rating of high or medium. 
# What is the difference in average balances of the customers with high credit card rating and low credit card rating?

SELECT 
    credit_card_rating,
    ROUND(AVG(average_balance), 2) AS 'Average balance'
FROM
    credit_card_data
WHERE
    credit_card_rating = 'High'
        OR credit_card_rating = 'Low'
GROUP BY credit_card_rating;
  
SELECT DISTINCT
    ROUND((SELECT 
                    AVG(average_balance)
                FROM
                    credit_card_data
                WHERE
                    credit_card_rating = 'High'
                GROUP BY credit_card_rating) - (SELECT 
                    AVG(average_balance)
                FROM
                    credit_card_data
                WHERE
                    credit_card_rating = 'Low'
                GROUP BY credit_card_rating),
            2)
FROM
    credit_card_data;


# 16. In the database, which all types of communication (`mailer_type`) were used and with how many customers?

SELECT 
    mailer_type AS 'Type of Mail' , COUNT(customer_number) AS 'Number of customer'
FROM
    credit_card_data
GROUP BY mailer_type;


# 17. Provide the details of the customer that is the 11th least `Q1_balance` in your database.

SELECT 
    q1_balance AS 'Q1 Balance'
FROM
    credit_card_data
WHERE
    q1_balance = (SELECT 
            q1_balance
        FROM
            (SELECT 
                q1_balance
            FROM
                credit_card_data
            ORDER BY q1_balance
            LIMIT 11) s1
        ORDER BY q1_balance DESC
        LIMIT 1)
GROUP BY q1_balance;

SELECT 
    q1_balance AS 'Q1 Balance' , customer_number as 'Customer Number'
FROM
    credit_card_data
ORDER BY q1_balance ASC
LIMIT 11;


# END