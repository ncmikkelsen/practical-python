# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        next(f)
        total_cost = 0

        for line in f:
            row = line.split(',')
            try:
                amount = int(row[1])
                cost = float(row[2])
                total_cost += amount * cost
            except ValueError:
                print('Error parsing', line)
        return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
