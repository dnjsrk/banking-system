def make_account(list_):
    print('[계좌 개설]')
    
    account_id = input('계좌ID: ')
    customer_name = input('이  름: ')
    balance = int(input('입금액: '))
    
    list_.account_id.append(account_id)
    list_.customer_name.append(customer_name)
    list_.balance.append(balance)