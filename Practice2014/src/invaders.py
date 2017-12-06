# open the file
file = open("C:\\Users\\Hazel\\Downloads\\PSCSTA\\PSCSTACode\\Practice2014\\files\\invaders.dat", "r")

# read in how many data sets you should expect
datasets = int(file.readline())

# loop that many times
for i in range(datasets):
    # do whatever for each data set
    x = file.readline().rstrip()
    arr = x.split(' ')

    day = 0
    rateincrease = 1000
    cities =
    total = 0
    for j in arr:
        num = float(j)
        total += num
    if total >= 2 :
        print("Player 1")
    else :
        print("Player 2")