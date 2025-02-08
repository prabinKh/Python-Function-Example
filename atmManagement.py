"""
1. a function to deposite money
2. a function to withdraw money
3. a function to check the balance
4. a function to view the transaction history

"""
acount_balance = 0
transaction= []
def deposite_money(amount):
    global acount_balance, transaction
    if amount <= 0:
        return "invalid amount"
    else:
        acount_balance += amount
        transaction.append(f'Deposited $ {amount}')
        return f"${amount} Deposited successfully"
    
def withdraw_money(amount):
    global acount_balance, transaction
  
    if amount > 0 and amount <= acount_balance:
        acount_balance -= amount
        transaction.append(f'withdraw ${amount}')
        return f"${amount} withdraw successfully"
    else:
        return "insufficient balance"
   

def check_balance():
    global acount_balance
    return f"current balance is ${acount_balance}"

def transaction_historyss():
    global transaction
    if not transaction:
        return "no transaction history"
    else:
        return transaction
    
def __main__():
    while True:
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice 1 to 5: ")
        if choice == "1":
            amount = float(input('Enter the amount to deposite: '))
            print(deposite_money(amount))
        elif choice == "2":
            amount = float(input('Enter the amount to withdraw: '))
            print(withdraw_money(amount))
        elif choice == "3":
            print(check_balance())
        elif choice == "4":
            print(transaction_historyss())
        elif choice == "5":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    __main__()