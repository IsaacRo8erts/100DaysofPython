# BMI Calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (float(weight))/((float(height)**2))
rounded_bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")




