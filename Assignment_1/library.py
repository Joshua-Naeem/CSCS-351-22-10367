class Library:
    
    def __init__(self,listofbooks):
        self.listofbooks = listofbooks
        
    def get_available_books(self):
        return self.listofbooks
    
    def lendbook(self, requestedbook):
        if requestedbook in self.listofbooks:
            print("")
        else:
            print("Sorry the book you have requested is currently not in the library")
        return requestedbook
    
    def add_book(self,returnedbook):
        return returnedbook
    
    def new_book(self, new):
        return new
    
    def delete_book(self, delete):    
        return delete
    
                            