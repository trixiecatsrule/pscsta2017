# open the file
file = open("C:\\Users\\Hazel\\Downloads\\PSCSTA\\PSCSTACode\\Practice2014\\files\\sammysays.dat", "r")

# read in how many data sets you should expect
datasets = int(file.readline())

# loop that many times
for i in range(datasets):
    # do whatever for each data set
    x = file.readline().rstrip()
    sammy = x.split(' ')

    toprint = ""
    if ((sammy[0] == "Sammy") & (sammy[1] == "says")):
        j = 2
        while (j < len(sammy)):
            toprint += sammy[j] + " "
            j += 1
        print (toprint)