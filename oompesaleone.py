from abc import ABC, abstractmethod

# Encapsulation
class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        print(f"Withdrawing {amount}. Current balance: {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_holder_name(self):
        return self.holder_name

# Inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number

# Polymorphism
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        pass

class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)

class WithdrawTransaction(Transaction):
    def execute(self, account):
        account.withdraw(self.amount)

# Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_transaction(self, amount):
        pass

class MpesaPaymentSystem(PaymentSystem):
    def process_transaction(self, amount):
        print(f"Processing Mpesa transaction of {amount}")

# Example usage
mpesa = MpesaPaymentSystem()
account1 = Customer(1, "Jamal", 1000, "101352920")
deposit1 = DepositTransaction(200)
withdraw1 = WithdrawTransaction(100)

# Execute transactions
deposit1.execute(account1)
withdraw1.execute(account1)

# Check the balance
print(f"Balance for {account1.get_holder_name()} is: {account1.get_balance()}")

mpesa=MpesaPaymentSystem()
account2 = Customer(1, "alhabib", 500, "743616435")
deposit2 = DepositTransaction(200)
withdraw2 = WithdrawTransaction(1000)
deposit2.execute(account2)
withdraw2.execute(account2)
print(f"Balance for {account2.get_holder_name()} is: {account2.get_balance()}")