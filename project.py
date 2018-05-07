import library

weight = int(input('Insert your weight (in kg): '))
height = float(input('Insert your height (in metres): '))
name = input('Insert your name: ')

bmi = library.BMI(weight, height)
library.decision(bmi, name)
