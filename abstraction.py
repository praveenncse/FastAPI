from abc import ABC, abstractmethod

'''class Server(ABC):
    @abstractmethod
    def start(self):
        pass    


class WebServer(Server):
    def start(self):
        print("Web Server is starting...")


class DatabaseServer(Server):
    def start(self):
        print("Database Server is starting...") 

web_server = WebServer()
db_server = DatabaseServer()    
web_server.start()
db_server.start()

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


shapes = [Circle(5), Rectangle(4,6)]
for s in shapes:
    print(s.area())


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending PUSH: {message}")


notifiers= [EmailNotification(), SMSNotification(), PushNotification()]
for n in notifiers:
    n.send("Server down!")'''



class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    

    def pay(self, amount):
        if amount<0:
            print("Invalid amount")
       
        else:   
            print(f"Paid {amount} using Credit Card")

class UPIPayment(Payment):
    

    def pay(self, amount):
        if amount<0:
            print("Invalid amount")
        else:   
            print(f"Paid {amount} using UPI")
    
    
class NetBankingPayment(Payment):
   

    def pay(self, amount):
        if amount<0:
            print("Invalid amount")
       
        else:   
            print(f"Paid {amount} using Net Banking")

class NetbankingPayment(Payment):
   
    def pay(self, amount):
        if amount<0:
            print("Invalid amount")
      
        else:   
            print(f"Paid {amount} using Net Banking")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for p in payments:
    p.pay(0)