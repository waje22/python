class MathOp:
         def AddOp(self):
                 self.a=int(input("Enter first no"))
                 self.b=int(input("Enter second no"))
                 self.c=self.a*self.b
                 print("Addition is:",self.c)
         def SubOp(self):
                 self.a=int(input("Enter first no"))
                 self.b=int(input("Enter second no"))
                 self.c=self.a*self.b
                 print("Substraction is:",self.c)  
         def MulOp(self):
                 self.a=int(input("Enter first no"))
                 self.b=int(input("Enter second no"))
                 self.c=self.a*self.b
                 print("Multiplication is:",self.c)              
obj=MathOp()
while True:  
        print("\n1.Addition")  
        print("\n2.Substraction")    
        print("\n3.Multiplication")
        print("4.Exit")
        ch=int(input("Enter choice to perform any operation"))
        if ch==1:
                obj.AddOP()       
        if ch==2:
                obj.SubOp()                   
        if ch==3:
                obj.MulOP()   
        if ch==4:
            print("\n Program stop")
            break
        else:
             print("Wrong Choice")                                        