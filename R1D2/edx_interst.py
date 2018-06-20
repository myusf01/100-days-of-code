"""
author= Muhammed Yusuf

bln: stands for balance
aIR: for Annual Interest Rate
mPr: for Monthly Payment Rate

"""
### Version 0.1
def interest(bln, aIr, mPr):

    def clc(bln, aIr, mPr):

        for i in range(12):
            monthlyInterstRate = aIr / 12.0
            minMonthlyPayment = mPr * bln
            monthlyUnpaidBalance = bln - minMonthlyPayment
            bln = monthlyUnpaidBalance  + (monthlyInterstRate  * monthlyUnpaidBalance)
        return bln

    return "Remaining Balance: " + str(round(clc(bln, aIr, mPr), 2))

### Version 0.2

def interest(balance, annualInterestRate, monthlyPaymentRate):

    def clc(balance, annualInterestRate, monthlyPaymentRate):

        for i in range(12):
            monthlyInterstRate = annualInterestRate / 12.0
            minMonthlyPayment = monthlyPaymentRate * balance
            monthlyUnpaidBalance = balance - minMonthlyPayment
            balance = monthlyUnpaidBalance  + (monthlyInterstRate  * monthlyUnpaidBalance)
        return balance

    print("Remaining Balance: " + str(round(clc(balance, annualInterestRate, monthlyPaymentRate), 2)))


### Version 0.3

        # for i in range(12):
        #     monthlyInterstRate = annualInterestRate / 12.0
        #     minMonthlyPayment = monthlyPaymentRate * balance
        #     monthlyUnpaidBalance = balance - minMonthlyPayment
        #     balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
        #
        # print("Remaining Balance: " + str(round(balance, 2)))
