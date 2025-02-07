# create a new class called friuts having attributes:Name,colur,price, impliment a constructor method and a method function that
# prints my favourite fruits """""""(the attributes)
#create file instances of the class
#the begining
class fruits:
#constructor method
 def __init__(self,Name,colour,price):
    self.Name=Name
    self.colour=colour
    self.price=price
 def describe_fruit(self):
     print(f"My favourite fruit is {self.Name} ,"
           f"The fruits colour is {self.colour} ,"
           f"The price of the fruit is {self.price}")
# instance
my_obj=fruits("Mangoe","yellow","0.9$")
my_obj.describe_fruit()
my_obj2=fruits("Banaa","Yellow","2$")
my_obj2.describe_fruit()
my_obj3=fruits("apples","red","1.5$")
my_obj3.describe_fruit()