###
# Credit card payment 
#
account_balance = 500
total_payment = int(input())

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')