# Body Mass Index calculator
height=float(input("Enter your height in Meter: "))
weight=float(input("Enter your weight in KG: "))
BMI = weight/(height**2)

print(f" Your BMI is: {BMI:.2f}")

if BMI >= 30:
    print("Obesity")
elif BMI >= 25:
    print("Overweight")
elif BMI > 18.5:
    print("Normal")
else:
    print("Underweight")
