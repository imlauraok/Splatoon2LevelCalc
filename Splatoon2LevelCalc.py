from array import * # Import arrays, used to attach total XP to level

# Initialise lists and variables
LevelsList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # TODO remove list, work from TotalXPList
TotalXPList = [0, 0, 1000, 3800, 8400, 14900, 23400, 33900, 46500, 61300, 78300] # TODO finish adding levels
CurrentLevel = 1
CurrentLevelXP = 0
CurrentTotalXP = 0
TargetLevel = 10 # TODO allow user to choose target level

# Test pulling total XP for level from list
for x in range(len(LevelsList)):
    print("Total XP for level", LevelsList[x], "is", TotalXPList[x])

CurrentLevel = int(input("What is your current level? ")) # TODO check input is valid before continuing
CurrentLevelXP = int(input("How much XP do you have in the current level? ")) # TODO check input is valid before continuing
CurrentTotalXP = TotalXPList[CurrentLevel] + CurrentLevelXP

print("Total XP:", CurrentTotalXP)
print("XP to level", TargetLevel, "=", (TotalXPList[TargetLevel] - CurrentTotalXP))
