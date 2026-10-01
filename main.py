def debit_balance():
    while True:
        with open("balance.txt","r+") as f:
            current_balance = f.read().strip()
            current_balance = int(current_balance)
            print("Your balance is",current_balance)
            try:
                debit = int(input("Enter the amount you want to debit from your account: "))
            except:
                continue
            if debit > current_balance or debit <= 0:
                print("ERROR\nEnter a valid amount")
                continue
            else:
                new_balance = current_balance - debit
                f.seek(0)
                f.truncate()
                f.write(str(new_balance))
                print("Your balance is",new_balance)
                break