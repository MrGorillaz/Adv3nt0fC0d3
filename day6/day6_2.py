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

race_times_total = "".join(race_times_total)
race_distances_total = "".join(race_distances_total)


possibility = 0
for p in range(int(race_times_total)):
    time = p*(int(race_times_total)-p)
    if time > int(race_distances_total):
        possibility = possibility + 1 
races_mul = races_mul*possibility

print(races_mul)


