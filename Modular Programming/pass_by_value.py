__author__ = 'eric'
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    balance = newBalance

def main ():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)

main()
