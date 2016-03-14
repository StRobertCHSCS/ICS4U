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
    for t in range (len(transactions_list)):
        transactions_list[t] = transactions_list[t].strip()

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
    return transaction[0]


def get_tran_amount(transaction):
    tran_items = transaction.split(",")
    amount_str = tran_items[1]
    return float(amount_str)


def new_balance(curr_balance,transaction_type, transaction_amount):

    if transaction_type.lower() == 'd':
        curr_balance += transaction_amount
    else:
        curr_balance -= transaction_amount

    return curr_balance


def trans_string(transaction, curr_balance):
    return transaction +"," + str(curr_balance)





def print_report(transactions_list, initial_balance, final_balance, deposit_count, withdrawal_count):

    report_str = ""
    header = "{0:5}{1:>10}{2:>10}{3:>10}{4:>15}\n".format("Type","Amount","Date", "Vendor", "Current Balance")
    report_str += header

    for tran in transactions_list:
        tran_items = trans.split(",")
        tran_type = get_tran_amount(tran)
        amount = get_tran_amount(tran)





def main():
    # Get Data
    starting_balance, transactions_list = get_data('data.txt')

    # Process Transactions
    new_transactions_list, final_balance, deposit_count, withdrawal_count = process_transactions(starting_balance,transactions_list)

    # Print Report
    print_report(new_transactions_list, starting_balance, final_balance, deposit_count, withdrawal_count)

