class MyDate:
         def accept(self):
                    self.d=int(input("Enter Day:"))
                    self.m=int(input("Enter Month"))
                    self.y=int(input("Enter Year:"))
         def display(self):
                    try:
                        if self.d>31:
                                raise ValueError("Day value is greater than 31") 
                        if self.m>12:
                                raise ValueError("Month value is greater than 12") 
                        print("Date is:",self.d,"_",self.m,"_",self.y)
                    except ValueError as e:
                        print(e)    
obj=MyDate()
obj.accept()
obj.display()
                                    