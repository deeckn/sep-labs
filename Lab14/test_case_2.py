import ZODB
import ZODB.FileStorage
import persistent
import BTrees.OOBTree
import transaction
import account_2 as account

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers["Jone"] = account.Customer("Jone")
    root.customers["Mary"] = account.Customer("Mary")
    j = root.customers["Jone"]
    m = root.customers["Mary"]
    j.print_status()

    a = j.add_account(account.SavingAccount(100, j))
    b = j.add_account(account.CurrentAccount(200, j))
    c = j.add_account(account.SavingAccount(1000, m))

    c.transfer(100, a)
    a.transfer(150, b)
    b.deposit(500)
    b.withdraw(50)
    b.transfer(200, c)
    c.withdraw(250)

    print()
    print("Account C")
    print()
    c.print_bank_transactions()

    transaction.commit()
