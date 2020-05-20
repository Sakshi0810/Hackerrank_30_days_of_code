import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=float(meal_cost*(tip_percent/100))
    tax=float(meal_cost*(tax_percent/100))
    total=meal_cost+tip+tax
    print(round(total))
if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
