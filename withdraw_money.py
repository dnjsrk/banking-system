def deposit_money(list_):
    print('[출    금]')
    id = input('계좌 아이디: ')
    money = int(input('출금액: '))
    
    for idx, account_id in enumerate(list_.account_id):
        if id == account_id:
            if list_.balance[idx] >= money:
                list_.balance[idx] -= money
                print('출금완료')
            else:
                print('잔액부족')
        else:
            print('존재하지 않는 아이디입니다.')
            