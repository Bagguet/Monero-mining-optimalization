import json

with open("info.json", "r") as f:
    info = json.load(f)

hoursInDay = info["hoursInDay"]
powerCostPerKwh = info["prices"]["kwh"]

worstCaseSolar = info["solar"]["minCase"]
avgCaseSolar = info["solar"]["avgCase"]
maxCaseSolar = info["solar"]["maxCase"]

wattage = info["wattsOnWall"]
kwhPerDay = hoursInDay*wattage
kwhPerDayOnlyCPU = hoursInDay*wattage


moneroPrice = info["prices"]["optimal"]["monero"]
ravenPrice = info["prices"]["optimal"]["raven"]
tariPrice = info["prices"]["optimal"]["tari"]

profitOnlyCPUMin = []
profitOnlyCPUAvg = []
profitOnlyCPUMax = []

profitMin = []
profitAvg = []
profitMax = []

for i in range(hoursInDay - worstCaseSolar+1):
    workingHours = i + worstCaseSolar
    
    paidHoursMin = workingHours-worstCaseSolar
    paidHoursAvg = workingHours-avgCaseSolar
    paidHoursMax = workingHours-maxCaseSolar
    

    #Calculating Working percentage
    machineWorkingPercentage = workingHours/hoursInDay
    paidHoursPercentageMin = paidHoursMin/hoursInDay
    paidHoursPercentageAvg = paidHoursAvg/hoursInDay
    paidHoursPercentageMax = paidHoursMax/hoursInDay

    #Price
    paidPerDayMin = kwhPerDay*paidHoursPercentageMin*powerCostPerKwh/1000
    paidPerDayAvg = kwhPerDay*paidHoursPercentageAvg*powerCostPerKwh/1000
    paidPerDayMax = kwhPerDay*paidHoursPercentageMax*powerCostPerKwh/1000

    paidPerDayOnlyCPUMin = kwhPerDayOnlyCPU*paidHoursPercentageMin*powerCostPerKwh/1000
    paidPerDayOnlyCPUAvg = kwhPerDayOnlyCPU*paidHoursPercentageAvg*powerCostPerKwh/1000
    paidPerDayOnlyCPUMax = kwhPerDayOnlyCPU*paidHoursPercentageMax*powerCostPerKwh/1000

    #Mined
    moneroMined = info["mined"]["monero"]
    ravenMined = info["mined"]["raven"]
    tariMined = info["mined"]["tari"]

    #Income
    totalIncome = machineWorkingPercentage*(moneroMined*moneroPrice + ravenMined*ravenPrice + tariMined*tariPrice)
    totalIncomeOnlyCPU = machineWorkingPercentage*(moneroMined*moneroPrice + tariMined*tariPrice) 
    #Profit
    if paidHoursMin >= 0:
        profitOnlyCPUMin.append((totalIncomeOnlyCPU - paidPerDayOnlyCPUMin, workingHours))
    if paidHoursAvg >= 0:
        profitOnlyCPUAvg.append((totalIncomeOnlyCPU - paidPerDayOnlyCPUAvg, workingHours))
    if paidHoursMax >= 0:
        profitOnlyCPUMax.append((totalIncomeOnlyCPU - paidPerDayOnlyCPUMax, workingHours))

    if paidHoursMin >= 0:
        profitMin.append((totalIncome - paidPerDayMin, workingHours))
    if paidHoursAvg >= 0:
        profitAvg.append((totalIncome - paidPerDayAvg, workingHours))
    if paidHoursMax >= 0:
        profitMax.append((totalIncome - paidPerDayMax, workingHours))


profitOnlyCPUMin.sort(reverse=True)
profitOnlyCPUAvg.sort(reverse=True)
profitOnlyCPUMax.sort(reverse=True)

profitMin.sort(reverse=True)
profitAvg.sort(reverse=True)
profitMax.sort(reverse=True)

print("Mining all")
print(f"Working hours: {profitMin[0][1]}, Profit: {profitMin[0][0]}\n")
print(f"Working hours: {profitAvg[0][1]}, Profit: {profitAvg[0][0]}\n")
print(f"Working hours: {profitMax[0][1]}, Profit: {profitMax[0][0]}\n")

print("CPU Only")
print(f"Working hours: {profitOnlyCPUMin[0][1]}, Profit: {profitOnlyCPUMin[0][0]}\n")
print(f"Working hours: {profitOnlyCPUAvg[0][1]}, Profit: {profitOnlyCPUAvg[0][0]}\n")
print(f"Working hours: {profitOnlyCPUMax[0][1]}, Profit: {profitOnlyCPUMax[0][0]}\n")




    
    
