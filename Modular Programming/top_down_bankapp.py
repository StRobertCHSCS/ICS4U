__author__ = 'eric'

def get_data(filename):
    pass


def process_transactions(initial_balance, transactions_list):
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
    pass


def get_tran_amount(transaction):
    pass


def new_balance(curr_balance,transaction_type, transaction_amount):
    pass


def trans_string(transaction_list, curr_balance):
    pass



