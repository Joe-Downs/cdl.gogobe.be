import csv
import os

badFiles = []

for result in os.listdir("results"):
    with open(f"results/{result}", newline='') as csvResult:
        cdlReader = csv.reader(csvResult)
        for row in cdlReader:
            print(",".join(row))
        print()
        response = "y"
        response = input("Does this look valid? [y/n/(p)rint] ")
        if response.lower() == "n":
            badFiles.append(result)
        if response.lower() == "p":
            badFiles.sort()
            print(badFiles)
        print()
    csvResult.close()

badFiles.sort()
print(badFiles)

