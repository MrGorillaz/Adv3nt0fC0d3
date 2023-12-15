
file = open("day8_2.txt","r")

road = file.readlines()
file.close()

for line in range(len(road)):
    road[line] = road[line].strip()

paths = {}
#next = "AAA"
end = "Z"
step_counter = 0

def get_steps(stepline):
    
    steps = []
    for step in stepline:
        steps.append(step)
    
    return steps


def build_paths(road):
    for i in range(2,len(road)):
        dest = road[i].split("=")[0].strip()
        left = (road[i].split("=")[1].strip()).split(",")[0].replace("(","")
        right = (road[i].split("=")[1].strip()).split(",")[1].replace(")","").strip()

        paths[dest]={"L":left,"R":right}
    return paths


def is_finished(all_paths):

    for path in all_paths.keys():
        if(all_paths[path]["finished"] == False):
            return False
    
    return True


steps = get_steps(road[0])
paths = build_paths(road)

paths_start = {}
paths_next = {}
paths_next_counter = 0

for key in paths.keys():
    if key[2] == 'A':
        paths_next[paths_next_counter] = {"next":key,"finished":False}
        paths_next_counter = paths_next_counter + 1


all_step_counter = 0

#this takes forever! :(
while (is_finished(paths_next)==False):
    #loop_counter = loop_counter +1
    #print(loop_counter)
    for step in steps:
        #all_step_counter = all_step_counter +1
        for path in paths_next.keys():
            #paths_next[path]["next"] = paths[paths_next[path]["next"]][step]

            if (paths_next[path]["next"][2] == end):
                paths_next[path]["finished"] = True
                
            else:
                paths_next[path]["finished"] = False
            paths_next[path]["next"] = paths[paths_next[path]["next"]][step]
           

        if (is_finished(paths_next)):
            print(all_step_counter)
            exit()
        all_step_counter = all_step_counter +1 
        #print(all_step_counter)

