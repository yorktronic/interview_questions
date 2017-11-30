# Apple stock trading
import datetime as dt

STOCK_PRICES_YESTERDAY = [10, 7, 5, 8, 11, 9]

# Optimal, provided by IC
def get_max_profit_optimal(stock_prices_yesterday):
    best_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    lowest_price = stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        if index == 0:
            continue

        profit = current_price - lowest_price
        best_profit = max(best_profit, profit)
        lowest_price = min(lowest_price, current_price)

    return best_profit

# My revised original
def get_max_profit(stock_prices_yesterday):
    best_profit = 0
    lowest_price = stock_prices_yesterday[0]

    # Don't need to do any comparisons @ idx = 0
    stock_prices_yesterday = stock_prices_yesterday[1:]

    for price in stock_prices_yesterday:

        profit = price - lowest_price
        lowest_price = min(price, lowest_price)
        best_profit = max(profit, best_profit)

    return best_profit

before = dt.datetime.now()
print('Running my version')
print(get_max_profit(STOCK_PRICES_YESTERDAY))
print('Completed in {}'.format(dt.datetime.now() - before))

#before = dt.datetime.now()
#print('Running IC version')
#print(get_max_profit_optimal(STOCK_PRICES_YESTERDAY))
#print('Completed in {}'.format(dt.datetime.now() - before))
