marks = int(input("Provide me your Marks: "))

if marks > 100: 
    print("Enter your real marks to check your grade")
    exit()

if marks >= 90: 
    print("You scored A grade")
elif marks >= 80:
    print("You scored B grade")
elif marks >= 70:
    print("You scored C grade")
elif marks >= 60:
    print("You scored D grade")
else:
    print("You scored F grade")