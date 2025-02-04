weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in cm:"))
bmi=weight/(height*height)

if bmi<=18.5:
    weight="under weight"
elif bmi>=28.9:
    weight="over weight"
elif bmi==19-25:
    weight="normal weight"
print(f"your weight is {weight},{bmi} ")
