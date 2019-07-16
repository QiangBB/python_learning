class Calculator:
    def __init__(self,name,price,height,width,weight):
        self.name=name
        self.price=price
    def add(self,x,y):
        print(self.name)
        print(x+y)
    def minus(self,x,y):
        print(x-y)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
        
