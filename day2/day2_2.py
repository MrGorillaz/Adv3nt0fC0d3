

file = open("day2_input2.txt","r")
games = file.readlines()
file.close()



game_sum = 0


for game in games:


    cubes_max = {

            "red": 1,
            "green": 1,
            "blue": 1
            }

    game = game.strip()
    game_id = int((game.split(":")[0]).split("Game ")[1])
    current_games =  (game.split(":")[1]).split(";")
    #game_possible = True

    for current_game in current_games:
        
       

        part_game = current_game.split(",")
        part_multi = 0

        for part in part_game:

            temp_key = part.strip().split(" ")[1]
            temp_value = int(part.strip().split(" ")[0])

            if (temp_value > cubes_max[temp_key]):
                cubes_max[temp_key] = temp_value
                
    part_multi = cubes_max["red"] * cubes_max["green"] * cubes_max["blue"]
    game_sum = game_sum + part_multi

print(game_sum)