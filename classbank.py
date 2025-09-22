class BankAccount:
    def __init__(self, account_num, pin, branch_code, balance, name):
        self.account_num = account_num
        self.pin = pin
        self.branch_code = branch_code
        self.balance = balance
        self.name = name

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            raise IncorrectPin("Entered Pin is incorrect")
        if amount > self.balance:
            raise InsufficientBalance("Not enough balance")
        if amount <= 0:
            raise InvalidAmount("Enter a valid amount")
        self.balance -= amount
        self.update_account_file()
        return f"Withdraw successful. Remaining balance: {self.balance}"

    def deposit(self, amount, entered_pin):
        if entered_pin != self.pin:
            raise IncorrectPin("Entered Pin is incorrect")
        if amount <= 0:
            raise InvalidAmount("Invalid Amount Entered")
        self.balance += amount
        self.update_account_file()
        return f"Deposit successful. Remaining balance: {self.balance}"

    def check_balance(self):
        return f"Remaining balance: {self.balance}"

    def transfer(self, receiver_account, amount):
        if amount > self.balance:
            raise InsufficientBalance("Not enough balance")
        if amount <= 0:
            raise InvalidAmount("Enter a valid amount")
        receiver_account.balance += amount
        self.balance -= amount
        self.update_account_file()
        receiver_account.update_account_file()
        return f"Transaction successful. Remaining balance: {self.balance}"

    def update_account_file(self):
        with open(f"{self.account_num}.txt", "w") as file:
            file.write(f"{self.name}{self.account_num}\n{self.pin}\n{self.balance}\n{self.branch_code}")

class InvalidAccountNumber(Exception):
    pass

class UnidentifiedError(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class InvalidAmount(Exception):
    pass

class IncorrectPin(Exception):
    pass

def load_account(account_num):
    with open("accounts.txt", "r") as file:
        if f"{account_num}.txt\n" not in file.readlines():
            raise InvalidAccountNumber("Account does not exist")
    with open(f"{account_num}.txt", "r") as file:
        name = file.readline()
        account = int(file.readline())
        pin = int(file.readline())
        balance = float(file.readline())
        branch_code = file.readline()
    return BankAccount(account, pin, branch_code, balance, name)

def main():
    account_num = input("Enter the account number: ")
    try:
        account = load_account(account_num)
        print(f"Welcome to Virtual Banking Systems, {account.name}")
        while True:
            print("Choose an option:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Transfer")
            print("5. Exit")
            option = int(input())
            if option == 5:
                break
            elif option == 1:
                amount = int(input("Enter withdrawal amount: "))
                entered_pin = int(input("Enter PIN: "))
                print(account.withdraw(amount, entered_pin))
            elif option == 2:
                amount = int(input("Enter deposit amount: "))
                entered_pin = int(input("Enter PIN: "))
                print(account.deposit(amount, entered_pin))
            elif option == 3:
                print(account.check_balance())
            elif option == 4:
                receiver_acc_num = input("Enter receiver's account number: ")
                receiver_account = load_account(receiver_acc_num)
                amount = int(input("Enter transfer amount: "))
                print(account.transfer(receiver_account, amount))
            else:
                print("Invalid option. Try again.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
