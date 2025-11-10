# Initialize counts
nInfo = 0
nWarn = 0
nError = 0

# Open file then check if string exists then add in counts
with open("mini_log.txt") as f:
    for line in f:
        if "INFO: " in line:
            nInfo += 1
        elif "WARNING: " in line:
            nWarn += 1
        elif "ERROR: " in line:
            nError += 1

nTotal = nInfo + nWarn + nError

# Catch if logs were not found or no problems in file
if nTotal == 0:
    print("No log entries found.")
    exit()

# Convert to percentages
pInfo = float(nInfo / nTotal * 100)
pWarn = float(nWarn / nTotal * 100)
pError = float(nError / nTotal * 100)

# Log outputs
print("Log Summary:")
print("-------------")
print(f"Errors: {nError} {pError:.2f}%")
print(f"Warnings: {nWarn} {pWarn:.2f}%")
print(f"Info: {nInfo} {pInfo:.2f}%")