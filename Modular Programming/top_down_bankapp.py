__author__ = 'eric'

def get_data(filename):
    """
    get data from datafile and return initial balance and transactions list
    :param filename:
    :return: float, str[ ]
    """

    datafile = open(filename, 'r')

    initial_balance = float(datafile.readline())
    transactions_list = datafile.readlines()

    # clean up leading/trailing whitespace
    for t in range(len(transactions_list)):
        transactions_list[t] = transactions_list[t].strip()

    datafile.close()

    return initial_balance, transactions_list


def process_transactions(initial_balance, transactions_list):
    """
    process transactions list with current balance and compute withdrawal and deposit counts
    :param initial_balance: float - the starting balance of the account
    :param transactions_list: str[ ] - list of transaction strings
    :return: str[ ], float, int, int
    """

    deposit_count = 0
    withdrawal_count = 0
    current_balance = initial_balance

    for t in range(len(transactions_list)):

        tran_type = get_tran_type(transactions_list[t])
        amount = get_tran_amount(transactions_list[t])
        current_balance = new_balance(current_balance,tran_type, amount)
        transactions_list[t] = trans_string(transactions_list[t],current_balance)

        if tran_type == "d":
            deposit_count += 1
        else:
            withdrawal_count += 1

    return transactions_list, current_balance, withdrawal_count, deposit_count


def get_tran_type(transaction):
    """
    get the transaction type from a transaction string ('d' or 'w')
    :param transaction: str - a transaction string
    :return: str
    """
    return transaction[0]


def get_tran_amount(transaction):
    """
    get the transaction amount from a transaction string
    :param transaction: str - a transaction string
    :return: float
    """
    tran_items = transaction.split(",")
    amount_str = tran_items[1]
    return float(amount_str)


def new_balance(curr_balance,transaction_type, transaction_amount):
    """
    compute and return a new balance based on transaction type
    :param curr_balance: float - the current balance
    :param transaction_type: str -  transaction type i.e "d" for deposit, "w" for withdrawal
    :param transaction_amount: float - transaction amount
    :return: float - the updated balance
    """

    if transaction_type.lower() == 'd':
        curr_balance += transaction_amount
    else:
        curr_balance -= transaction_amount

    return curr_balance


def trans_string(transaction, curr_balance):
    """
    compute a new transaction string with the current balance appended to it.
    :param transaction: str - a transaction string
    :param curr_balance: float - the current balance
    :return: new transaction string
    """
    return transaction +"," + str(curr_balance)





def print_report(transactions_list, initial_balance, final_balance, deposit_count, withdrawal_count):

    report_str = ""

    # create the table header
    header = "{0:5}{1:>10}{2:>15}{3:>15}{4:>20}\n".format("Type","Amount","Date", "Vendor", "Current Balance")
    report_str += header + '\n'

    # create the table body
    for tran in transactions_list:
        tran_items = tran.split(",")
        tran_type = get_tran_type(tran)
        amount = get_tran_amount(tran)
        tran_date = tran_items[2]
        tran_vendor = tran_items[3]
        tran_balance = float(tran_items[4])
        report_str += "{0:5}{1:>10}{2:>15}{3:>15}{4:>20}\n".format(tran_type,amount,tran_date, tran_vendor, tran_balance)

    # append count reports
    report_str += '\n'
    report_str += "Starting balance: ${0:0.2f}\n".format(initial_balance)
    report_str += "Final balance: ${0:0.2f}\n".format(final_balance)
    report_str += "Deposit Count: {0}\n".format(deposit_count)
    report_str += "Withdrawal Count: {0}\n".format(withdrawal_count)

    report_file = open("bank_report.txt",'w')
    report_file.write(report_str)
    report_file.close()









def main():
    # Get Data
    starting_balance, transactions_list = get_data('data.txt')

    # Process Transactions
    new_transactions_list, final_balance, deposit_count, withdrawal_count = process_transactions(starting_balance,transactions_list)

    # Print Report
    print_report(new_transactions_list, starting_balance, final_balance, deposit_count, withdrawal_count)

main()
