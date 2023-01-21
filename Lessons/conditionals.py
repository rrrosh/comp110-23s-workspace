"""If it's raining, tell me to pack umbrella"""

weather: str = input("What is the weather like?")

if (weather == "rain"):
    print("Pack an umbrella! ")
else:
    if (weather == "sunny"):
        print ("wear a hat")
print("dont pack an umbrella")