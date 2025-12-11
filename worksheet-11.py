class BankAccount :
    def __init__(self, name, balance) :
        self.name = name
        self.balance = balance

    def get_name(self) :
        print(self.name)
    def get_balance(self) :
        print(self.balance) 

# varaible = call your class with attributes
account = BankAccount("John",1000)
# new instance wii get created

#calling my order_id
account.get_deposit()
account.get_withdraw()

