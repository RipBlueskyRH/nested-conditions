#Write a program to check whether the student can take an exam or not.
#Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no).
#If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

a=str (input("do you have meducal cause?"))
b=str (input("are you here at least %75 of the time?"))

if a=="yes":
    print ("you can take the test")
else:
    print ("i will check your attendance")
    if b=="yes":
        print ("you can take the test")
    else:
        print ("you cannot take the test")