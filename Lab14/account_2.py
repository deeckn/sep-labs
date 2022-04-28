import persistent
from abc import ABC, abstractmethod
import datetime


class Customer(persistent.Persistent):
    def __init__(self, name: str = ""):
        self.name = name
        self.accounts = persistent.list.PersistentList()

    def __str__(self) -> str:
        return f"Customer Name: {self.name}"

    def add_account(self, account):
        self.accounts.append(account)
        return account

    def account(self, n: int):
        if 0 <= n < len(self.accounts):
            return self.accounts[n]
        return None

    def print_status(self):
        print(self.__str__())
        for account in self.accounts:
            print("\t", end="")
            account.print_status()


class BankTransaction(persistent.Persistent):
    def __init__(self, amount: float, old_balance: float, new_balance: float, ttype: str):
        self.amount = amount
        self.old_balance = old_balance
        self.new_balance = new_balance
        self.timestamp = datetime.datetime.now()
        self.ttype = ttype

    def print_details(self):
        print(self.ttype)
        print(f"\tAmount: {self.amount}")
        print(f"\tOld Balance: {self.old_balance}")
        print(f"\tNew Balance: {self.new_balance}")
        print(f"\tTimestamp: {self.timestamp}")
        print()


class Account(ABC):
    def __init__(self, balance: float = 0.0, owner: Customer = None):
        self.balance = balance
        self.owner = owner
        self.bank_transactions = persistent.list.PersistentList()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError(
            "Users must define __str__ to use the base class")

    @abstractmethod
    def deposit(self, amount):
        """Add cash to balance with specified amount"""
        raise NotImplementedError(
            "Users must define deposit to use the base class")

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw from account with specified amount"""
        raise NotImplementedError(
            "Users must define withdraw to use the base class")

    @abstractmethod
    def transfer(self, amount, account):
        """Transfer specified amount to another account"""
        raise NotImplementedError(
            "Users must define transfer to use the base class")

    @abstractmethod
    def account_detail(self):
        """Returns a string of the account details"""
        raise NotImplementedError(
            "Users must define account_detail to use the base class")

    def transfer_in(self, amount, account):
        """Receive specified amount from another account"""
        if issubclass(account.__class__, Account):
            self.balance += amount

            self.bank_transactions.append(BankTransaction(
                amount,
                self.balance-amount,
                self.balance,
                f"Transfer from {account.owner.name}"
            ))

    def get_balance(self) -> int | float:
        """Returns the balance of the account"""
        return self.balance

    def print_status(self):
        """Displays the status detaisl of the account"""
        print(self.__str__())

    def print_bank_transactions(self):
        self.print_status()
        print()

        for transaction in self.bank_transactions:
            transaction.print_details()


class SavingAccount(Account, persistent.Persistent):
    def __init__(self, balance: float = 0.0, owner=None, interest=1.0):
        Account.__init__(self, balance, owner)
        self.interest = interest

    def __str__(self) -> str:
        """String representation of the SavingAccount class"""
        return f"Saving Account of Customer: {self.owner.name} Balance: {self.balance:.2f} Interest: {self.interest:.2f}"

    def deposit(self, amount: int | float):
        """Add cash to balance with specified amount"""
        self.balance += amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance-amount,
            self.balance,
            "Deposit"
        ))

    def withdraw(self, amount: int | float):
        """Withdraw from account with specified amount"""
        if amount > self.balance:
            return
        self.balance -= amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance+amount,
            self.balance,
            "Withdraw"
        ))

    def transfer(self, amount: int | float, account: Account):
        """Transfer specified amount to another account"""
        if amount > self.balance:
            return

        account.transfer_in(amount, self)
        self.balance -= amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance+amount,
            self.balance,
            f"Transfer to {account.owner.name}"
        ))

    def account_detail(self) -> str:
        """Returns a string of the account details"""
        return self.__str__()


class CurrentAccount(Account, persistent.Persistent):
    def __init__(self, balance: float = 0.0, owner: Customer = None, limit: int | float = -5000):
        Account.__init__(self, balance, owner)
        self.limit = limit

    def __str__(self) -> str:
        return f"Current Account of Customer: {self.owner.name} Balance: {self.balance:.2f} Limit: {self.limit:.2f}"

    def deposit(self, amount: int | float):
        """Add cash to balance with specified amount"""
        self.balance += amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance-amount,
            self.balance,
            "Deposit"
        ))

    def withdraw(self, amount: int | float):
        """Withdraw from account with specified amount"""
        if amount < self.limit:
            return
        if amount > self.balance:
            return
        self.balance -= amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance+amount,
            self.balance,
            "Withdraw"
        ))

    def transfer(self, amount: int | float, account: Account):
        """Transfer specified amount to another account"""
        if amount > self.balance:
            return

        account.transfer_in(amount, self)
        self.balance -= amount

        self.bank_transactions.append(BankTransaction(
            amount,
            self.balance+amount,
            self.balance,
            f"Transfer to {account.owner.name}"
        ))

    def account_detail(self) -> str:
        """Returns a string of the account details"""
        return self.__str__()
