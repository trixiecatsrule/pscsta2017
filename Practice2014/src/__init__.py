# open the file
file = open("C:\\Users\\Hazel\\Downloads\\PSCSTA\\PSCSTACode\\Practice2014\\files\\bopscotch.dat", "r")

# read in how many data sets you should expect
datasets = int(file.readline())

# loop that many times
for i in range(datasets):
    # do whatever for each data set
    x = file.readline().rstrip()
    print(x)

# When reading in data from the text file:
# to remove extra newline characters
# x = file.readline().rstrip()
# to convert to int
# x = int(file.readline())
