import time


class Transaction:
    def __init__(self, timestamp, transaction_type, amount, description):
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        
    def __str__(self):
        return (
            f"{self.timestamp} | "
            f"{self.transaction_type.capitalize():10} | "
            f"${self.amount:.2f} | "
            f"{self.description}"
        )


class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.__balance = balance
        self.transactions = []
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
            transaction = Transaction(
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                transaction_type="deposit",
                amount=amount,
                description="Deposit"
            )
            self.transactions.append(transaction)
            
            print(
                f"Deposited amount: ${amount:.2f}. "
                f"New balance: ${self.__balance:.2f}"
            )
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            
            transaction = Transaction(
                timestamp=time.strftime("%Y-%m-%d %H:%M:%S"),
                transaction_type="withdrawal",
                amount=amount,
                description="Withdrawal"
            )
            self.transactions.append(transaction)
            
            print(
                f"Withdrawn amount: ${amount:.2f}. "
                f"New balance: ${self.__balance:.2f}"
            )
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def get_balance(self):
        return self.__balance
    
    def get_transactions(self):
        statement = (
            f"\nAccount Number: {self.account_number}\n"
            f"Current Balance: ${self.__balance:.2f}\n"
            f"\nTransaction History:\n"
            f"{'-' * 65}\n"
        )
        if not self.transactions:
            statement += "No transactions yet.\n"
        else:
            for transaction in self.transactions:
                statement += str(transaction) + "\n"
        
        statement += "-" * 65
        
        return statement
    
    def __str__(self):
        return self.get_transactions()


def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            
            if amount >= 0:
                return amount
            
            print("Amount cannot be negative.")
            
        except ValueError:
            print("Please enter a valid number.")


def account_menu(account):
    while True:
        print(f"\nAccount: {account.account_number}")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Bank statement")
        print("4. Balance")
        print("5. Return to account selection")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            amount = get_amount("Enter withdrawal amount: ")
            account.withdraw(amount)
        
        elif choice == "2":
            amount = get_amount("Enter deposit amount: ")
            account.deposit(amount)
        
        elif choice == "3":
            print(account)
        
        elif choice == "4":
            print(f"Current balance: ${account.get_balance():.2f}")
        
        elif choice == "5":
            print("Returning to account selection...")
            break
        
        else:
            print("Invalid option. Please choose a number from 1 to 5.")


def run_bank():
    accounts = {
        "1895": BankAccount(
            account_number="1895207253",
            pin="1895",
            balance=10000
        )
    }
    
    while True:
        print("\nBank accounts")
        print("1. Select an account")
        print("2. Create an account")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            pin = input("Enter your PIN: ").strip()
            
            account = accounts.get(pin)
            
            if account is None:
                print("Incorrect PIN or account not found.")
            else:
                account_menu(account)
                
        elif choice == "2":
            account_number = input(
                "Enter a new account number: "
            ).strip()
            
            if not account_number:
                print("Account number cannot be empty.")
                continue
            
            pin = input("Create a PIN: ").strip()
            
            if not pin:
                print("PIN cannot be empty.")
            elif pin in accounts:
                print("That PIN is already in use.")
            else:
                accounts[pin] = BankAccount(
                    account_number=account_number,
                    pin=pin,
                    balance=get_amount(
                        "Enter the opening balance: ")
                )
                
                print("Account created successfully.")
        
        elif choice == "3":
            print("Thank you for using our app!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    run_bank()