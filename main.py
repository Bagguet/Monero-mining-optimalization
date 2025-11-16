import json

with open("info.json", "r") as f:
    info = json.load(f)
    

hoursInDay = info["hoursInDay"]
worstCaseSolar = info["worstCaseSolar"]
for i in range(hoursInDay - worstCaseSolar):
    workingHours = i + worstCaseSolar
    paidHours = hoursInDay-workingHours
    print(paidHours, hoursInDay, workingHours)
