'''class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

a=[Dog(),Cat()]
for animal in a:
    animal.sound()


print("-----------------------------*-----------------------------")

class Server:
    def start(self):
        print("Server is starting...")
    
class WebServer(Server):
    def start(self):
        print("Web Server is starting")


class DatabaseServer(Server):
    def start(self):
        super().start()
        print("Database Server is starting...")


s=[WebServer(),DatabaseServer()]
for server in s:
    server.start()'''



class MasterNode:
    def deploy(self):
        print("Deploying control plane...")

class WorkerNode:
    def deploy(self):
        print("Deploying application pods...")

def service_deployment(node):
    node.deploy()

service_deployment(MasterNode())
service_deployment(WorkerNode())
    
