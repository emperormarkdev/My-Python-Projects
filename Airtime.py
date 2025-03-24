# Initial balances
bank_balance = 1200
aloan_balance = 750
dloan_balance = 750

# Get user name
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Display options
print("\nHome: ")
print("1: Buy Airtime")
print("2: Buy Data")
print("3: Borrow Airtime")
print("4: Borrow Data")

# Get user choice
tchoice = int(input("Input a number: "))

# Option 1: Buy Airtime
if tchoice == 1: 
    airtime_amount = int(input("Please enter Airtime Amount: "))

    if bank_balance - airtime_amount > 57:
        bank_balance -= airtime_amount
        print("Airtime purchase successful!")
        print(f"Your Bank Balance is {bank_balance}")
    else:
        print("Insufficient Funds, please fund your wallet.")

# Option 2: Buy Data
elif tchoice == 2:
    data_amount = int(input("Please enter Data Amount: "))

    if bank_balance - data_amount > 57:
        bank_balance -= data_amount
        print("Data purchase successful!")
        print(f"Your Bank Balance is {bank_balance}")
    else:
        print("Insufficient Funds, please fund your wallet.")

# Option 3: Borrow Airtime
elif tchoice == 3:
    aloan_amount = int(input("Please enter Airtime Loan amount: "))
    aloan_eligibility = int(input("Enter your Airtime Loan eligibility: "))

    if aloan_amount <= aloan_eligibility and aloan_amount <= bank_balance:
        print("Successful!")
        print(f"{name}, you have been credited with {aloan_amount}.")
    else:
        print("Unsuccessful! Please fund your wallet.")

# Option 4: Borrow Data
elif tchoice == 4:
    dloan_amount = int(input("Please enter Data Loan amount: "))
    dloan_eligibility = int(input("Enter your Data Loan eligibility: "))

    if dloan_amount <= dloan_eligibility and dloan_amount <= bank_balance:
        print("Successful!")
        print(f"{name}, you have been credited with {dloan_amount}.")
    else:
        print("Unsuccessful! Please fund your wallet.")

# Invalid Choice
else:
    print("Invalid option. Please enter a valid number.")
