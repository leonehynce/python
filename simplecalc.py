# prompt the user for two numbers
# from ctypes import result

number1=float(input("Enter first number:"))
number2=float(input("Enter second number"))

#promp user to enter operator
operator=input("Enter an operator (+,-,*,/):")
# perform calculation based on operator
if operator=="+":
    result =(number1+number2)
elif operator=="-":
    result=(number2-number1)
elif operator=="*":
    result=(number1*number2)
elif operator=="/":
    result=(number1/number2)
    if number2!=0:
        result=number1/number2
    else:
        result="invalid operator"
print(f"The answer is {result}")



