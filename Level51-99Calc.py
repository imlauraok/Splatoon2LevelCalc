# Level 51-99 Total XP Calculator - Development tool for Splatoon2LevelCalc

PreviousLevel = 2641900 # XP for the previous level - initialised to 2,641,900 - the total XP for level 50
CurrentLevel = 0 # The XP for the current level being calculated
Levels = []

for x in range(51, 99):
    CurrentLevel = PreviousLevel + 100000
    print("Level", x, ":", CurrentLevel)
    Levels.append(CurrentLevel)
    PreviousLevel = CurrentLevel

print("")
print(Levels)
