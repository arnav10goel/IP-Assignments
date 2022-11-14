c = float(input("Initial Cost: "))
dep_rate = (float(input("Depreciaton Rate:(%) ")))/100

def best_time(c, dep_rate):
    value_utility = 50
    maintenance = 0
    depreciation = dep_rate*c
    time = 1
    cost = c
    while time <= 15:
        value_utility = value_utility*1.1
        value = 6000*(value_utility)
        if time <= 5:
            #Only for the first 5 years
            maintenance += 0.01*c
            cost -= (maintenance + depreciation)
            if cost < value:
                return time
        else:
            #Different maintenance rate in play after 5 years
            maintenance += 0.5*maintenance
            cost -= (maintenance + depreciation)
            if cost < value:
                return time
        time += 1
    return 15   

print("Sell it in", best_time(c, dep_rate), "years.")