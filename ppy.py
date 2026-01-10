class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return  # Exit the method if insufficient balance
        self.balance -= amount   

    def deposit(self, amount):
        self.balance += amount


def transfer_money(sender, receiver, amount):
    if sender is None or receiver is None:
        print("Transfer failed: Invalid sender or receiver.")
        return
    sender.withdraw(amount)
    receiver.deposit(amount)


accounts = [
    BankAccount("Alice", 5000),
    BankAccount("Bob", 3000)
]

# Find account by name
def get_account(name):
    for acc in accounts:
        if acc.name == name:
            return acc
    return None


sender = get_account("Alice")
receiver = get_account("Charlie")  

# Check if receiver is valid before attempting to transfer money
if receiver is not None:
    transfer_money(sender, receiver, 7000)  
else:
    print("Transfer failed: Receiver account not found.")

print("Transfer complete")
print("Sender balance:", sender.balance)
if receiver is not None:
    print("Receiver balance:", receiver.balance)
else:
    print("Receiver account not found.")

# CodeSentinal: created for you by RuchirAdnaik.