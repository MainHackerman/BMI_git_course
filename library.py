def BMI(weight, height):
    return weight / height**2

def msg(bmi, name):
    return name + "'s BMI is " + str(bmi) + ' which means'

def decision(bmi, name):
    if bmi < 18.5:
        print(msg(bmi, name) + ' underweight.')
    elif bmi < 25:
        print(msg(bmi, name) + ' ideal weight.')
    elif bmi < 30:
        print(msg(bmi, name) + ' light overweight.')
    elif bmi < 40:
        print(msg(bmi, name) + ' overweight.')
    else:
        print(msg(bmi, name) + ' heavy overweight.')
