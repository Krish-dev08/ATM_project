"""
Full ATM System - Using only loops and if-else (no functions, no dictionaries)
"""

balance = 0
pin = "0000"
history = []

print("=" * 30)
print("   WELCOME TO PYTHON ATM")
print("=" * 30)

attempts = 0
logged_in = False

while attempts < 3:
    entered_pin = input("Enter PIN: ")

    if entered_pin == pin:
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("❌ Incorrect PIN! Attempts left:", 3 - attempts)

if logged_in == True:
    print("\n✅ Login successful!")

    running = True

    while running == True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance_pin = input("Enter PIN to check balance: ")

            if balance_pin == pin:
                print("💰 Current Balance:", balance)
            else:
                print("❌ Incorrect PIN!")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("❌ Enter a valid positive amount!")
            else:
                balance = balance + amount
                history.append("Deposited " + str(amount))
                print("✅ Money deposited successfully!")
                print("💰 New Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("❌ Enter a valid positive amount!")
            elif amount > balance:
                print("❌ Insufficient balance!")
            else:
                balance = balance - amount
                history.append("Withdrew " + str(amount))
                print("✅ Withdrawal successful!")
                print("💰 New Balance:", balance)

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin != pin:
                print("❌ Incorrect current PIN!")
            else:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    history.append("PIN changed")
                    print("✅ PIN changed successfully!")
                else:
                    print("❌ PIN must be exactly 4 digits!")

        elif choice == "5":
            print("\n----- TRANSACTION HISTORY -----")

            if len(history) == 0:
                print("No transactions yet.")
            else:
                count = 1
                for entry in history:
                    print(str(count) + ". " + entry)
                    count = count + 1

        elif choice == "6":
            print("🙏 Thank you for using ATM! Goodbye")
            running = False

        else:
            print("❌ Invalid choice! Try again.")

else:
    print("\n❌ Too many incorrect attempts. Card blocked!")