class Account:

    def __init__(self, fName, lName, sBalance, cBalance):
        """
        Constructor for an Account object
        """
        self.fName = str(fName)
        self.lName = str(lName)
        self.sBalance = float(sBalance)
        self.cBalance = float(cBalance)
        self.total = sBalance + cBalance
        self.output = ""
    

    def __str__(self):
        """
        Prints out both savings and checking balances of the account
        """
        self.output = "The balance of " + self.fName + "'s account is as follows:\n"\
            + "Savings Account: " + "{:.2f}".format(self.sBalance)\
            + "\nChecking Account: " + "{:.2f}".format(self.cBalance)
        return self.output

def populateList():
    bankList = [Account("Drake", "Bell", 4.20, 69),\
        Account("Josh", "Peck", 66.6, 20.40),\
        Account("Jamie", "Fox", 44, 3456)]
    return bankList

def displayNames(bankList):
    print("We have accounts for the following individuals. Which account would you like to view? (Please input an integer)")
    y = 1
    for x in bankList:
        print(str(y) + ". " + x.fName + " " + x.lName)
        y += 1
    return y

def main():
    
    bankList = populateList()
    listSize = int(displayNames(bankList))
    promptInput = int(input("> "))
    if promptInput > 0 and promptInput < listSize:
        print(bankList[promptInput - 1])
    createAccount = str(input("Would you like to create a new account? (Y/N)"))
    if createAccount == "Y" or createAccount == "y" or createAccount == "Yes"\
         or createAccount == "YES" or createAccount == "yes":
        myAccount = Account(input("First Name: "), input("Last Name: "), input("Amount of money in your savings account: "), input("Amount of money in your checking account: "))
        print(myAccount)

if __name__ == "__main__":
    main()