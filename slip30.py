class country:
        def AcceptCountry(self):
                self.cname=input("enter Country Name:")
        def DisplayCountry(self):
                print("Contry Name is:",self.cname)
class State(country):
        def AcceptState(self):
                self.sname=input("Enter State Name:")
        def DisplayState(self):
                print("State Name is:",self.sname)
class demo(State):
        def AcceptDemo(self): 
              self.dname=input("Enter Demo Name:") 
        def DisplayDemo(self):      
              print("Demo Name is:",self.dname)              
obj=demo()
obj.AcceptCountry()  
obj.AcceptState()
obj.AcceptDemo()  
obj.DisplayCountry()             
obj.DisplayState()  
obj.DisplayDemo()                    


