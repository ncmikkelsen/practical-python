# pcost.py
#
# Exercise 1.27
import csv

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

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
