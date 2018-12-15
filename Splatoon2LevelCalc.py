from array import * # Import arrays, used to attach total XP to level

# Initialise lists and variables
TotalXPList = [0, 0, 1000, 3800, 8400, 14900, 23400, 33900, 46500, 61300, 78300, 97600, 119200, 143300, 169900, 199000, 230800, 265400, 302800, 343100, 386400, 431400, 477900, 525900, 575400, 626400, 678900, 732900, 788400, 845400, 903900, 965900, 1031400, 1110400, 1172900, 1248900, 1327900, 1409900, 1494900, 1582900, 1672900, 1764900, 1858900, 1953900, 2049900, 2146900, 2244900, 2343400, 2442400, 2541900, 2641900] # TODO finish adding levels
CurrentLevel = 1
CurrentLevelXP = 0
CurrentTotalXP = 0
TargetLevel = 50 # TODO allow user to choose target level

# Test pulling total XP for level from list
for x in range(len(TotalXPList)):
    print("Total XP for level", x, "is", TotalXPList[x])

CurrentLevel = int(input("What is your current level? ")) # TODO check input is valid before continuing
CurrentLevelXP = int(input("How much XP do you have in the current level? ")) # TODO check input is valid before continuing
CurrentTotalXP = TotalXPList[CurrentLevel] + CurrentLevelXP

print("Total XP:", CurrentTotalXP)
print("XP to level", TargetLevel, "=", (TotalXPList[TargetLevel] - CurrentTotalXP))
