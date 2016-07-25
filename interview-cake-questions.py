# Stock Trading Function -- see the README of the interview_questions repo for the problem description
# This was my first solution, which is not optimal as it's an O(2n) solution instead of their optimal O(n) solution
stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 1, 0, 99, 1, 200, 3]
stock_prices_decreasing = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def get_max_profit(stock_prices_yesterday):
    max_diff = 0
    idy = 0
    for price in stock_prices_yesterday:
        idy += 1
        idx = idy + 1
        while idx < len(stock_prices_yesterday):
            diff = price - stock_prices_yesterday[idx]
            if diff < max_diff:
                max_diff = diff
            idx += 1
    return abs(max_diff)

# Same problem as above, but with a recursive solution
MAX_DIFF = 0
def get_max_profit_recursive(stock_prices_yesterday):
    global MAX_DIFF
    for price in stock_prices_yesterday:
        if price - stock_prices_yesterday[0] < MAX_DIFF:
            MAX_DIFF = price - stock_prices_yesterday[0]
    MAX_DIFF = get_max_profit(stock_prices_yesterday[1:])
    return MAX_DIFF

# Interview Cake's optimal solution
def get_max_profit_cake(stock_prices_yesterday):
    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit