class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


pele = User("pele")
alexis = User("alexis")
gerson = User("gerson")

pele.make_deposit(100)
pele.make_deposit(200)
pele.make_deposit(50)
pele.make_withdrawl(45)
pele.display_user_balance()

alexis.make_deposit(1000)
alexis.make_deposit(1000)
alexis.make_withdrawl(500)
alexis.make_withdrawl(300)
alexis.display_user_balance()

gerson.make_deposit(1500)
gerson.make_withdrawl(1000)
gerson.make_withdrawl(5000)
gerson.make_withdrawl(3000)
gerson.display_user_balance()


gerson.transfer_money(400, pele)