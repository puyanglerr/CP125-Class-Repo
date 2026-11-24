# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participant, tent_capacity, tent_price):
    tent_capacity = math.ceil (participant/tent_capacity)
    cost = tent_capacity * tent_price
    return cost
