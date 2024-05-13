class TicketMachine:
    def __init__(self, price):
        if price >= 0:
            self.price = price
        else:
            raise Exception("Ticket price cannot be negative")
        self.balance = 0
        self.total = 0
    
    def insertMoney(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n{amount} recharged to balance\n")
        else:
            raise Exception("Balance amount cannot be negative")
        return self.balance
        
    def getPrice(self):
        print(f"\nTicket Price: {self.price}")
        return self.price
    
    def getBalance(self):
        print(f"\nYour balance: {self.balance}")
        return self.balance
    
    def printTicket(self):
        if self.balance >= self.price:
            self.balance -= self.price
            self.total += self.price
            print("\nflat-fare-ticket")
            print("--------------------------")
            print(f"Ticket Price: {self.price}")
            print(f"New balance: {self.balance}")
            print("--------------------------")
            print(f"Total Sales: {self.total}")
        else:
            print("Not enough balance. Please recharge")
    
T = TicketMachine(20)
T.getPrice()
T.getBalance()
T.insertMoney(40)
T.getBalance()
T.printTicket()

