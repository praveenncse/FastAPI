class AWSVM:
    def create(self):
        print("AWS VM Created")

class AWSStorage:
    def create(self):
        print("AWS Storage Created")


class AzureVM:
    def create(self):
        print("Azure VM Created")

class AzureStorage:
    def create(self):
        print("Azure Storage Created")

class abstractFactory:

    def AWSFactory(self,cloud_provider):
        if cloud_provider=="AWS":
            return AWSVM(),AWSStorage()
    
    def AzureFactory(self,cloud_provider):
        if cloud_provider=="Azure":
            return AzureVM(),AzureStorage()
    
cloud_provider=input("Enter cloud provider (AWS/Azure): ")
if cloud_provider=="AWS":
    vm,storage=abstractFactory().AWSFactory(cloud_provider)
    vm.create()
    storage.create()
elif cloud_provider=="Azure":
    vm,storage=abstractFactory().AzureFactory(cloud_provider)
    vm.create()
    storage.create()
else:
    print("Invalid cloud provider")


