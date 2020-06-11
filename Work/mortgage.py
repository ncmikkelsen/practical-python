# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 5*12
extra_payment_end_month = extra_payment_start_month + 4 * 12
extra_payment = 1000.0


while principal > 0:
    month += 1
    if principal >= payment:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

        if month >= extra_payment_start_month and month < extra_payment_end_month:
            principal -= extra_payment
            total_paid += extra_payment
    else:
        total_paid = total_paid + principal
        principal = 0
    monthly_result = f'{month} \t {total_paid:0.2f} \t {principal:0.2f}'
    print(monthly_result)

print('Total paid', round(total_paid, 1), 'over', month, 'months which is', month // 12, 'years and', month % 12, 'months')
