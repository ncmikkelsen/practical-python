# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])

                portfolio.append({'name': name, 'shares': shares, 'price': price})

            except ValueError:
                print('Error parsing', row)

    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_list = read_portfolio(filename)
print(portfolio_list)
