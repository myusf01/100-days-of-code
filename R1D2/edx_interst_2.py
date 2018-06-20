###Very first version!!!


balance = 4773
annualInterestRate = 0.2
minFixedMonthlyPayment = 0.1

# while True:
#     for i in range(12):
#         monthlyInterstRate = annualInterestRate / 12.0
#         monthlyUnpaidBalance = balance - minFixedMonthlyPayment
#         balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
#     if balance >= 0:
#         minFixedMonthlyPayment += 10
#         continue
#     elif balance <= 0:
#         print("Lowest Payment: " + str(minFixedMonthlyPayment))
#         break

#### Working Latest Version
def hesap(balance, annualInterestRate):
    for i in range(12):
        monthlyInterstRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - minFixedMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
    return balance

while True:
    if hesap(balance, annualInterestRate) > 0:
        minFixedMonthlyPayment += 10
        continue
    else:
        print(minFixedMonthlyPayment)
        break