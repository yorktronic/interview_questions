# Product of other numbers

from operator import mul
import numpy as np

NUMBERS = [1, 7, 3, 4]

# Original solution, second fastest
def other_products(nums):
    products = []
    max_index = len(nums) - 1

    for idx, num in enumerate(nums):

        if idx == 0:
            products.append(reduce(mul, nums[1:]))
        elif idx == max_index:
            products.append(reduce(mul, nums[:max_index]))
        else:
            products.append(reduce(mul, nums[:idx] + nums[(idx+1):]))

    return products

# Breaking the problem down in to subproblems, slowest

def get_products(nums):
    before = prod_before(nums)
    after = prod_after(nums)
    return np.multiply(before, after)

def prod_before(nums):
   before = []
   for idx, num in enumerate(nums):
       if idx == 0:
           before.append(1)
       else:
           before.append(reduce(mul, nums[:idx]))

   return before


def prod_after(nums):
    after = []
    max_index = len(nums) - 1
    for idx, num in enumerate(nums):
        if idx == max_index:
            after.append(1)
        else:
            after.append(reduce(mul, nums[(idx+1):]))

    return after

# Interview Cake's optimal solution, fastest

def get_products_of_all_ints_except_at_index(int_list):
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
