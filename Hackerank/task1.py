#!/usr/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_amount = int(input().strip())
    tax_percentage = int(input().strip())
    tip_amount = meal_cost * tip_amount / 100
    tax_percentage = meal_cost * tax_percentage / 100
    total_cost = round(meal_cost + tip_amount + tax_percentage)
    print(f"The Total meal cost is {str(total_cost)} dollars")