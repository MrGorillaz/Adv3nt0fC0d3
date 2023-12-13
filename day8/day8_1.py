
file = open("day8_1.txt","r")

road = file.readlines()
file.close()

for line in range(len(road)):
    road[line] = road[line].strip()

paths = {}
next = "AAA"
end = "ZZZ"
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


steps = get_steps(road[0])
paths = build_paths(road)

while(next != end):


    for step in steps:
        next = paths[next][step]
        step_counter = step_counter +1
        if (next == end):
            break
        

print(step_counter)
