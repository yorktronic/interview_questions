# Making change problem
def make_change(amount, denominations):
    # in: total number of cents, denominations of currency
    # out: all ways to make change
    ways = [1]+[0]*amount
    for denomination in denominations:
        for i in range(denomination, amount+1):
            ways[i] += ways[i - denomination]
    return len(ways) - 1



def num_ways(amount, coins):

    # return 1 if there's nothing left
    if amount == 0: return 1

    # return 0 if amount is negative
    if amount < 0: return 0

    # we're out of denominations
    if 
