with open("SAFI_results.csv") as file:
    file.readline().split(",")[18]

    n_grass = 0 
    n_mabatipitched = 0
    n_mabatisloping = 0
    n_unknown = 0

    for line in file:
        roof_type = line.split(",")[18] #index 18, the 19th column is C01_respondent_roof_type
        if roof_type == "grass":
            n_grass = n_grass + 1
        elif roof_type == "mabatipitched":
            n_mabatipitched += 1
        elif roof_type == "mabatisloping":
            n_mabatisloping += 1
        else:
            n_unknown += 1

    print("There are " + str(n_grass) + " grass roofs")
    print("There are " + str(n_mabatipitched) + " mabatipitched roofs")
    print("There are " + str(n_mabatisloping) + " mabatisloping roofs")
    print("There are " + str(n_unknown) + " unknown roof types")
