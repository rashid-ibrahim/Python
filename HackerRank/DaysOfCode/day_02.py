"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-operators/problem
"""


mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

print("The total meal cost is", round(mealCost + (mealCost * (tipPercent/100) + (mealCost *(taxPercent/100)))), "dollars.")