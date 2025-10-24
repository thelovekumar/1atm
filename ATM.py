class ATM:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.__pin = pin          
        self.__balance = balance  

    # Private method to check pin
    def __verify_pin(self, pin):
        return self.__pin == pin

    # Public method to check balance
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            print(f"Your Current Balance is ₹{self.__balance}")
        else:
            print(" Invalid PIN")

    # Public method to withdraw money
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f" Withdrawal of ₹{amount} successful!")
                print(f"Remaining Balance: ₹{self.__balance}")
            else:
                print(" Insufficient balance or invalid amount.")
        else:
            print(" Invalid PIN")

    # Public method to deposit money
    def deposit(self, amount, pin):
        if self.__verify_pin(pin):
            if amount > 0:
                self.__balance += amount
                print(f" Deposit of ₹{amount} successful!")
                print(f"Updated Balance: ₹{self.__balance}")
            else:
                print(" Invalid amount.")
        else:
            print(" Invalid PIN")


#  Using the class (simulation)
user1 = ATM("1234-5678-9000", 1234, 5000)

# Correct PIN
user1.check_balance(1234)
user1.deposit(1000, 1234)
user1.withdraw(2000, 1234)

# Wrong PIN
user1.withdraw(1000, 9999)

# Direct access attempt
print(user1.check_balance)  
