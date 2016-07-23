# Interview Questions #
This repo contains some random interview questions that I've been asked. All questions have been made anonymous for obvious reasons.

## answer.sql - job interview SQL query question ##
1. You are an ecommerce company that sells products
2. There is a SQL table containing the following columns:
  * user_id (INT)
  * order_id (INT)
  * order_date (TEXT in the format YYYY-MM-DD and ignoring hours, minutes, and seconds for the sake of this problem)
3. The CEO just asked: "What is the average time between orders across all customers"?

What's your query, yo? You are only permitted to use SQL Queries to solve this problem.

## promotion.sql - Another job interview SQL query question ##
1. You are an ecommerce company that sells products
2. There's a SQL table containing the following columns
  * order_id (INT)
  * amount (FLOAT)
  * date (date)
3. The marketing department just asked: We'd like to keep track of the largest (most $$$) order placed every day. Also, there's another table for each month that contains all the orders for a given month. We would like to see an ordered list of the top performing days for the month of june, ordered by revenue.

## Measuring Success a of New Product ##
When a new product feature is released a variety of new events are tracked to support the 
measurement and analysis of that new feature. This role will define the data collection and 
testing based on the product spec and work with the engineering team to implement the event tracking. What steps might you take to ensure proper collection and data quality?

I decided that I could better explain how I would tackle this problem if I came up with my best guess at a real-world [company x] scenario, but I tried to keep things general enough so that they could get a handle on my problem solving / critical thinking skills.

###  The New Feature ###
[Company X] develops and rolls out a new feature that enables a peer-to-peer points system where members of a project team can distribute points to one another to recognize exceptional work, teamwork, etc.

### Step 1: What to Collect? ###
First, I would work with the engineering team as well as any other applicable teams at [company x] (sales, marketing, customer service, etc.), along with possibly getting input from [company x] customers to determine what events would be likely be related to the success or failure of the peer-to-peer points feature. Any measurements on the performance of existing features would need to be incorporated for comparing one feature to another. Here are some examples of things that would possibly need to be captured:

* Maybe teams have a way of selecting which recognition / reward program they would like to use. If that’s the case, we would want to monitor the utilization of the new feature over whatever competing existing reward systems are already in place
If the new feature was the first reward system, we would simply want to monitor its utilization
* Some other data might include time-related data, such as when notifications of the new feature are sent out vs. when it’s used by the same people
* If we’re comparing this new feature to some existing feature, we would include any elements that are relevant to the existing feature for comparing performance
* In the end, we want to have enough data to be able to A/B test ourr new feature against existing features and future features, so there needs to be consistency in the data that is collected so that the performance of each feature can be described in as close to the same context as possible

###  Step 2: Data Collection ###
The key aspect of collecting valuable, clean, usable data from an analytics / data science perspective is to ensure that the data we collect can be related to existing data as much as possible. For example, we would want our session data from users accessing the new feature to be linked to data about our users, be it what company they work for, what industry they are in, what role they on a team, where they are in the country / world, etc. If the new feature is competing with existing features, we would want to be able to illustrate what users used what features in the past vs. now. Things of that nature.

The idea here is, while we have worked with all applicable parties in Step 1 to define what the logical data elements to track are, we always want to be thinking ahead enough to ensure that what is collected can also be linked to as much other data as possible. When I go down the road of trying to define the usefulness of something, I often don’t know what exactly will be the most valuable piece of information to demonstrate success. It’s always better to have too much data than not enough.

###  Step 3: Ensuring Quality Data ###
Ultimately, the definition of the usefulness / success of the new feature is going to hinge on quality, clean data. This data will feed a model that will ultimately quantify in some way the performance of the new feature. I would work with the engineering team to ensure data quality metrics would also be captured while all the data identified in steps 1 and 2 is also being captured. This could be ensuring that all events are being properly logged in the database, and that the data is complete and as clean as possible. Typically, I would be looking for the following quality metrics:

* Completeness
* Accuracy
* Relevance to performance of the new feature in my model
* Reliability of our ability to capture certain data elements
* Ease of access

In all likelihood, I would have queries and either python scripts or utilization of some internal analytics tool like Looker to constantly monitor the quality of the data coming in. Any instances of missing, incomplete, or invalid data would be addressed with engineering to ensure that the integrity and usability of the data is maintained. If new elements are identified as useful I would again work with engineering to ensure that we were capturing those as well.

Data quality is also about monitoring the usability of the data. This is where my statistics and data science background would be leveraged, performing standard stats analyses on captured data to get a handle on the distribution of that data for use in my model. There would be many plots, modeling, and calculations here to ensure that I can be confident in the accuracy of my model. 

This entire process is iterative. As I learn more about what can be captured, what is and isn’t useful, etc., I might go back to steps 1 and 2 to continue to improve my assessment on the performance of the new feature. 