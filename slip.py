class Country:
        def AcceptCountry(self):
                self.cname=input("enter Country Name:")
        def DisplayCountry(self):
                print("Country Name is:",self.cname)    
class State(Country):
        def AcceptState(self):
                self.sname=input("Enter State Name:")
        def DisplayState(self):
                print("State Name is:",self.sname)
class Demo1(State):
        def AcceptDemo1(self):
                self.dname=input("Enter Demo1 Name:")
        def DisplayDemo1(self):
                print("Demo1 Name is:",self.dname)        
obj=Demo1()    
obj.AcceptCountry()    
obj.DisplayCountry()
obj.AcceptDemo1()
obj.AcceptState()
obj.DisplayState()
obj.DisplayDemo1()
