# create a bank system
import csv

class BankAccount():
    all_accounts=[]
    def __init__(self,account_holder,account_number,balance=0.0):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
        BankAccount.all_accounts.append(self)
    def __repr__(self):
       return f"{self.account_holder}: {self.account_number}: {self.balance}"
    @classmethod
    def create_instance(self):
        with open("accounts.csv","r") as file:
            accounts=csv.DictReader(file)
            for account_h in accounts:
                BankAccount(
                    account_holder=account_h.get("Name"),
                    account_number=account_h.get("Account Number"),
                    balance=float(account_h.get("Balance")),
                    
        
        
                )
    def update_csv(self):
        """ Update the CSV file with the current account information """
        try:
            # Open the CSV file in write mode
            with open("accounts.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                # Write the headers
                writer.writerow(["Name", "Account Number", "Balance"])
                # Write the updated account data
                for account in BankAccount.all_accounts:
                    writer.writerow([account.account_holder, account.account_number, account.balance])
            
        except Exception as e:
            print(f"Error updating CSV file: {e}")
    @classmethod
    def get_account_by_name(cls, name):
        # Retrieve a specific account by the account holder's name
        
        for account in cls.all_accounts:
            if account.account_holder == name:
                return account
        return None
            
    def deposit(self,amount:float):
        if amount >0:
            print(f"""Available Balance:R {self.balance}
                    Amount to  be deposited:R {amount}""")
            
            self.balance=self.balance+amount
            print(f"New balance:R {self.check_balance}")
        else:
            print("Deposit valid amount")
        self.update_csv()


    def withdrawal(self,amount):
        if self.balance>=amount:
            print(f"You can withdraw maximum of:R {self.balance}")

            self.balance-=amount
        else:
            print(f"The amount you want to withdraw : R{amount} is greater than the avalible amount: R {self.balance}")
    
    def check_balance(self):
        return( f"R{self.balance}")
    @classmethod
    def transfer(cls, sender_name, recipient_name, amount):
        """ Transfer amount from one account to another """

        # Retrieve the sender and recipient accounts using the names provided
        sender_account = cls.get_account_by_name(sender_name)
        recipient_account = cls.get_account_by_name(recipient_name)

        if not sender_account:
            print(f"No account found for {sender_name}")
            return

        if not recipient_account:
            print(f"No account found for {recipient_name}")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if sender_account.balance < amount:
            print(f"Insufficient funds in {sender_name}'s account.")
            return

        # Perform the transfer
        sender_account.balance -= amount
        recipient_account.balance += amount
        print(f"You have a balance of :R {sender_account.balance}")

        print(f"Transferred R {amount:.2f} from {sender_name} to {recipient_name}.")
        print(f"{sender_name}'s new balance: R {sender_account.balance:.2f}")
      

        # Update the CSV file after the transfer
        sender_account.update_csv()
        recipient_account.update_csv()
        
BankAccount.create_instance()
name_to_search="Olivia Bennett"  # Example name
account = BankAccount.get_account_by_name(name_to_search)

if account: 
    account.deposit(40000)
    account.transfer("Olivia Bennett","Emma Taylor",5000)

