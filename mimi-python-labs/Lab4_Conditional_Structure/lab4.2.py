print(">>> ======RESTART====")
print(">>>")
print("Fever symptoms advisor program")
temp = input("Check your body temperature: ")
temp = float(temp)
if temp >= 38.0:
    print("You have a fever.")
    treat = int(input(("Choose your treatment: 1=Medication, 2=Rest: ")))
    if treat == 1:
        print("Take fever-reducing medication.")
    elif treat == 2:
        print("Get plenty of rest.")
else:
    print("You are fine.")