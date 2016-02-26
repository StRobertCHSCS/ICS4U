def addInterest(balanceList, rate):
    for i in range(len(balanceList)):
        balanceList[i] = balanceList[i] * (1+rate)
        

def main ():
    amounts = [1000, 1200, 900, 1100]
    print("The initial amounts are:",amounts)
    rate = 0.05
    addInterest(amounts, rate)
    print("The updated amounts are:",amounts)

main()
