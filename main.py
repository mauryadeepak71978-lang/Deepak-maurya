def balance_check():
    with open("balance.txt","r+") as f:
        balance = f.read()
        print("Your balance is", balance)

balance_check()