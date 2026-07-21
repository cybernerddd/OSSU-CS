class Account(object):
    """A banking Account System"""
    def __init__(self, account_holder, balance=0.0):
        """
        Input: account holder name and initial balance
        which is optinal, also
        holds have account type, status and the account
        number info...
        """
        self.holder = account_holder
        self.account_number = "0000000001"

        self.balance = balance
        self.type = "Account"
        self.status = "Active" # Active / Frozen
        self.transactions = []

        # Record initial balance if provided
        if balance > 0:
            self.transactions.append({
                "type": "initial deposit",
                "amount": balance
            })
    
    def get_holder(self):
        """returns the account holder name"""
        return self.holder
    
    def get_account_number(self):
        """returns the account number"""
        return self.account_number
    
    def get_balance(self):
        """returns the current balance of the account"""
        return self.balance
    
    def get_account_type(self):
        """returns the type of account, being i.e.savings, checking or other"""
        return self.type

    def get_status(self):
        """return active if account is active, Frozen o.w."""
        return self.status
    
    def set_holder(self, new):
        """updates the account holder to 'new'"""
        self.holder = new

    def set_status(self, other):
        """update the account status to other"""
        self.status = other # will update so it switches between active/Frozen

    ##########################################################################
    ##########################################################################
    #                     Banking  Operations                                #
    ##########################################################################

    def deposit(self, amount):
        """add money to your account,
        record transaction if successful."""
        if (amount <= 0):
            raise ValueError("You can't deposit that amount.")
        
        self.balance += amount
        
        # record the transaction
        self.transactions.append({
            "type": "transfer_in",
            "amount": amount,
            "Available balance": self.get_balance()
        })
        print(f"Deposit successful! You have deposited ${amount}.")
        
    def withdraw(self, amount):
        """subtract amount from your balance
        if enough in account and,
        record the transaction after successful
        raise error o.w.."""

        if (amount <= 0) or (amount > self.balance):
            raise ValueError("Failed! Please check your current balance.")
        
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Amount withdrawn: GH₵{amount}")
            self.transactions.append({
                "type": "transfer_out",
                "amount": amount,
                "Available balance": self.get_balance()
            })
        
    def transfer(self, other_account, amount):
        """transfer amount to other account."""       
        # check if user has the amount in current balance first.      
         
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")
        
        # Withdraw from self
        self.balance -= amount
        self.transactions.append({
        "type": "transfer_out",
        "amount": amount,
        "to": other_account.get_account_number()
        })

        # Deposit into receiver
        other_account.balance += amount
        other_account.transactions.append({
            "type": "transfer_in",
            "amount": amount,
            "from": self.get_account_number()
        })
        print(f"Transfer successful! Sent ${amount} to {other_account.get_holder()}.")


    def get_transaction_history(self):
        """returns the total transaction history"""
        return self.transactions
    
    def __str__(self):
        """returns the text graphical format of your account."""
        return ("==============================\n"
            "\n\n🏦 Cybernerddd Finance\n\n" 
            f"Account Holder: {self.get_holder()}\n"
            f"Account Number: {self.get_account_number()}\n"
            f"Current Balance: GH₵{self.get_balance():,.2f}\n"
            f"Account Type: {self.type}\n"
            f"Status: {self.get_status()}\n\n"
            f"=============================="
        )

    def __eq__(self, other):
        """returns true if two accouns are equal,
          if they have the same account number."""
        return (self.get_account_number() == other.get_account_number())
    

class SavingsAccount(Account):
    """Subclass of account Class, for savings"""



    def __init__(self, account_holder, balance=0, interest_rate=0.05, account_limit=500):
        """added interest rate attribute which is optional,
        defaulting to 0.05"""
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
        # add account limit
        self.account_limit = account_limit
        # rewrite accoint type
        self.type = "Savings account"
        

        # check if user supplies interest rate
        # if interest_rate != 0.05:
        #     self.add_interest(self.interest_rate)

    def add_interest(self):
        """Apply interest to the savings account balance."""
        # calculate interest amount
        interest_amount = self.balance * (self.interest_rate / 100)

        # add interest to balance
        self.balance += interest_amount

        # record transaction
        self.transactions.append({
            "type": "interest",
            "amount": interest_amount,
            "Available balance": self.get_balance()
        })

        print(f"Interest of GH₵{interest_amount:.2f} added. New balance: GH₵{self.balance:.2f}")


    def get_interest_rate(self):
        """returns the interest rate"""
        return self.interest_rate #   f"Your savings account interest rate is {self.interest_rate}% anually. Thank You!"
    
    def get_account_limit(self):
        """returns your account limit"""
        return self.account_limit
    
    def withdraw(self, amount):
        """Withdraw from your savings account.
           Declines when you've passed daily
           limit for withdrawals."""

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        
        # calculate total withdrawals so far
        total_withdrawals = sum(
            tx["amount"] for tx in self.get_transaction_history()
            if tx["type"] == "transfer_out"
        )

        # check against account limit
        if total_withdrawals + amount > self.account_limit:
            raise ValueError(
                f"Withdrawal denied! Daily limit of GH₵{self.account_limit} exceeded."
            )
        
        # if within limit, perform withdrawal
        self.balance -= amount
        self.transactions.append({
            "type": "transfer_out",
            "amount": amount,
            "Available balance": self.get_balance()
        })
        print(f"Withdrawal successful! Amount withdrawn: GH₵{amount}")

    def __str__(self):
        """returns the text graphical format of your savings account."""
        return ("==============================\n"
            "\n\n🏦 Cybernerddd Finance\n\n" 
            f"Account Holder: {self.get_holder()}\n"
            f"Account Number: {self.get_account_number()}\n"
            f"Current Balance: GH₵{self.get_balance():,.2f}\n"
            f"Account Type: {self.type}\n"
            f"Interest Rate: {self.interest_rate}%\n"
            f"Status: {self.get_status()}\n\n"

            f"=============================="
        )


class CheckingAccount(Account):
    """subclass of Account, for checking holders"""

    def __init__(self, account_holder, balance=0, overdraft=100):
        """adds an overdraft feat, checking account
         can go overdraft
        """
        super().__init__(account_holder, balance)
        self.overdraft = overdraft
        self.type = "Checking account" # modify the account type
        
        self.overdraft_allowed = True # keeps track of ppl to give o.d.
    
    def get_overdraft_status(self):
        """returns True if you qualify for overdraft,
        False o.w."""
        return self.overdraft_allowed
    
    def get_overdraft_amount(self):
        """return overdraft remaining"""
        return self.overdraft
    
    def set_overdraft(self, value):
        """sets the overdraft qualification
        """
        self.overdraft = value

    def withdraw(self, amount):
        """Withdraw with overdraft support."""

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        # Check if balance + overdraft covers the withdrawal
        if amount <= (self.balance + self.overdraft):
            # First use balance if available
            if amount <= self.balance:
                self.balance -= amount
            else:
                # Use up balance first, then overdraft
                overdraft_used = amount - self.balance
                self.balance = 0
                self.overdraft -= overdraft_used   # <-- reduce overdraft limit

            # Record transaction
            self.transactions.append({
                "type": "transfer_out",
                "amount": amount,
                "Available balance": self.get_balance(),
                "Remaining overdraft": self.overdraft
            })

            print(f"Withdrawal successful! Amount withdrawn: GH₵{amount}")
        else:
            exceeded = amount - (self.balance + self.overdraft)
            print(
                f"Not enough funds! You exceeded your overdraft by GH₵{exceeded}"
            )
            raise ValueError("Withdrawal denied! Exceeds overdraft + balance limit.")
        
    def reset_overdraft(self, limit=100):
        """resets the overdraft, since Banks reset every month"""
        self.overdraft = limit
        print(f"Overdraft reset to GH₵{limit}")
        
    def __str__(self):
        """returns the text graphical format of your account."""
        return ("==============================\n"
            "\n\n🏦 Cybernerddd Finance\n\n" 
            f"Account Holder: {self.get_holder()}\n"
            f"Account Number: {self.get_account_number()}\n"
            f"Current Balance: GH₵{self.get_balance():,.2f}\n"
            f"Status: {self.get_status()}\n"
            f"Account Type: {self.type}\n"
            f"Overdraft Remaining: {self.get_overdraft_amount()}\n\n"
            f"=============================="
        )

class BusinessAccount(Account):
    """Account subclass for businesses"""

    def __init__(self, business_name, business_id, balance=0.0):
        """
        business_name replaces the account holder name.
        business_id is a unique identifier for the business.
        """
        super().__init__(business_name, balance)
        self.business_name = business_name
        self.business_id = business_id
        self.type = "Business Account"

    def get_business_id(self):
        """returns the business id"""
        return self.business_id
    
    def __str__(self):
        """returns the text graphical format of your account."""
        return ("==============================\n"
            "\n\n🏦 Cybernerddd Finance\n\n" 
            f"Business Name: {self.business_name}\n"
            f"Business ID: {self.get_business_id()}\n"
            f"Current Balance: GH₵{self.get_balance():,.2f}\n"
            f"Account Type: {self.type}\n"
            f"=============================="
        )


def total_money(accounts):
    """returns sum of all accounts in the list"""
    total = 0

    for acc in accounts: # acc1,acc3..
        balances = acc.get_balance()
        total += balances

    return total

def richest_account(accounts):
    richest_bal = 0.0
    richest_acc = None
    """returns the richest account from the list"""
    
    for acc in accounts: 
        # compare each account's balance

        if acc.get_balance() > richest_bal:
            richest_bal = acc.get_balance()
            richest_acc = acc
    
    return richest_acc

def active_accounts(accounts):
    """returns only accunts that are active"""
    # stores the actuve accounts in list
    actives = []

    for acc in accounts:
        # check for account's status
        stat = acc.get_status()
        
        if stat == "Active":
            # append it to the actives list
            actives.append(acc)
    return actives


