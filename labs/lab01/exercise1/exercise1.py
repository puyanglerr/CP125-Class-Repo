# Lab 01 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, budget):
    fuel_price = ((one_way_km * 2)/10) * 2
    if fuel_price > budget:
        return False
    else:
        return True
