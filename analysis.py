with open("SAFI_results.csv") as file:
    file.readline().split(",")[18]
    for line in file:
        print(line.split(",")[18]) #index 18

