'''class MobilePhone:
    def __init__(self):
        self.brand=None
        self.model=None
        self.price=None

    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")

class MobilePhoneBuilder:
    def __init__(self):
        self.phone = MobilePhone()

    def set_brand(self, brand):
        self.phone.brand = brand
        return self

    def set_model(self, model):
        self.phone.model = model
        return self

    def set_price(self, price):
        self.phone.price = price
        return self

m=MobilePhoneBuilder()
m.set_brand("Apple")
m.set_model("iPhone 14 Pro")
m.set_price(999)
m.phone.show_details()'''



##################################################

class Computer:
    def __init__(self):
        self.CPU=None
        self.RAM=None
        self.Storage=None
        self.GPU=None
        self.OperatingSystem=None

    
    def show_details(self):
        print(f"CPU : {self.CPU}")
        print(f"RAM : {self.RAM}")
        print(f"Storage : {self.Storage}")
        print(f"GPU : {self.GPU}")
        print(f"Operating System : {self.OperatingSystem}")



class ComputerBuilder:
    def __init__(self):
        self.computer=Computer()


    def set_cpu(self,CPU):
        self.computer.CPU=CPU
        return self

    def set_ram(self,RAM):
        self.computer.RAM=RAM
        return self

    def set_storage(self,Storage):
        self.computer.Storage=Storage
        return self

    def set_gpu(self,GPU):
        self.computer.GPU=GPU
        return self

    def set_operating_system(self,OperatingSystem):
        self.computer.OperatingSystem=OperatingSystem
        return self
    
    def build(self):
        return self.computer
    
pc = (
    ComputerBuilder()
    .set_cpu("Intel i9")
    .set_ram("32GB")
    .set_storage("1TB SSD")
    .set_gpu("RTX 4090")
    .set_operating_system("Ubuntu")
)

pc.show_details()
