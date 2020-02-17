class library:
    def __init__(self,listofbooks):
        self.availablebooks = listofbooks
        
        
    def displayavailablebooks(self):
        print("the books we have in our library are as follows")
        print("-----------------------------------------------")
        for book in self.availablebooks:
            print(book)
            
    def borrowabook(self,requestedbook):
        if requestedbook in self.availablebooks:
            print("the book you have requested has now been borrowed")
        else:
            print("sorry the book you have requested is currently not in the library")
            
    def addbook(self,returnedbooks):
        self.availablebooks.append(returnedbook)
        print("thank you for returing your borrowed book")