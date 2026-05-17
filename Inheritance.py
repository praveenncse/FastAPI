'''class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    ...

d= Dog()
d.sound()  


print("-----------------------------*-----------------------------")


class server:
    def start(self):
        print("Server is starting...")


class DatabaseServer(server):
    def backup(self):
        print("Database Server is backing up...")


db_server = DatabaseServer()
db_server.start()
db_server.backup()


print("-----------------------------*-----------------------------")


class Server:
    def start(self):
        print("Server is starting...")

class WebServer(Server):
    def start(self):
        super().start() 
        print("Web Server is starting with additional configurations...")


web_server = WebServer()
web_server.start()


print("-----------------------------*-----------------------------")



class Employee:
    def work(self):
        print("Employee working...")

class Manager(Employee):
    def manage(self):
        super().work()
        print("Managing team ...")

class Developer(Employee):
    def work(self):
        super().work()
        print("Writing code...")


manager = Manager()
manager.work()
manager.manage()

d= Developer()
d.work()
'''



class Node:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def start(self):
        print("Initializing worker services...")
    
    def stop(self):
        print("Stopping master services...")

class MasterNode(Node):
    def schedule_pod(self):
        print("Master Node is scheduling pods...")


class WorkerNode(Node):
    def run_pod(self):
        super().start()
        print("Worker Node is running pods...")



master_node = MasterNode("Master1", "Active")
master_node.schedule_pod()  

worker_node = WorkerNode("Worker1", "Active")
worker_node.run_pod()
