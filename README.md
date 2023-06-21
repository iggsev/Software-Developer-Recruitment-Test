1. Develop a function in Python 3 that receives a date and returns all the days from that date until the end of the following month, excluding weekends.
For example:
Input: '2022-01-26'
Output: ['2022-01-26', '2022-01-27', '2022-01-28', '2022-01-31', '2022-02-01', '2022-02-02', '2022-02-03', '2022-02-04', '2022-02-07', '2022-02-08', '2022-02-09', '2022-02-10', '2022-02-11', '2022-02-14', '2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18', '2022-02-21', '2022-02-22', '2022-02-23', '2022-02-24', '2022-02-25', '2022-02-28']

2. Representatives of a stationery products company visit numerous establishments on a weekly basis to offer their products. These representatives have a name, a salary, and are responsible for a list of establishments. The company also has coordinators who are responsible for a region and the representatives in that region. The coordinators also have a name and a salary.
The establishments have a name, an address, and a category to which they belong (such as a supermarket or a stationery store, for example).
Using object-oriented programming, develop the classes for these objects, making sure to utilize the concepts of this paradigm appropriately. Also, create the visit relationship between representatives and establishments, feel free to define the necessary attributes for this relationship.
Consider that this system can scale to include more entities and relationships.

3. A candy company has a system that generates discounts on products based on the quantity of boxes sold. The salesperson is responsible for presenting these discounts to the customer and convincing them to buy more products to obtain a greater discount.
Your task is to create the file that associates the discount for each product with each customer, respecting certain rules.
To do this, use the Python 3 programming language and the pandas or polars libraries.
This task comes with three files: products.csv, customers.csv, and discounts.csv. There is also a fourth validation file: customer_discount.csv.
The products.csv file is a product database containing the following information:
id: unique identifier of the product
name: name of the product
sugar: sugar index in the product
category: categorization of the product (Cookie, Chewing Gum, or Chocolate Bar)

The discounts.csv file is a discount file that specifies the discounts for products based on different quantities of boxes purchased:
product: unique identifier of the product with the discount
boxes: quantity of boxes that must be purchased to receive the discount
discount: percentage discount on the final price
In the first row, the product with id 1 has a 7% discount for purchases of 5 boxes.

The customers.csv file is a customer database containing the following information:
id: unique identifier of the customer
name: name of the customer
city: city of the customer
channel: customer categorization (Bar, Pharmacy, Market, University)

There is also the customer_discount.csv file that associates a customer from customers.csv with a discount from discounts.csv.
This is the file you need to generate, which the salesperson will use when meeting with the customer. Below is a snippet of this file. Therefore, customer with id 1 will be presented with a 7% discount on the purchase of 5 boxes of the product with id 1, an 8% discount on the purchase of 10 boxes of the same product, and so on.

Exercise 1:
Statement: Create the customer_discount database, with the distribution of all discounts for each customer (each row should have a customer and the discount for a product). You should create an n x n association between the databases in customers.csv and discounts.csv.
This database should be identical to the one in the customer_discount.csv file.
Exercise 2:
Business rule: The city of Belém has banned the sale of products with a high sugar index in schools and universities.
Statement: Develop a function that receives the customer_discount database as a parameter and returns a similar data frame, but without the discounts for products with a high sugar index for schools and universities in Belém.
Note: Create a function that works independently of the content of the databases. For example, if the customer database is changed and new customers such as universities and schools are added, your function should still return a valid result. The same requirement for generalizing the solution will be considered in the questions of this section.

Example tables:

Table: products.csv

| id |     name      | sugar |   category   |
|----|---------------|-------|--------------|
|  1 | Product1      |   10  |   Cookie     |
|  2 | Product2      |   5   | Chewing Gum  |
|  3 | Product3      |   15  | Chocolate Bar|


Table: discounts.csv

| product | boxes | discount |
|---------|-------|----------|
|    1    |   5   |    7     |
|    1    |  10   |    8     |
|    2    |   3   |    5     |


Table: customers.csv

| id |      name     |      city     |  channel   |
|----|---------------|---------------|------------|
|  1 | Customer1     |   New York    |    Bar     |
|  2 | Customer2     |   Los Angeles |    Market  |
|  3 | Customer3     |   Chicago     |  Pharmacy  |


Table: customer_discount.csv

| customer | product | boxes | discount |
|----------|---------|-------|----------|
|    1     |    1    |   5   |    7     |
|    1     |    1    |  10   |    8     |
|    2     |    2    |   3   |    5     |
