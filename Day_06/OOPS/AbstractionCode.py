'''class Bank:
    def __init__(self,name,accountNumber,role,balance):
        self.name=name #public 
        self.__account_number=accountNumber #private
        self._role=role #protected
        self.__pin=pin #private

    def __str__(self,naem ,accoutNumber):
        print("name is ",name " my account number is "accountNumber)
    def getpin(self):
        return self.__pin
    def setpin(self,__newpin):
        self.__pin=__newpin
        # return __newpin
        print("Modified pin",__newpin)

d=Bank('Ram',123,"manager",1234)
print(b.getpin()) '''

from abc import ABC 
