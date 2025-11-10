logsDict = {}
nTotal = 0

with open("mini_log.txt") as f:
    for line in f:
        origLine = line.split(": ", 1)
        keyLine = origLine[0]
        logsDict[keyLine] = logsDict.get(keyLine, 0) + 1
        nTotal += 1

if nTotal == 0:
    print("No log entries found.")
    exit()

sortedLogs = sorted(logsDict.items(), key=lambda item: item[1], reverse=True)
nTop = 3
for log, count in sortedLogs:
    pCount = float(count/nTotal * 100)
    print(f"{log}: {count} {pCount:.2f}%")
    nTop -= 1
    if (nTop == 0):
        break