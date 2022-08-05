
# solution 1
def bmi(weight, height):
    bmi_ = weight/(height**2)
    if bmi_ <= 18.5:
        return "Underweight"
    elif bmi_ <= 25.0:
        return "Normal"
    elif bmi_ <= 30.0:
        return "Overweight"
    else:
        return "Obese"
                  
print(bmi(90, 1.80))


# solution 2
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

print(bmi(90, 1.80))