# object oriented programming
class cars:
    #constructor method
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
         #a method function def describe_cars(self):
    def describe_car(self):
        print(f"My dream car make : {self.make}, "
                  f"My dream car model:{self.model} ," 
                  f"manufacturer: {self.year}" )
#create object or instances of a class
my_obj=cars("toyota","Lexus","2024")
my_obj.describe_car()
my_obj2=cars("BMW","GT","2024")
my_obj.describe_car()
my_obj3=cars("Mustang","Camrol","2012")
my_obj.describe_car()
my_obj4=cars("lamborgini","2018","spider")




