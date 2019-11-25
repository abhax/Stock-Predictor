'''
Created on Nov 24, 2019

@author: abhax_000
'''
from DataGather.StockInfoGatherer import DataSponge 
if __name__ == '__main__':
    dataTest  = DataSponge()
    json = dataTest.Test('account')
    print(json.json())
    print("Please enter the data you want to read: \n")
    command = input("Command?:")    
    while ((command != "exit") and (command != "Exit")):
        json = dataTest.Test('accounts')
        print(json.json())
        print("Please enter the data you want to read: \n")
        command = input("Command?:")
    pass