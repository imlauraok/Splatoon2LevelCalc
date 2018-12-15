# Initialise lists and variables
TotalXPList = [0, 0, 1000, 3800, 8400, 14900, 23400, 33900, 46500, 61300, 78300, 97600, 119200, 143300, 169900, 199000, 230800, 265400, 302800, 343100, 386400, 431400, 477900, 525900, 575400, 626400, 678900, 732900, 788400, 845400, 903900, 965900, 1031400, 1110400, 1172900, 1248900, 1327900, 1409900, 1494900, 1582900, 1672900, 1764900, 1858900, 1953900, 2049900, 2146900, 2244900, 2343400, 2442400, 2541900, 2641900, 2741900, 2841900, 2941900, 3041900, 3141900, 3241900, 3341900, 3441900, 3541900, 3641900, 3741900, 3841900, 3941900, 4041900, 4141900, 4241900, 4341900, 4441900, 4541900, 4641900, 4741900, 4841900, 4941900, 5041900, 5141900, 5241900, 5341900, 5441900, 5541900, 5641900, 5741900, 5841900, 5941900, 6041900, 6141900, 6241900, 6341900, 6441900, 6541900, 6641900, 6741900, 6841900, 6941900, 7041900, 7141900, 7241900, 7341900, 7441900, 7541900]
CurrentLevel = 1
CurrentLevelXP = 0
CurrentTotalXP = 0
TargetLevel = 99
XPToTarget = 0

# Test pulling total XP for level from list
#for x in range(len(TotalXPList)):
#    print("Total XP for level", x, "is", TotalXPList[x])

CurrentLevel = int(input("What is your current level? ")) # TODO check input is valid before continuing
CurrentLevelXP = int(input("How much XP do you have in the current level? ")) # TODO check input is valid before continuing
TargetLevel = int(input("What is your target level? ")) # TODO check input is valid before continuing
CurrentTotalXP = TotalXPList[CurrentLevel] + CurrentLevelXP

XPToTarget = (TotalXPList[TargetLevel] - CurrentTotalXP)

print("Total XP:", CurrentTotalXP)
print("XP to level", TargetLevel, "=", XPToTarget)
print(round(((CurrentTotalXP / TotalXPList[TargetLevel]) * 100), 2), "% of total XP earned")
print(round((XPToTarget / 1100), 2), "average Turf War games remaining,", round((XPToTarget / 1100 * 3), 2), "minutes of gameplay") # An average Turf War game is calculated as two games (one win one loss) with max turf inked, then divided by two
# TODO add Ranked Mode calculator
