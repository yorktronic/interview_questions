# NOTE: I didn't have time to import any external data sources. Here are some ideas of external sources that I'd use:
# For each date I would be interested in doing NLP on twitter posts from a handful of sources, such as CoinDesk
# Check other currency conversion rates, price of gold, etc.
# Anyway I used linear regression with time indexes as the feature, which is obviously going to give horrible predictions
# Also, I use graphlab create instead of scikit-learn, as that's what I've been working with recently

import json, urllib
import graphlab

# Get the data
url = "http://www.quandl.com/api/v1/datasets/BCHAIN/MKPRU.json"
data = urllib.urlopen(url)
btc_hist = json.loads(data.read())

dates = []
prices = []
index = list(range(0,len(btc_hist['data'])))
index.reverse()

# Convert the price data into an SFrame
for date_price_pair in btc_hist['data']:
    dates.append(date_price_pair[0])
    prices.append(date_price_pair[1])

btc = graphlab.SFrame({'index': index, 'date': dates, 'price': prices})

# Split the SFrame into train and test sets
train = btc[btc['date'] < '2016-03-31']
test = btc[btc['date'] >= '2016-03-31']

model = graphlab.linear_regression.create(train, features=['index', 'date'], target='price', max_iterations=1000000000)

predictions = model.predict(test)

test['prediction'] = predictions

print "the prediction for July 4, 2016 is {}".format(test[test['date'] == '2016-07-04']['prediction'][0])