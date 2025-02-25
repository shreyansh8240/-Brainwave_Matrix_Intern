class ATM:
    def __init__(self, balance):
        self.balance = balance

    def chek_balance(self):
        return self.balance 
    
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited succesfully. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"${amount} withdraw successfully. New balance: ${self.balance}"
        

def main():
     starting_balance = float(input("Enter starting balance: "))
     atm = ATM(starting_balance)

     while True:
         print("\nChoose an action:")
         print("1. Check Balance")
         print("2. Deposit")
         print("3. Withdraw")
         print("4. Exit" )

         choice = input("Enter your choice (1/2/3/4): ")


         if choice == "1":
             print("Your current balance is : $", atm.chek_balance())
         elif choice == "2":
             amount = float(input("Enter amount to deposit: "))
             print(atm.deposit(amount))
         elif choice == "3":
             amount = float(input("Enter amount to withdraw: "))
             print(atm.withdraw(amount))
         elif choice == "4":
             print("Thank you for using ATM.")
             break
         else:
             print("Invalid choice  Please choose a valid option.")

if __name__ == "__main__":
    main()
