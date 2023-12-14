file = open("day6_input1.txt")
races = file.readlines()
file.close()

races_mul = 1

#clear Data
for line in range(len(races)):
    races[line] = races[line].strip()


race_times_total = (races[0].split(":")[1].strip().split(" "))
race_distances_total = (races[1].split(":")[1].strip().split(" "))

while(True):

    try:
        race_times_total.remove("")
    except:
        break

while(True):
    try:
        race_distances_total.remove("")
    except:
        break

for i in range(len(race_times_total)):

    possibility = 0

    for p in range(int(race_times_total[i])):
        time = p*(int(race_times_total[i])-p)
        if time > int(race_distances_total[i]):
            possibility = possibility + 1 

    races_mul = races_mul*possibility

print(races_mul)


