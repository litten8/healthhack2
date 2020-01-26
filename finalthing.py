from healthhack import *
import os

cold=0
allergies=0
flu=0
tb=0
cancer=0

information("Welcome!")
information("Time to find out what sickness you have based on symtoms!")
information("All you need to do is answer whether or not you have a symptom.")

yn = question("Do you have a cough?\n")
if yn == "yes":
    information("Don't worry, coughs are normal, and it's most likely that you just have a common cold. But make sure to cough into your arm so you don't spread it!")
    cold+=1
    flu+=1
    
    yn = question("Just to make sure, are you coughing up blood?\n")
    if yn == "yes":
        information("That could be worrying.\n There's still a chance that you just have a\nparticularly bad cold, but you should definitely go to the doctor.")
        tb+=2
        cancer+=1
    else:
        information("That's good, so it's even more likely that you just have a common cold.")
        cold+=1
else:
    information("Coughing is a symptom of many sicknesses, so not having it is a good sign.")

yn = question("Do you have a fever?\n")
if yn == "yes":
    information("A fever means your body is fighting off your sickness! A fever doesn't\nnecessarily mean a worse disease, it just means that your body is doing more work to fight it off.")
    cold+=1
    flu+=1
    tb+=1
    yn = question("Is your fever above 105 degrees Fahrenheit?\n")
    if yn == "yes":
        information("Go to the doctor immediately! This is considered a medical emergency,\nand could lead to brain damage or death!")
        master.destroy()
    else:
        information("That's good. If your fever ever does get above 105 degrees Fahrenheit,\ngo to the doctor immediately")
else:
    information("Not having a fever is not always an indication that you aren't sick.\nIn fact, you won't get a fever often when you just have the common cold.")
    flu-=1
    allergies+=1

yn = question("Do you have a runny nose?\n")
if yn == "yes":
    information("As annoying as it is, a runny nose is more often than not just\ncaused by allergies and nothing to worry about.")
    flu+=1
    cold+=1
    allergies+=1
else:
    information("You're lucky you don't have a runny nose, because it's really annoying.")
    allergies-=1

yn = question("Are you feeling unusually tired?\n")
if yn == "yes":
    information("Being tired is often a sign that you aren't sleeping enough or are\nstressed, but it can be a sign of certain sicknesses.")
    flu+=1
    cold+=1
else:
    information("If you're not tired, that's a good sign that you're healthy in general,\nnot just that you don't have a sickness.")

yn = question("Are you having muscle pains?\n")
if yn == "yes":
    information("Have you been exercising a lot recently?\n")
    flu+=1
    if yn == "yes":
        information("Then muscle pains are probably just due to being sore.\nKeep going, exercise is good way to stay healthy.")
        nothing+=2
    if yn == "no":
        information("In that case, muscle pains could be a sign of the flu,\nwhich is only slightly worse than the common cold.\nHowever, muscle pains can also just be a sign that you injured a muscle without realizing it.")
else:
    information("Not being in pain is good!")

yn = question("Do you have a lump on your body where there shouldn't be one?\n")
if yn == "yes":
    information("This is often a sign of cancer.\nThe sooner you go to the doctor, the more likely they can get rid of it.")
    cancer+=3
else:
    information("Then there's a good chance you don't have cancer!")

yn = question("Have you had an unexplained weight loss recently?\n")
if yn == "yes":
    information("That's not good. You should go to the doctor to have that checked out,\nsince it could be a sign of something bad.")
    cancer+=1
    tb+=1
else:
    information("That's good.")

yn = question("Do you have a sore throat?\n")
if yn == "yes":
    information("A sore throat generally is caused by either allergies or the common cold,\nso you're probably fine.")
    cold+=1
    flu+=1
    allergies+=1
else:
    information("A sore throat is a common sign of sickness,\nso there's a good chance you're not sick.")

yn = question("Do you have a rash or hives?\n")
if yn == "yes":
    information("Rashes are a common sign of allergies, but generally not many sicknesses.")
    allergies+=1
else:
    information("That's good.")

yn = question("Do you have a headache?\n")
if yn == "yes":
    information("Headaches are common, even when you're not sick,\nthough they are more common when you have a cold.")
    cold+=1
    flu+=1
else:
    information("That's good.")

yn = question("Are you sneezing a lot?\n")
if yn == "yes":
    information("Sneezing is often caused by allergies, or even will just happen when not sick,\nthough it can be a sign of a cold.")
    cold+=1
    allergies+=2

if cold>3 and cold>flu and cold>allergies and cold>tb and cold>cancer:
    information("It is most likely that you have a common cold.\nDon't worry, it will pass in a week or two, and won't cause many problems.")
elif allergies>3 and allergies>flu and allergies>tb and allergies>cancer:
    information("Your symptoms point to you most likely just having allergies.\nThere's no way to stop them, but they're also no big deal.")
elif flu>3 and flu>tb and flu>cancer:
    information("Your symptoms match you having the flu.\nYou should probably go to the doctor if things start getting bad,\nbut otherwise you'll probably be fine.")
elif tb>3 and tb>cancer:
    information("I'm sorry to say this, but you're most likely have tuberculosis.\nGo to a doctor immediately.")
elif cancer>3:
    information("I'm sorry to say this, but you're most likely have cancer.\nGo to a doctor immediately.")
else:
    information("You seem perfectly healthy, with no sicknesses.")

master.destroy()
