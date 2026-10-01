#ATM clone


def create_account():
    name = input("Enter your name: ")
    dob = input("Enter your year of birth: ")
    contact = int(input("Enter your phone number: "))
    email = input("Enter your email address: ")
    while True:
        try:
            ac_type = int(input("(1) saving account\n(2) current account\nChoose your account type: "))
            if ac_type == 1:
                ac_type = "saving account"
                break
            elif ac_type == 2:
                ac_type = "current account"
                break
            else:
                print("Invalid option ")                
        except:

            pass
    while True:
        try:
            pin = input("Create a 5 digit pin: ")
            if len(pin) == 5:
                print("New pin is created")
                f = open("pin.txt","x")
                f.write(pin)
                f.close
            else:
                print("Invalid pin")
        except:
            pass
    print("New account has been created\nYour username is",name+dob)
    try:
        file = open("balance.txt","x")
        file.write("0")
        file.close
    except:
        pass

def credit_account():
    while True:
        try:
            credit = int(input("Enter the amount you want to credit: "))
            if credit <= 0:
                print("Enter a valid amount")
            else:
                with open("balance.txt","r+") as f:
                    current_balance = f.read().strip()
                    current_balance = int(current_balance)
                    credited_balance = current_balance + credit
                    credited_balance = str(credited_balance)
                    f.seek(0)
                    f.truncate
                    f.write(credited_balance)
                    f.seek(0)
                    new_balance = f.read().strip()
                    print("Your current balance is", new_balance)
                    break
        except:
            pass

def balance_check():
    with open("balance.txt","r+") as f:
        balance = f.read()
        print("Your balance is", balance)

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

