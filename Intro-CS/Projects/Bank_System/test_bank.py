from bank import (
    Account,
    SavingsAccount,
    CheckingAccount,
    BusinessAccount,
    total_money,
    richest_account,
    active_accounts
)

print("=" * 50)
print("ACCOUNT")
print("=" * 50)

acc1 = Account("Emmanuel", 500)

print(acc1)

acc1.deposit(250)
acc1.withdraw(100)

print(acc1.get_transaction_history())


print("\n" + "=" * 50)
print("SAVINGS ACCOUNT")
print("=" * 50)

save = SavingsAccount("Alice", 1000)

save.add_interest()

print(save)

save.withdraw(100)

print(save.get_transaction_history())


print("\n" + "=" * 50)
print("CHECKING ACCOUNT")
print("=" * 50)

check = CheckingAccount("Bob", 200)

check.withdraw(250)

print(check)

print("Remaining overdraft:", check.get_overdraft_amount())


print("\n" + "=" * 50)
print("BUSINESS ACCOUNT")
print("=" * 50)

biz = BusinessAccount(
    "Cybernerddd Ltd.",
    "GH-2026-001",
    15000
)

print(biz)


print("\n" + "=" * 50)
print("TRANSFER")
print("=" * 50)

acc1.transfer(save, 100)

print(acc1.get_balance())
print(save.get_balance())


print("\n" + "=" * 50)
print("HELPER FUNCTIONS")
print("=" * 50)

accounts = [acc1, save, check, biz]

print("Total money:", total_money(accounts))

print("Richest account:")
print(richest_account(accounts))

print("Active accounts:")

for acc in active_accounts(accounts):
    print(acc.get_holder())