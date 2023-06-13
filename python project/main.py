class Atm:
    def __int__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input=input('''
                      Hello , how would you like to proceed ?
                       1. Enter 1 to create pin
                       2. Enter 2 to deposit
                       3. Enter 3 to withdraw
                       4. Enter 4 to check babalnce
                       5. Enter 5 to exit
                       ''')
        if user_input == '1':
            print("create pin")
        elif user_input == '2':
            print("deposit")
        elif user_input == '3':
            print("withdraw")
        elif user_input == '4':
            print("check balance")
        else:
            print("bye")

sbi = Atm()
sbi.menu()
