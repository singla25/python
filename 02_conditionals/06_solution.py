distance = int(input("Enter distance in km (only number): "))

if distance < 0:
    print("Enter right distance")
    exit()

if distance > 15:
    modeOfTransport = "Car"
elif distance >= 3:
    modeOfTransport = "Bike"
else:
    modeOfTransport = "Walk"

print("You mode of transport is", modeOfTransport)