class BankAccount(object):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    # deposit method
    
    def deposit(self, amount):
        """
        input: int,
        adds money to the balance
        """
        self.balance += amount
        return self.balance
        
    # withdraw method
    
    def withdraw(self, amount):
        """
        input: int,
        subtracts the withdrawal from
        balance
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        else:
            self.balance -= amount
        return self.balance
    
    # check balance
    def get_balance(self):
        """
        input: no args,
        return current balance
        """
        return self.balance
    
# examples
acc = BankAccount("Cyber", 500)

acc.deposit(100)

print(acc.get_balance())
# 600

acc.withdraw(250)

# print(acc.get_balance())
# # 350
