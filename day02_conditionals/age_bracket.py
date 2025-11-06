
try:
    age = int(input("Enter your age: "))
    ageNote = ""

    if age >= 65:
        ageNote = "a Senior"
    elif age >= 20:
        ageNote = "an Adult"
    elif age >= 13:
        ageNote = "a Teen"
    elif age >= 0:
        ageNote = "a Child"
    else:
        ageNote = "a Fetus!"
    
    print(f" You are {ageNote}");
except ValueError:
    print("Use numbers please!")


    