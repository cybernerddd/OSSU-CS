# 🏦 Bank Account System Checklist

## 📌 Phase 1: Build the Base Account Class

### Step 1 — Create the Class
- [✅  ] Create the `Account` class
- [✅ ] Add a class docstring
- [✅ ] Create the `__init__()` constructor

---

### Step 2 — Add Instance Variables
- [ ✅] `holder`
- [✅ ] `account_number`
- [✅ ] `balance`
- [✅ ] `account_type`
- [ ✅] `status`
- [ ✅] `transactions`

---

### Step 3 — Create Getters
- [✅ ] `get_holder()`
- [✅ ] `get_account_number()`
- [✅ ] `get_balance()`
- [ ✅] `get_account_type()`
- [ ✅] `get_status()`

---

### Step 4 — Create Setters
- [ ✅] `set_holder()`
- [✅ ] `set_status()`

---

## 💰 Phase 2: Banking Operations

### Step 5 — Deposit
- [ ✅] Create `deposit()`
- [ ✅] Reject invalid deposits
- [✅ ] Update balance
- [ ✅] Record transaction

---

### Step 6 — Withdraw
- [ ✅] Create `withdraw()`
- [✅ ] Reject invalid withdrawals
- [ ✅] Check sufficient balance
- [ ✅] Update balance
- [✅ ] Record transaction

---

### Step 7 — Transfer
- [ ✅] Create `transfer()`
- [✅ ] Withdraw from sender
- [ ✅] Deposit into receiver
- [  ✅] Record both transactions

---

## 📒 Phase 3: Transaction History

### Step 8 — Transactions
- [ ✅ ] Design transaction format
- [  ✅] Store every deposit
- [  ✅] Store every withdrawal
- [  ✅] Store every transfer

---

### Step 9 — Transaction History
- [ ✅ ] Create `get_transaction_history()`

---

## 🖨️ Phase 4: Special Methods

### Step 10 — String Representation
- [✅ ] Implement `__str__()`
- [ ✅] Display account information nicely

---

### Step 11 — Equality
- [✅ ] Implement `__eq__()`

---

## 🏦 Phase 5: Inheritance

### Step 12 — SavingsAccount
- [ ✅] Create `SavingsAccount`
- [ ✅] Add interest rate
- [ ✅] Add `add_interest()`
- [ ✅ ] Add `add_ daily limit for withdraw`

---

### Step 13 — CheckingAccount
- [ ✅] Create `CheckingAccount`
- [ ✅] Add overdraft limit

---

### Step 14 — BusinessAccount
- [ ✅ ] Create `BusinessAccount`
- [ ✅ ] Add business name
- [  ✅] Add business ID

---

## 🔄 Phase 6: Polymorphism

### Step 15
- [✅ ] Override methods where appropriate
- [ ✅ ] Test inherited behavior

---

## 🛠️ Phase 7: Utility Functions

### Step 16
- [ ✅] `total_money(accounts)`
- [ ✅] `richest_account(accounts)`
- [ ✅] `active_accounts(accounts)`

---

## ⭐ Phase 8: Advanced Features

### Step 17
- [ ] Freeze account
- [ ] Unfreeze account
- [ ] Account creation date
- [ ] PIN verification
- [ ] Monthly statement
- [ ] Save accounts to JSON
- [ ] Load accounts from JSON

---

# ✅ Final Review

- [ ] Test every class
- [ ] Test inheritance
- [ ] Test polymorphism
- [ ] Add comments/docstrings
- [ ] Create README.md
- [ ] Push to GitHub
- [ ] Write LinkedIn post