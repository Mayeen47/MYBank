class MYBank:
    def __init__(my, balance):
        my.balance = balance
        my.min_withdraw = 500
        my.max_withdraw = 10000

    def get_balance(my):
        return my.balance
    def withdraw (my , amount):
        if amount < my.min_withdraw:
            return f"no money for you account .Minimum need to take {my.min_withdraw} taka"
        elif amount > my.max_withdraw:
            return f"Cross maximum limit : {my.max_withdraw}"
        elif amount > my.balance:
            return "No money "
        else:
            my.balance = my.balance -amount
            return f"Hey your withdrawal money : {amount}"
    def deposit(my, amount):
          my.balance = my.balance + amount

A = int(input("Enter balance:"))
my_bank = MYBank(A)

B = int(input("Enter withdraw:"))
reply = my_bank.withdraw(B)

print(reply)
print(my_bank.get_balance())

C = int(input("Enter Deposit:"))
print(my_bank.deposit(C))
print(my_bank.get_balance())