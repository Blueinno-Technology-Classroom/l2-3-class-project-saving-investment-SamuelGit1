##################################################
'''
Challenge
'''

def round_off(num):
    return float("{:.2f}".format(num))

def investment(initial_investment, deposit_every_year):
    current_balance = round_off(initial_investment)
    deposit = round_off(deposit_every_year)
    interest_per_year = 0.065
    for i in range(1, 26):
        if i <= 9:
            year = '0' + str(i)
        else :
            year = str(i)
        interest = round_off(current_balance * interest_per_year)
        new_balance = round_off(current_balance + interest)
        print(f'{year}: current balance: {current_balance}, interest: {interest},  deposit: {deposit}, new balance: {new_balance}')
        current_balance = new_balance

investment(1000, 100)