weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
print("BMI =", round(bmi, 2))
if bmi < 18.5:
    print("Underweight")
elif bmi>18.5 and bmi<=24.9:
    print("Healthy weight")
elif bmi <25 and bmi<=29.9 :
    print("Overweight")
else:
    print("Obese")
