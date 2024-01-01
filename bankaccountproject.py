class Bank:

    def __init__(self, initialamt=0):
        self.balance = initialamt

    def withdrawal(self):
        try:
            withdrawingmoney = float(input("Enter the amount to be withdrawn: "))
        except ValueError:
            withdrawingmoney = 0
        self.balance = self.balance - withdrawingmoney
        return withdrawingmoney

    def deposit(self):
        try:
            depositmoney = float(input("Enter amount to be deposited: "))
        except ValueError:
            depositmoney = 0
        self.balance = self.balance + depositmoney
        return depositmoney


try:
    initialamt = float(input("Enter initial bank savings: "))
    bank = Bank(initialamt)
    option="continue"
    while option=="continue":
        choice = input("Enter W/w for withdrawal or D/d for deposit: ").lower()
        
        if choice == 'w':
            withdrawn_amount = bank.withdrawal()
            with open('transaction.txt', 'a') as file:
                file.write(f"Previous total amount: {initialamt}\nAmount withdrawn: {withdrawn_amount}\nPresent total amount: {bank.balance}\n")
            initialamt=bank.balance
            with open('transaction.txt','r') as file:
                print(file.read())
            option=input("Enter 'continue' or 'cancel':").lower()

        elif choice == 'd':
            deposited_amount = bank.deposit()
            with open('transaction.txt', 'a') as file:
                file.write(f"Previous total amount: {initialamt}\nAmount deposited: {deposited_amount}\nPresent total amount: {bank.balance}\n")
            initialamt=bank.balance
            with open('transaction.txt','r') as file:
                print(file.read())
            option=input("Enter 'continue' or 'cancel':").lower()


        else:
            print("Invalid choice. Please enter W/w or D/d.")
            option=input("Enter 'continue' or 'cancel':").lower()
except ValueError:
    print("Sorry. Invalid input.")

finally:
    print("Thank you")
