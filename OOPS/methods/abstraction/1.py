from abc import abstractmethod,ABC
class ATM(ABC):
    @abstractmethod
    def check_bal():
        pass
    @abstractmethod
    def deposite():
        pass
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def customer_info():
        pass
class NewAtm(ATM): #Override
    def __init__(self,name,addr,bal):
        self.name = name
        self.addr = addr
        self.bal = bal

    def customer_info(self):
        print(f'Name: {self.name},Address:{self.addr},Balance{self.bal}')
    def check_bal(self):
        print(f"Your Balance is :{self.bal}")
    def deposite(self):
        bal = int(input("Enter the deposite Amount: "))
        self.bal+=bal
        print(f"Deposite Amount:{bal},current Balance:{self.bal}")


        

    