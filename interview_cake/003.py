# Highest product of three ints in a list
from itertools import islice
NUMBERS = [-10, -10, 1, 3, 2]
NUMBERS2 = [1, 10, -5, 1, -100]

# First attempt
def get_highest_product(nums):
    nums = sorted(nums, reverse=True)
    nums = [nums[0], nums[1], nums[2], nums[-1], nums[-2]]
    return max(nums[0] * nums[1] * nums[2], nums[-1] * nums[-2] * nums[0])


# IC's solution
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # we could also start these as None and check below if they're set
    # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest =  min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]

    # except this one--we pre-populate it for the first /3/ items.
    # this means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # walk through items, starting at index 2
    for current in islice(list_of_ints, 2, None):

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


# Second attempt, handling product of k rather than 3
# WORK IN PROGRESS
def get_highest_product_k(nums, k):
    nums = sorted(nums, reverse=True)

    biggest_pos = []
    biggest_neg = []
    idx = 0

    while (len(biggest_pos) <= k or len(biggest_neg) <= k) and idx < len(nums):
        if nums[idx] > 0:
            print('added a pos')
            biggest_pos.append(nums[idx])
        elif nums[idx] < 0:
            print('added a neg')
            biggest_neg.append(nums[idx])
        print(idx)
        idx += 1

    # Choose the largest k numbers from both lists, tracking if we use even or odd negs
    idx = 0
    biggest_neg = sorted(biggest_neg)
    odd = False

    biggest = []
    failsafe = []

    while idx <= k:
        if abs(biggest_neg[idx]) > biggest_pos[idx]:
            biggest.append(biggest_neg[idx])
            failsafe.append(biggest_pos[idx])
        else:
            biggest.append(biggest_pos[idx])

        idx += 1

    return biggest_pos, biggest_neg
