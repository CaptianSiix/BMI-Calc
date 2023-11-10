#User Input
def print_BMI():
    weight = input("Please tell me your weight in kilograms!")
    height = input("Please tell me your height in meters!")

##def

    fweight = float(weight)
    fheight = float(height)
##results

    BMI = (fweight/fheight**2)
    fBMI = float(BMI)
    if (BMI>0):
        if (BMI <= 16):
            print("you are severely underweight")
        elif (BMI <= 18.5):
            print("you are underweight")
        elif (BMI <= 25):
            print("you are Healthy")
        elif (BMI <= 30):
            print("you are overweight")
        else:
            print("you are severely overweight")

    print("Your BMI is", BMI)

print_BMI()
