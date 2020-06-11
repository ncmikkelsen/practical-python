# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        total_cost = 0
        for row in rows:
            try:
                amount = int(row[1])
                cost = float(row[2])
                total_cost += amount * cost
            except ValueError:
                print('Error parsing', row)
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
