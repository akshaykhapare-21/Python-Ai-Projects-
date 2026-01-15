# Simple ATM Simulation
# Beginner Friendly Version

# fixed pin and starting balance
PIN = "1234"
balance = 1000


# function to check balance
def check_balance():
    print("Your current balance is:", balance)


# function to deposit money
def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Money deposited successfully.")


# function to withdraw money
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance.")


# main program starts here
print("WELCOME TO ATM")

user_pin = input("Enter your PIN: ")

if user_pin == PIN:
    print("PIN verified successfully.")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Wrong PIN. Access denied.")
