score = int(input("Enter your test score: "))
if score > 90 and score < 100:
    print("Congratulations! You will be fully funded for your studies.")
elif score > 70 and score < 80:
    print("Congratulations! You will be financed with 1500 GEL.")
elif score > 40 and score < 70:
    print("Congratulations! You will be financed with 500 GEL.")
elif score < 40:
    print("Sorry, your study process will not be financed.")