import math

# open the file
file = open("C:\\Users\\Hazel\\Downloads\\PSCSTA\\PSCSTACode\\Practice2014\\files\\gorf.dat", "r")

# read in how many data sets you should expect
datasets = int(file.readline())

# loop that many times
for i in range(datasets):
    # do whatever for each data set
    x = file.readline().rstrip()
    #print(x)
    arr = x.split(' ')
    a = float(arr[0])
    b = float(arr[1])
    c = float(arr[2])
    start = (-b - math.sqrt(b**2 - 4*a*c)/(2*a))
    end = (-b + math.sqrt(b**2 - 4*a*c)/(2*a))
    print(format(start - end, '.1f'))

# When reading in data from the text file:
# to remove extra newline characters
# x = file.readline().rstrip()
# to convert to int
# x = int(file.readline())