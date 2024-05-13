class TicketMachines:
    
    old_new_machines = [] # hold all machine ids, even from removed machines
    machines = []  # initialized a list to record machine ids, only holds ids of existing machines
    total_sales = 0 # a var to hold overall sales value 

    # we initialize the instance but this function also calls create id to get unique machine ids
    def __init__(self, price): 
        if price >= 0:
            self.price = price
        else:
            raise ValueError("Ticket price cannot be negative")
        self.balance = 0
        self.total = 0
        self.id = TicketMachines.create_id()
    
    # This function creates unique ids for each machine and appends them to both ids list
    # it returns the id
    def create_id(): 
        for i in range(1, 10):
            if i not in TicketMachines.machines:
                if i not in TicketMachines.old_new_machines:
                    id = i
                    break
        TicketMachines.machines.append(id)
        TicketMachines.old_new_machines.append(id)
        return id
    
    def getID(self): # we can use this to check for a machine's id
        if self.id in TicketMachines.machines:
            print(f"\nMachine id: {self.id}")
        else:
            print("\nMachine does not exist")
        return self.id
    
    @classmethod # a class method that adds a new machine by initializing an instance of the class
    def addMachine(cls, price):
        new = cls(price)
        print(f"\nNew device added. Machine_id: {new.id}")
        return new
    
    # removes a machine my remove it's id from the machines list, its id exists however in another list 
    # so that it's id is not reused, creating confusion.
    @classmethod      
    def removeMachine(cls, machine_ID):
        if machine_ID in cls.machines:
            cls.machines.remove(machine_ID)
            print(f"\nDevice removed. Machine_id: {machine_ID}")
        else:
            print("\nMachine does not exist")
    
    @classmethod # prints the total sales of all machines combined
    def totalSales(cls):
        print(f"\nTotal sales across all machines: {cls.total_sales}")
        return cls.total_sales
    
    # the following functions from previous exercise also check whether the machine exists or not
    def insertMoney(self, amount):
        if self.id in TicketMachines.machines:
            if amount >= 0:
                self.balance += amount
                print(f"\n{amount} recharged to balance\n")
            else:
                raise ValueError("Balance amount cannot be negative")
        else:
            print("\nMachine does not exist")
        return self.balance
        
    def getPrice(self):
        if self.id in TicketMachines.machines:
            print(f"\nTicket Price: {self.price}")
        else:
            print("\nMachine does not exist")
        return self.price
    
    def getBalance(self):
        if self.id in TicketMachines.machines:
            print(f"\nYour balance: {self.balance}")
        else:
            print("\nMachine does not exist")
        return self.balance
    
    # each ticket printed adds to the overall total sales too.
    def printTicket(self):
        if self.id in TicketMachines.machines:
            if self.balance >= self.price:
                self.balance -= self.price
                self.total += self.price
                TicketMachines.total_sales += self.price
                print(f"\nFlat-fare-ticket. Machine ID: {self.id}")
                print("--------------------------")
                print(f"Ticket Price: {self.price}")
                print(f"New balance: {self.balance}")
                print("--------------------------")
                print(f"Total Sales: {self.total}")
            else:
                print("\nNot enough balance. Please recharge")
        else:
            print("\nMachine does not exist")
    
    def machine_total(self):
        if self.id in TicketMachines.machines:
            print(f"\nMachine {self.id} total is: {self.total}")
        else:
            print("\nMachine does not exist")
        return self.total

# tests   
T = TicketMachines(20) # create instance1
T2 = TicketMachines(30) # create instance2
T.getID() # get instance1 ID
T2.getID() # get inctance2 ID
T.getPrice() # get instance1 price
T2.getPrice() # get instance2 price
T3 = TicketMachines.addMachine(40) # create a new instance using addMachine
T3.getID() # get new instance's ID
T3.getPrice() # get new instance's price
TicketMachines.removeMachine(1) # remove instance 1
T.getPrice() # get price of inctance 1, machine does not exist.
T.getID() # get ID of inctance 1, machine does not exist.
T4 = TicketMachines.addMachine(10) # create a new instance
T4.getID() # get new instance's ID
T4.getPrice() # get new instance's price
T2.getBalance() # get balance of instance 2
T3.getBalance() # get balance of instance 3
T4.getBalance() # get balance of instance 4
T2.insertMoney(10) # insert money in machine/instance 2
T3.insertMoney(30) # insert money in machine/instance 3
T4.insertMoney(50) # insert money in machine/instance 4
T3.printTicket() # try printing ticket, not enough money as ticket price is  40 and balance is 30
T4.printTicket() # try printing ticket, success as ticket price is  10 and balance is 50
T3.machine_total() # get machine total sales but T3 is zero
T4.machine_total() # get machine total sales of T4, 10
T2.insertMoney(60) # insert money in T2
T2.printTicket() #  try printing ticket, success as ticket price is  30 and balance is 60
T2.machine_total() # get machine total sales of T2, 30
TicketMachines.totalSales() # get total sales of all machines, 10 from T4 + 30 from T2 = 40
T.getPrice() # T does not exist as it was removed earlier.