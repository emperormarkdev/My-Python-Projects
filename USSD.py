# A USSD pyhton code for a savings app, allowing a user to perform transactions 

name = input("Enter your name: ") # name of user
print(f"Welcome {name}, please proceed with your transactions")
balance = int(input("Enter initial deposit: ")) # balance in bank
 
print("Please select transaction")
print("1: Deposit money")
print("2: Withdraw money")
print("3: Check balance")


tchoice = int(input("Enter your choice (1-3): "))

if tchoice == 1: # choose 1 to deposit money
    deposit_amount = float(input("Please enter deposit amount: "))
    new_balance = balance + deposit_amount
    print("Transaction sucessful")
    print(f"{name}, your balance is {new_balance}")

elif tchoice == 2: # choose 2 to withdraw money
    withdrawal_amount = float(input("Please enter withdrawal amount: "))
    new_balance = balance - withdrawal_amount
    
    if balance > withdrawal_amount: # condition for withdrawal
        print("Transaction Sucessful")
        print(f"{name}, your balance is {new_balance}")
    else:
        print(f"{name}, Oops looks like you have Insufficient funds")

elif tchoice == 3: # choose 3 to check balance
    print(f"{name}, your balance is {balance}")

else:
    print(f"{name}, Oops looks like you've entered an Invalid input, please try again later") # if the user enters a wrong number,
                                                                                             # he gets thus error code
              
