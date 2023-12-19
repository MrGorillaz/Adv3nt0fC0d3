import numpy as np
file = open("day11_input1.txt","r")

values = file.readlines()
file.close()

for line in range(len(values)):
    values[line] = values[line].strip()
    values[line] = list(values[line])





def expand_universe(universe):

    expand_line_pos = []
    expand_row_pos = []

    universe = np.array(universe)

    for line in range(len(universe)):
        if ("#" in universe[line]):
            pass
        else:
            expand_line_pos.append(line)
    
    #tranpose matrix of universe
    trans_universe = universe.transpose()


    for line in range(len(trans_universe)):

        if ("#") in trans_universe[line]:
            pass
        else:
            expand_row_pos.append(line)


    universe = np.insert(universe,expand_row_pos,".",axis=1)
    universe = np.insert(universe,expand_line_pos,".",axis=0)

    
    
    galaxy = 0

    #for line in universe:
    #    for i in range(len(line)):
    #        if (line[i] == "#"):
    #            galaxy = galaxy+1
    #            line[i] = galaxy
    

    return universe


def get_galaxy_positions(universe):

    galaxy_count = (universe != ".").sum()
    galaxies = np.where(universe == "#")
    galaxy_pos = []

    for galaxy in range(len(galaxies[0])):

        galaxy_pos.append([galaxies[0][galaxy],galaxies[1][galaxy]])
        
        if ([galaxies[1][galaxy],galaxies[0][galaxy]] in galaxy_pos):
            galaxy_pos.remove([galaxies[1][galaxy],galaxies[0][galaxy]])
        

    return galaxy_pos


def get_galaxy_positions_distances(galaxy_pos):

    distance_sum = 0
    galaxy_pairs = []

    

    for pos in galaxy_pos:


        for i in range(len(galaxy_pos)):

            galaxy_pair = [pos,galaxy_pos[i]]
            galaxy_pair.sort(key=lambda x: x[0])
            if galaxy_pair not in galaxy_pairs:
                if ((galaxy_pair[0][0] != galaxy_pair[1][0]) and (galaxy_pair[0][1] != galaxy_pair[1][1])):
                    galaxy_pairs.append(galaxy_pair)
                elif((galaxy_pair[0][0] != galaxy_pair[1][0]) and (galaxy_pair[0][1] == galaxy_pair[1][1])):
                    galaxy_pairs.append(galaxy_pair)
                elif((galaxy_pair[0][0] == galaxy_pair[1][0]) and (galaxy_pair[0][1] != galaxy_pair[1][1])):
                    galaxy_pairs.append(galaxy_pair)
                else:
                    print(galaxy_pair)
        
        for g in galaxy_pairs:

            if [g[1],g[0]] in galaxy_pairs:
                galaxy_pairs.remove([g[1],g[0]])

   

    for pos in galaxy_pairs:

        distance = abs(pos[0][0] - pos[1][0]) + abs(pos[0][1]-pos[1][1])
        #if distance == 5:
        #    print(pos)
        distance_sum = distance_sum + distance

    return distance_sum





universe = expand_universe(values)

galaxy_pos = get_galaxy_positions(universe)

all_galaxy_distances = get_galaxy_positions_distances(galaxy_pos)

print (all_galaxy_distances)




