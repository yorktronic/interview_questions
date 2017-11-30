# Interview Questions #
This repo contains some random interview questions that I've been asked. All questions have been made anonymous for obvious reasons.

# Analyzing Wikipedia text and BTC price predictor #

## Wikipedia text analysis ##
Write a Python program that takes the content of (http://en.wikipedia.org/wiki/Machine_learning) and counts the frequency of each word and outputs the 10 most frequent words ordered by decreasing frequency.

BONUS POINTS:
- exclude common words using (http://en.wikipedia.org/wiki/Most_common_words_in_English)

my solution is in <a href="kickback.py">kickback.py</a>. There's a bug I need to fix, the algorithm is still logging spaces as words.

Output:
```python
[(u'learning', 96),
 (u'', 86),
 (u'machine', 26),
 (u'data', 26),
 (u'algorithms', 20),
 (u'Machine', 16),
 (u'model', 14),
 (u'training', 13),
 (u'set', 12),
 (u'In', 12)]
```

## BTC Price Predictor ##
Write a python program that takes the historical values of USDBTC exchange rate from (http://www.quandl.com/api/v1/datasets/BCHAIN/MKPRU.json) and generates a prediction for the price of Bitcoins in USD on July 4th 2016.

BONUS POINTS:
- use only data up to March 31st 2016 to train your model
- introduce 1 external data source (besides the price itself) to improve your model

my solution is in <a href="kickback2.py">kickback2.py</a>

Output: 
```python
the prediction for July 4, 2016 is 420.498926059
```

# <a href="https://www.interviewcake.com/" target="_blank">InterviewCake.com</a> Sample Interview Questions #
Interview Cake is a website that has a bunch of sample coding interview questions, which I solve periodically.
 
## Stock Trading Function ##
Suppose we could access yesterday's stock prices as a list, where:

* The indices are the time in minutes past trade opening time, which was 9:30am local time.
* The values are the price in dollars of Apple stock at that time.  

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the **best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.**

For example:

```python
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
```
My solution can be found with other my Interview Cake solutions in <a href="interview-cake-questions.py">interview-cake-questions.py</a>

## Fun with Integers ##
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.  

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
  
`[1, 7, 3, 4]`  

Your function would return:  

`[84, 12, 28, 21]`

by calculating:

`[7*3*4, 1*3*4, 1*7*4, 1*7*3]`  

**Do not use division in your solution.**

## Highest Product ##
Given a list_of_ints, find the highest_product you can get from three of the integers.  

The input list_of_ints will always have at least three integers.

## Find a duplicate, Space Edition™ ##
We have a list of integers, where:  

1. The integers are in the range 1..n1..n
2. The list has a length of n+1n+1  

It follows that our list has *at least* one integer which appears *at least* twice. But it may have *several* duplicates, and each duplicate may appear *more than* twice.

**Write a function which finds *any* integer that appears more than once in our list.**

We're going to run this function on our new, super-hip Macbook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. **So we need to optimize for space!**

# Measuring Success a of New Product #

**Question:** When a new product feature is released a variety of new events are tracked to support the measurement and analysis of that new feature. This role will define the data collection and 
testing based on the product spec and work with the engineering team to implement the event tracking. What steps might you take to ensure proper collection and data quality?

*I decided that I could better explain how I would tackle this problem if I came up with my best guess at a real-world [company x] scenario, but I tried to keep things general enough so that they could get a handle on my problem solving / critical thinking skills.*

##  The New Feature ##
[Company X] develops and rolls out a new feature that enables a peer-to-peer points system where members of a project team can distribute points to one another to recognize exceptional work, teamwork, etc.

## Step 1: What to Collect? ##
First, I would work with the engineering team as well as any other applicable teams at [company x] (sales, marketing, customer service, etc.), along with possibly getting input from [company x] customers to determine what events would be likely be related to the success or failure of the peer-to-peer points feature. Any measurements on the performance of existing features would need to be incorporated for comparing one feature to another. Here are some examples of things that would possibly need to be captured:

* Maybe teams have a way of selecting which recognition / reward program they would like to use. If that’s the case, we would want to monitor the utilization of the new feature over whatever competing existing reward systems are already in place
If the new feature was the first reward system, we would simply want to monitor its utilization
* Some other data might include time-related data, such as when notifications of the new feature are sent out vs. when it’s used by the same people
* If we’re comparing this new feature to some existing feature, we would include any elements that are relevant to the existing feature for comparing performance
* In the end, we want to have enough data to be able to A/B test ourr new feature against existing features and future features, so there needs to be consistency in the data that is collected so that the performance of each feature can be described in as close to the same context as possible

##  Step 2: Data Collection ##
The key aspect of collecting valuable, clean, usable data from an analytics / data science perspective is to ensure that the data we collect can be related to existing data as much as possible. For example, we would want our session data from users accessing the new feature to be linked to data about our users, be it what company they work for, what industry they are in, what role they on a team, where they are in the country / world, etc. If the new feature is competing with existing features, we would want to be able to illustrate what users used what features in the past vs. now. Things of that nature.

The idea here is, while we have worked with all applicable parties in Step 1 to define what the logical data elements to track are, we always want to be thinking ahead enough to ensure that what is collected can also be linked to as much other data as possible. When I go down the road of trying to define the usefulness of something, I often don’t know what exactly will be the most valuable piece of information to demonstrate success. It’s always better to have too much data than not enough.

##  Step 3: Ensuring Quality Data ##
Ultimately, the definition of the usefulness / success of the new feature is going to hinge on quality, clean data. This data will feed a model that will ultimately quantify in some way the performance of the new feature. I would work with the engineering team to ensure data quality metrics would also be captured while all the data identified in steps 1 and 2 is also being captured. This could be ensuring that all events are being properly logged in the database, and that the data is complete and as clean as possible. Typically, I would be looking for the following quality metrics:

* Completeness
* Accuracy
* Relevance to performance of the new feature in my model
* Reliability of our ability to capture certain data elements
* Ease of access

In all likelihood, I would have queries and either python scripts or utilization of some internal analytics tool like Looker to constantly monitor the quality of the data coming in. Any instances of missing, incomplete, or invalid data would be addressed with engineering to ensure that the integrity and usability of the data is maintained. If new elements are identified as useful I would again work with engineering to ensure that we were capturing those as well.

Data quality is also about monitoring the usability of the data. This is where my statistics and data science background would be leveraged, performing standard stats analyses on captured data to get a handle on the distribution of that data for use in my model. There would be many plots, modeling, and calculations here to ensure that I can be confident in the accuracy of my model. 

This entire process is iterative. As I learn more about what can be captured, what is and isn’t useful, etc., I might go back to steps 1 and 2 to continue to improve my assessment on the performance of the new feature.
 
# answer.sql - job interview SQL query question #
1. You are an ecommerce company that sells products
2. There is a SQL table containing the following columns:
  * user_id (INT)
  * order_id (INT)
  * order_date (TEXT in the format YYYY-MM-DD and ignoring hours, minutes, and seconds for the sake of this problem)
3. The CEO just asked: "What is the average time between orders across all customers"?

What's your query, yo? You are only permitted to use SQL Queries to solve this problem.

# promotion.sql - Another job interview SQL query question #
1. You are an ecommerce company that sells products
2. There's a SQL table containing the following columns
  * order_id (INT)
  * amount (FLOAT)
  * date (date)
3. The marketing department just asked: We'd like to keep track of the largest (most $$$) order placed every day. Also, there's another table for each month that contains all the orders for a given month. We would like to see an ordered list of the top performing days for the month of june, ordered by revenue.