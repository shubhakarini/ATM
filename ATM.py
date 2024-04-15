# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:21:02 2023

@author: CMP
"""
import tkinter as tk
import random

class ATMInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure PIN Entry")

        self.pin_digits = [str(i) for i in range(10)]
        self.pin_entry = []
        self.pin_label = tk.Label(root, text="Enter PIN:")
        self.pin_label.pack()

        self.create_dynamic_keypad()

    def create_dynamic_keypad(self):
        # Randomize the layout of the keypad
        random.shuffle(self.pin_digits)

        for digit in self.pin_digits:
            button = tk.Button(self.root, text=digit, width=5, height=2, command=lambda d=digit: self.handle_keypress(d))
            button.pack(side=tk.LEFT)

    def handle_keypress(self, digit):
        # Process the keypress (e.g., display '*' on the screen)
        self.pin_entry.append(digit)
        self.display_masked_pin()

    def display_masked_pin(self):
        # Display '*' for each entered digit
        masked_pin = '*' * len(self.pin_entry)
        self.pin_label.config(text=f"Enter PIN: {masked_pin}")

        # Check if the PIN entry is complete (e.g., 4 digits)
        if len(self.pin_entry) == 4:
            self.verify_pin()

    def verify_pin(self):
        # Add your PIN verification logic here
        entered_pin = ''.join(self.pin_entry)

        # For demonstration purposes, printing the entered PIN
        print("Entered PIN:", entered_pin)

        # Clear PIN entry after verification
        self.clear_pin_entry()

    def clear_pin_entry(self):
        # Clear PIN entry and create a new dynamic keypad for the next entry
        self.pin_entry = []
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_dynamic_keypad()


if __name__ == "__main__":
    root = tk.Tk()
    atm_interface = ATMInterface(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM GUI")

        # Initialize balance
        self.balance = 1000

        # Create labels
        self.balance_label = tk.Label(root, text="Balance: $1000")
        self.amount_label = tk.Label(root, text="Enter Amount:")

        # Create entry widget
        self.amount_entry = tk.Entry(root)

        # Create buttons
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)

        # Layout
        self.balance_label.grid(row=0, column=0, columnspan=2)
        self.amount_label.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)
        self.withdraw_button.grid(row=2, column=0)
        self.deposit_button.grid(row=2, column=1)
        self.check_balance_button.grid(row=3, column=0, columnspan=2)

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.balance -= amount
                self.update_balance()

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            self.balance += amount
            self.update_balance()

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.balance}")

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero")
                return None
            return amount
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return None

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
