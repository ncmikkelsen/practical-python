# pcost.py
#
# Exercise 1.27

f = open('Data/portfolio.csv', 'rt')
next(f)
total_cost = 0

for line in f:
    row = line.split(',')
    amount = int(row[1])
    cost = float(row[2])
    stock_cost = amount * cost

    print(f'{row[0]} \t costs \t ${stock_cost:0.2f}')

    total_cost += stock_cost

print(f'Total \t cost is ${total_cost:0.2f}')

f.close()
