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

came_from_got_to = {

    "south": {
        
        "|":"north",
        "F":"east",
        "7":"west"
    },
    "north": {
        "|":"south",
        "L":"east",
        "J":"west"
    },
    "east": {
        "-":"west",
        "L":"north",
        "F":"south"
    },
    "west": {
        "-":"east",
        "7":"south",
        "J":"north"
    }
}






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

start_go = ["west","east","south","north"]
go_to = start_go[0]
came_from = "west"
#start_go.remove(go_to)
position = "F"



print("Start",start_pos,position)
loop_count = 0

while(True):

    #Try go North
    if go_to == "north":
        position = values[start_pos[0]-1][start_pos[1]]
        if (position == "S"):
            break
        if (position in go_north ):
        #if ((values[start_pos[0]-1][start_pos[1]] in go_north) and ((start_pos[0]-1,start_pos[1]) != old_pos)):
            position = values[start_pos[0]-1][start_pos[1]]
            old_pos = start_pos
            start_pos = (start_pos[0]-1,start_pos[1])
            route.append(start_pos)
            came_from = "south"
            #came_from = came_from_got_to[came_from]
            go_to = came_from_got_to[came_from][position]
            print("Go North",start_pos,position)
            pass
            continue
        else:
            loop_count = loop_count +1
            go_to = start_go[loop_count%4]

    #Try go East
    elif go_to == "east":
        position = values[start_pos[0]][start_pos[1]+1]
        if (position == "S"):
            break
        if ((position in go_east) ):
    #elif((values[start_pos[0]][start_pos[1]+1] in go_east) and ((start_pos[0],start_pos[1]+1) != old_pos)):
            came_from = "west"
            position = values[start_pos[0]][start_pos[1]+1]
            go_to = came_from_got_to[came_from][position]
            
            old_pos = start_pos
            start_pos = (start_pos[0],start_pos[1]+1)
            route.append(start_pos)
            #came_from = "west"
           
            print("Go East",start_pos,position)
            pass
            continue
        else:
            loop_count = loop_count +1
            go_to = start_go[loop_count%4]
            


    #Try go South
    elif go_to == "south":
        position = values[start_pos[0]+1][start_pos[1]]
        if (position == "S"):
            break
    #elif((values[start_pos[0]+1][start_pos[1]]in go_south) and ((start_pos[0]+1,start_pos[1]) != old_pos) ):
        if ((position in go_south) ):
            position = values[start_pos[0]+1][start_pos[1]]
            old_pos = start_pos
            start_pos = (start_pos[0]+1,start_pos[1])
            route.append(start_pos)
            came_from = "north"
            #came_from = came_from_got_to[came_from]
            go_to = came_from_got_to[came_from][position]
            print("Go South",start_pos,position)
            continue
        else:
            loop_count = loop_count +1
            go_to = start_go[loop_count%4]
            
        

    #Try go West
    elif go_to == "west":
        position = values[start_pos[0]][start_pos[1]-1]
        if (position == "S"):
            break
    #elif((values[start_pos[0]][start_pos[1]-1] in go_west) and ((start_pos[0],start_pos[1]-1) != old_pos)):
        if ((position in go_west)):
            #came_from = came_from_got_to[came_from][position]
            position = values[start_pos[0]][start_pos[1]-1]
            old_pos = start_pos
            start_pos = (start_pos[0],start_pos[1]-1)
            route.append(start_pos)
            came_from = "east"
            #came_from = came_from_got_to[came_from]
            go_to = came_from_got_to[came_from][position]
            print("Go West",start_pos,position)
            continue
        else:
            loop_count = loop_count +1
            go_to = start_go[loop_count%4]
            

    else:
        
    #    pass
    #    temp_pos = find_start(values)
            loop_count = loop_count +1
            go_to = start_go[loop_count%4]
        #came_from = "west"
   #     start_go.remove(go_to)
        #if (((start_pos[0]-temp_pos[0])>1) or ((start_pos[1]-temp_pos[1])> 1) ):
        #    start_pos = (temp_pos[0],temp_pos[1]+1)
        #    route = []
        #else:
        #    break


print(len(route)/2)





