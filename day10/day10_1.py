file = open("day10_input1.txt","r")

values = file.readlines()
file.close()

for line in range(len(values)):
    values[line] = values[line].strip()
    values[line] = list(values[line])
    values[line].insert(0,".")
    values[line].append(".")


#extend for easier algorithm
values.append(list("."*len(values[0])))
values.insert(0,list("."*len(values[0])))


#directions


go_north = ["|","F","7"]
go_south = ["|","L","J"]
go_west = ["-","L","F"]
go_east = ["-","J","7"]
no_way = "."

def find_start(maps):

    line = 0
    row = 0
    pos = (row,line)


    for l in maps:

        if ("S" in l):
            row = l.index("S")
            pos = (line,row)
            return pos
        
        line = line + 1

    return pos

start_pos = find_start(values)
old_pos = (0,0)
came_from = None
route = []
route.append(start_pos)

finished = True
position = "S"

print("Start",start_pos,position)

while(True):

    #Try go North
    if ((values[start_pos[0]-1][start_pos[1]] in go_north) and ((start_pos[0]-1,start_pos[1]) != old_pos)):
        position = values[start_pos[0]-1][start_pos[1]]
        old_pos = start_pos
        start_pos = (start_pos[0]-1,start_pos[1])
        route.append(start_pos)
        came_from = "south"
        print("Go North",start_pos,position)
        pass

    #Try go East
    elif((values[start_pos[0]][start_pos[1]+1] in go_east) and ((start_pos[0],start_pos[1]+1) != old_pos)):
        position = values[start_pos[0]][start_pos[1]+1]
        old_pos = start_pos
        start_pos = (start_pos[0],start_pos[1]+1)
        route.append(start_pos)
        came_from = "west"
        print("Go East",start_pos,position)
        pass


    #Try go South
    elif((values[start_pos[0]+1][start_pos[1]]in go_south) and ((start_pos[0]+1,start_pos[1]) != old_pos) ):
        
        position = values[start_pos[0]+1][start_pos[1]]
        old_pos = start_pos
        start_pos = (start_pos[0]+1,start_pos[1])
        route.append(start_pos)
        came_from = "north"
        print("Go South",start_pos,position)
        

    #Try go West
    elif((values[start_pos[0]][start_pos[1]-1] in go_west) and ((start_pos[0],start_pos[1]-1) != old_pos)):
        position = values[start_pos[0]][start_pos[1]-1]
        old_pos = start_pos
        start_pos = (start_pos[0],start_pos[1]-1)
        route.append(start_pos)
        came_from = "east"
        print("Go West",start_pos,position)

    else:
        
        pass
        temp_pos = find_start(values)
        if (((start_pos[0]-temp_pos[0])>1) or ((start_pos[1]-temp_pos[1])> 1) ):
            start_pos = (temp_pos[0],temp_pos[1]+1)
            route = []
        else:
            break


print(len(route)/2)





