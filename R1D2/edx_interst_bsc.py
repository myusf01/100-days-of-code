balance = 320000
annualInterestRate = 0.2
eps = 0.10
remain = balance

monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentBound_Lower = balance / 12
monthlyPaymentBound_Upper = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
minGuess = (monthlyPaymentBound_Upper + monthlyPaymentBound_Lower) / 2

while remain >= eps:
    minGuess = (monthlyPaymentBound_Upper + monthlyPaymentBound_Lower) / 2

    for i in range(12):
        newBalance = remain - minGuess
        monthlyInterest = annualInterestRate / 12 * newBalance
        remain = newBalance + monthlyInterest
    if remain < 0:
        monthlyPaymentBound_Upper = minGuess
        remain = balance
    elif remain > eps:
        monthlyPaymentBound_Lower = minGuess
        remain = balance
print(round(minGuess,2))

for i in range(12):
    news = remain - minGuess
    monthlyInteresta =