# BMI Calculator 1.0

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = (float(weight))/((float(height)**2))
print(round(bmi))