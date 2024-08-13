from info import *

def show_all_account_information(acc):
    for i in range(len(acc.account_id)):
        print(f'''
            계좌 id : {acc.account[i]}
            계좌 주인 : {acc.customer_name[i]}
            계좌 잔액 : {acc.balance[i]}
        ''')
