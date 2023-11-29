# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 18:20:50 2023

@author: Yang Cairong
"""

class BankAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def transfer(self, target_account, amount):
        if target_account == self:
            raise ValueError("Cannot transfer money to yourself.")
        if amount > self.balance:
            raise ValueError("Not enough balance to transfer.")
        self.balance -= amount
        target_account.deposit(amount)

# # Example usage of Level 1 functions
# account1 = BankAccount("123")
# account2 = BankAccount("456")

# account1.deposit(1000)
# account2.deposit(500)

# print(f"Account 1 balance: {account1.balance}")
# print(f"Account 2 balance: {account2.balance}")

# account1.transfer(account2, 300)

# print(f"Account 1 balance after transfer: {account1.balance}")
# print(f"Account 2 balance after transfer: {account2.balance}")

from heapq import nlargest

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id):
        if account_id in self.accounts:
            raise ValueError(f"Account '{account_id}' already exists.")
        self.accounts[account_id] = BankAccount(account_id)

    def get_top_n_accounts(self, n):
        return nlargest(n, self.accounts.values(), key=lambda account: (account.balance, account.account_id))

# Example usage of Level 2 functions
bank = Bank()

bank.create_account("123")
bank.create_account("456")
bank.create_account("789")

bank.accounts["123"].deposit(1000)
bank.accounts["456"].deposit(500)
bank.accounts["789"].deposit(1500)

top_accounts = bank.get_top_n_accounts(2)
for account in top_accounts:
    print(f"Account ID: {account.account_id}, Balance: {account.balance}")

import time

class ScheduledPaymentsBank(Bank):
    def schedule_payment(self, account_id, amount, interval):
        if account_id not in self.accounts:
            raise ValueError(f"Account '{account_id}' does not exist.")
        while True:
            time.sleep(interval)
            self.accounts[account_id].deposit(amount)

# Example usage of Level 3 function
scheduled_bank = ScheduledPaymentsBank()

scheduled_bank.create_account("001")
scheduled_bank.create_account("002")

scheduled_bank.accounts["001"].deposit(1000)
scheduled_bank.accounts["002"].deposit(500)

# Schedule a payment of 200 every 3 seconds for account "001"
scheduled_bank.schedule_payment("001", 200, 3)

# Wait for payments to occur (you may interrupt the program manually)
