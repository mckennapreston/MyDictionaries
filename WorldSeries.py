
infile = open("WorldSeriesWinners.txt", "r")
infile2 = open("WorldSeriesWinners.txt", "r")

output = int(input("Enter a year: "))

if output == 1904:
    print("World Series not played")
elif output == 1994:
    print("World Series not played")
else:
    winner = {}


for line in infile:
    line = line.rstrip('\n')
    if line in winner:
        winner[line] = winner[line] + 1
    else:
        winner[line] = 1
    winner[line]


year = {}

counter = 1902

for line in infile2:
    line = line.rstrip("\n")
    if counter == 1903:
        counter += 2
        year[counter] = line
    elif counter == 1993:
        counter += 1
        year[counter] = line
    else:
        counter += 1
        year[counter] = line
year[counter] = line


counter = output
result = year[counter]
wins = winner[result]

print("World Series Champion: ", result)
print("Number of Championships won: ", wins)
