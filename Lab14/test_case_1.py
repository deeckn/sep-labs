import ZODB
import ZODB.FileStorage
import persistent
import BTrees.OOBTree
import transaction
import account_1 as account

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if __name__ == "__main__":
    root.customers = BTrees.OOBTree.BTree()
    root.customers["Jone"] = account.Customer("Jone")
    j = root.customers["Jone"]
    j.print_status()

    print()
    a = j.add_account(account.SavingAccount(400, j))
    b = j.add_account(account.CurrentAccount(200, j))
    a.print_status()
    b.print_status()
    j.print_status()

    print()
    b.withdraw(100)
    j.print_status()

    print()
    a.transfer(150, b)
    j.print_status()

    print()
    a.deposit(500)
    j.print_status()

    transaction.commit()
