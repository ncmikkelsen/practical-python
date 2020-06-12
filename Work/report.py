# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
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

def read_prices(filename):
    prices = { }

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                try:
                    name = row[0]
                    price = float(row[1])
                    prices[name] = price
                except ValueError:
                    print('Error parsing', row)



    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

gain = 0
total_cost = 0
total_value = 0
for h in portfolio:
    name = h['name']
    if name in prices:
        o_price = h['price']
        shares = h['shares']
        c_price = prices[name]
        this_gain = shares * (c_price - o_price)
        gain += this_gain
        #print(f"The gain/loss of {name} \t is ${this_gain:0.02f}")

        print("The result of", name, end=' ')
        if this_gain > 0.0:
            print(f"is a gain of ${this_gain}")
        else:
            print(f"is a loss of ${this_gain}")
        total_cost = shares * o_price
        total_value = shares * c_price


    else:
        print(f"the name {name} is not in the pricelist")

print()
print(f'The total cost was ${total_cost:0.02f}')
print(f'The total value is ${total_value:0.02f}')
print('The result is a', end=' ')
if gain > 0:
    print('gain', end = ' ')
else:
    print('loss', end = ' ')
print(f'of ${gain:0.02f}')
