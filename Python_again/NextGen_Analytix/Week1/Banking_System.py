def bank_system():
    ACCOUNTS = {}
    enter_choice = 'y'

    while enter_choice == 'y':

        print("\nWELCOME TO OnlyBanks!\n1.Create Account\n2.Check Balance\n3.Deposit Money\n4.Withdraw Money\n5.Exit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter numerical choice: ")

        def create_account():
            print("\nCREATE AN ACCOUNT: ")
            name = input("Enter your name: ").strip().title()
            if name not in ACCOUNTS:
                try:
                    balance = float(input("Enter your balance: "))
                    if balance > 0:
                        ACCOUNTS[name] = balance
                        return "Account created successfully!\n"
                    else:
                        return "Invalid balance entered!\n"
                    
                except ValueError:
                    return "Enter a valid amount!\n"
            else:
                return "Account already exists!\n"
        
        def check_balance():
            name = input("Enter the account you want to check balance: ").strip().title()
            try:
                return f"{name}'s balance: {ACCOUNTS[name]}" 
            except KeyError:
                return "Account doesn't exist!\n"
            
        def deposit_money():
            try:
                name = input("Enter the account you want to deposit: ").strip().title()
                amt = float(input("Enter the amount to deposit: "))
                if amt <=0:
                    return "Invalid amount entered!"
                else:
                    ACCOUNTS[name] += amt
                    return f"Balance deposited successfully!\nNew Balance: {ACCOUNTS[name]}"
            except KeyError:
                return "Account doesn't exist!\n"
            except ValueError:
                return "Invalid amount entered!\n"
            
        
        def withdraw_money():
            try:
                name = input("Enter the account you want to withdraw from: ").strip().title()
                amt = float(input("Enter the amount to withdraw: "))
                if amt > 0:
                    if amt > ACCOUNTS[name]:
                        return "Less balance. You are poor!\n"
                    else:
                        ACCOUNTS[name] -= amt
                        return "Balance withdrawn successfully!\n"
                else:
                    return "Negative amount can't be withdrawn!"
            except KeyError:
                return "Account doesn't exist!\n"
            except ValueError:
                return "Invalid amount entered!\n"
            

        if choice == 1:
            print(create_account())
            enter_choice = input("Do you want to continue (y/n)?: ")

        elif choice == 2:
            print(check_balance())

        elif choice == 3:
            print(deposit_money())

        elif choice == 4:
            print(withdraw_money())

        elif choice == 5:
            enter_choice = input("Do you want to exit (y/n)?: ")
        
        else:
            print("No operations exist for this choice!")

if __name__ == '__main__':
    bank_system()
