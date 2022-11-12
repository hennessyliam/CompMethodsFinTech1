import re


# exception handling to only allow "yYnN" input
def get_transaction_choice_input(transaction_choice):
    if not re.search("[yYnN]", transaction_choice):
        print("Invalid input. Please enter either y or n.")
        return get_transaction_choice_input(input("Would you like to make another transaction? "))
    else:
        print("Thank you for banking with us!")
        print("Printing receipt...")
        print("********************************")
        print("Transaction is now complete.")
        #print("Account holder: " + account_holder)
        #print("Account number: " + account_number)
        print("Thank you for choosing FinTech as your bank!")
        print("********************************")
    

print(get_transaction_choice_input(input("Would you like to make another transaction? ")))