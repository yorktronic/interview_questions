#######################################################################################################################
#
# Stock Trading Function -- see the README of the interview_questions repo for the problem description
# My initial solution: 14.1 microseconds
# My recursive solution: 14.3 microseconds
# Interview Cake's solution: 6.33 microseconds
#
#######################################################################################################################

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

#######################################################################################################################
#
# Fun with Integers
# My solution: 10.1 microseconds
# Interview Cake's solution: 4.06 microseconds
#
#######################################################################################################################

# My solution
def get_products_of_all_ints_except_at_index(nums):
    from operator import mul
    products = []
    for i, num in enumerate(nums):
        reduced_nums = nums[:i] + nums[i+1 :]
        products.append(reduce(mul, reduced_nums))
    return products

# Interview Cake's Solution, of complexity O(n) time and O(n) space
def get_products_of_all_ints_except_at_index_cake(int_list):
    # we make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    i = len(int_list) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products_of_all_ints_except_at_index

#######################################################################################################################
#
# Highest Product (I'm finally faster than Interview Cake!)
# My solution: 3.07 microseconds if there are no negative numbers, 3.5 microseconds otherwise
# Interview Cake's solution: 5.72 microseconds if there are no negative numbers, 7.37 microseconds otherwise
#
#######################################################################################################################

# My solution
def highest_product(nums):
    nums_asc = sorted(nums)
    nums_desc = sorted(nums, reverse=True)

    if nums_asc[0] * nums_asc[1] * nums_desc[0] > nums_desc[0] * nums_desc[1] * nums_desc[2]:
        return nums_asc[0] * nums_asc[1] * nums_desc[0]
    else:
        return nums_desc[0] * nums_desc[1] * nums_desc[2]

# Interview Cake's solution
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in list_of_ints[2:]:
        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_three