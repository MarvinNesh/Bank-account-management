from bank import BankAccount
import csv
def create_account_number():
    import uuid

    account_number=uuid.uuid4()
    return str(account_number)

def csv_writing():
    import csv
    import random
    with open("names.txt","r",errors="ignore") as f:
        account_holders=f.read().splitlines()
    account_with_name_number={}
    balances = [round(random.uniform(0, 10000), 2) for _ in range(100)]
    for name in account_holders:
        account_with_name_number[name]=[create_account_number(),random.choice(balances)]
        
    account_with_name_number
        
    with open("accounts.csv",mode="w",newline="",encoding="utf-8") as file:
        
        account=csv.writer(file)
        account.writerow(["Name","Account Number","Balance"])
        for name,account_and_balance in account_with_name_number.items():
            print(name,account_and_balance)
            account.writerow([name,account_and_balance[0],account_and_balance[1]])
