weather = input("Enter the weather: ").upper()

if weather == "SUNNY":
    activity = "Go for a walk"
elif weather == "RAINY":
    activity = "Read a Book"
elif weather == "SNOWY":
    activity = "Build a Snowman"
else:
    activity = "Bad Day - No Activity Take a Rest"

print(activity)
