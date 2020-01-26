cold=1
allergies=1
flu=0
tb=-1
cancer=-1

print("Welcome!")
print("Time to find out what sickness you have based on symtoms!")
print("All you need to do is answer whether or not you have a symptom.")

yn = input("Do you have a cough?\n")
if yn == "yes":
    print("Don't worry, coughs are normal, and it's most likely that you just have a common cold. But make sure to cough into your arm so you don't spread it!")
    cold+=1
    flu+=1
    
    yn = input("Just to make sure, are you coughing up blood?\n")
    if yn == "yes":
        print("That could be worrying. There's still a chance that you just have a particularly bad cold, but you should definitely go to the doctor.")
        tb+=2
        cancer+=1
    else:
        print("That's good, so it's even more likely that you just have a common cold.")
        cold+=1
else:
    print("Coughing is a symptom of many sicknesses, so not having it is a good sign.")

yn = input("Do you have a fever?\n")
if yn == "yes":
    print("A fever means your body is fighting off your sickness! A fever doesn't necessarily mean a worse disease, it just means that your body is doing more work to fight it off.")
    cold+=1
    flu+=1
    tb+=1
    yn = input("Is your fever above 105 degrees Fahrenheit?\n")
    if yn == "yes":
        print("Go to the doctor immediately! This is considered a medical emergency, and could lead to brain damage or death!")
        exit()
    else:
        print("That's good. If your fever ever does get above 105 degrees Fahrenheit, go to the doctor immediately")
else:
    print("Not having a fever is not always an indication that you aren't sick. In fact, you won't get a fever often when you just have the common cold.")
    flu-=1
    allergies+=1

yn = input("Do you have a runny nose?\n")
if yn == "yes":
    print("As annoying as it is, a runny nose is more often than not just caused by allergies and nothing to worry about.")
    flu+=1
    cold+=1
    allergies+=1
else:
    print("You're lucky you don't have a runny nose, because it's really annoying.")
    allergies-=1
    nothing+=1

yn = input("Are you feeling unusually tired?\n")
if yn == "yes":
    print("Being tired is often a sign that you aren't sleeping enough or are stressed, but it can be a sign of certain sicknesses.")
    flu+=1
    cold+=1
else:
    print("If you're not tired, that's a good sign that you're healthy in general, not just that you don't have a sickness.")

yn = input("Are you having muscle pains?\n")
if yn == "yes":
    print("Have you been exercising a lot recently?\n")
    flu+=1
    if yn == "yes":
        print("Then muscle pains are probably just due to being sore. Keep going, exercise is good way to stay healthy.")
        nothing+=2
    if yn == "no":
        print("In that case, muscle pains could be a sign of the flu, which is only slightly worse than the common cold.")
        print("However, muscle pains can also just be a sign that you injured a muscle without realizing it.")
else:
    print("Not being in pain is good!")

yn = input("Do you have a lump on your body where there shouldn't be one?\n")
if yn == "yes":
    print("This is often a sign of cancer. The sooner you go to the doctor, the more likely they can get rid of it.")
    cancer+=3
else:
    print("Then there's a good chance you don't have cancer!")

yn = input("Have you had an unexplained weight loss recently?\n")
if yn == "yes":
    print("That's not good. You should go to the doctor to have that checked out, since it could be a sign of something bad.")
    cancer+=1
    tb+=1
else:
    print("That's good.")

yn = input("Do you have a sore throat?\n")
if yn == "yes":
    print("A sore throat generally is caused by either allergies or the common cold, so you're probably fine.")
    cold+=1
    flu+=1
    allergies+=1
else:
    print("A sore throat is a common sign of sickness, so there's a good chance you're not sick.")

yn = input("Do you have a rash or hives?\n")
if yn == "yes":
    print("Rashes are a common sign of allergies, but generally not many sicknesses.")
    allergies+=1
else:
    print("That's good.")

yn = input("Do you have a headache?\n")
if yn == "yes":
    print("Headaches are common, even when you're not sick, though they are more common when you have a cold.")
    cold+=1
    flu+=1
else:
    print("That's good.")

yn = input("Are you sneezing a lot?\n")
if yn == "yes":
    print("Sneezing is often caused by allergies, or even will just happen when not sick, though it can be a sign of a cold.")
    cold+=1
    allergies+=2

if cold>3 and cold>flu and cold>allergies and cold>tb and cold>cancer:
    print("It is most likely that you have a common cold. Don't worry, it will pass in a week or two, and won't cause many problems.")
elif allergies>3 and allergies>flu and allergies>tb and allergies>cancer:
    print("Your symptoms point to you most likely just having allergies. There's no way to stop them, but they're also no big deal.")
elif flu>3 and flu>tb and flu>cancer:
    print("Your symptoms match you having the flu. You should probably go to the doctor if things start getting bad, but otherwise you'll probably be fine.")
elif tb>3 and tb>cancer:
    print("I'm sorry to say this, but you're most likely have tuberculosis. Go to a doctor immediately.")
elif cancer>3:
    print("I'm sorry to say this, but you're most likely have cancer. Go to a doctor immediately.")
else:
    print("You seem perfectly healthy, with no sicknesses.")
