#atleast 5 exceptions
def accountInput():
    account_no=int(input("Enter your 9 digit account number: "))
    try:
        if account_no==Accounts["Harshit Gurjar"]["Account Number"]:
            person="Harshit Gurjar"
            return person
        elif account_no==Accounts["Ravi Kumar"]["Account Number"]:
            person="Ravi Kumar"
            return person
        elif account_no==Accounts["Tushar Kumar"]["Account Number"]:
            person="Tushar Kumar"
            return person
        else: 
            raise InvalidAccountNumber()
        return 0
    except:
        print("Please check your account number and try again")
        return 0

class InvalidAccountNumber(Exception):
    pass
class UnidentifiedError(Exception):
    pass
class InsufficientBalance(Exception):
    pass
class invalidamount(Exception):
    pass
class IncorrectPin(Exception):
    pass
Accounts={"Harshit Gurjar":{
    "Holder's Name": "Harshit Gurjar",
    "Account Number": 240190199,
    "Pin":5555,
    "Balance":132.46,
    "BranchCode":"PremN2345"

},
"Ravi Kumar":{
    "Holder's Name": "Ravi Kumar",
    "Account Number":321131332,
    "Pin":4444,
    "Balance":422.43,
    "BranchCode":"Mycity8748",

},
"Tushar Kumar":{
    "Holder's Name":"Tushar Kumar",
    "Account Number":532443244,
    "Pin":3333,
    "Balance":5555.55,
    "BranchCode":"GGN7657",
}
}

print("Welcome to Virtual Banking Sytems")
person=accountInput()
if person!=0:
    print(f"Hi {person}! How may i help you today?\nYou may choose the following options:")
    print("1 for Withdraw")
    print("2 for Deposit")
    print("3 to Check Balance")
    print("4 to Transfer to another account")
    print("5 to Exit\n")
    n=int(input(""))
    if(n==1):

        withdraw_amt=int(input("How much amount would you like to withdraw sir?\n"))
        enteredpin=int(input("Enter your 4 digit pin"))
        try:
            if enteredpin==Accounts[person]["Pin"]:
                if withdraw_amt>Accounts[person]["Balance"]:
                    raise InsufficientBalance("You are Way too Gareeb sir")
                elif withdraw_amt<=0:
                    raise invalidamount("Enter a valid amount")
                else:
                    print("Withdraw successfull")
                    Accounts[person]["Balance"]=Accounts[person]["Balance"]-withdraw_amt
                    print(f"Remaining balance is {Accounts[person]["Balance"]}")
            else:
                raise IncorrectPin("Entered Pin is incorrect")
        except Exception as e:
            print(e)
    
    if(n==2):
            deposit_amt=int(input("Enter the amout you want to deposit\n"))
            enteredpin=int(input("Enter your 4 digit pin"))
            try:
                if enteredpin==Accounts[person]["Pin"]:
                    if deposit_amt<=0:
                        raise invalidamount("Invalid Amount Entered")
                    else:
                        Accounts[person]["Balance"]+=deposit_amt
                        print(f"The updated balance is {Accounts[person]["Balance"]}")
            except Exception as e:
                print(e)