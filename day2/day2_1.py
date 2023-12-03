

file = open("day2_input1.txt","r")
games = file.readlines()
file.close()

cubes_max = {

    "red": 12,
    "green": 13,
    "blue": 14
}

game_sum = 0


for game in games:
    game = game.strip()
    game_id = int((game.split(":")[0]).split("Game ")[1])
    current_games =  (game.split(":")[1]).split(";")
    game_possible = True

    for current_game in current_games:
        
        if (game_possible == False):
            break

        part_game = current_game.split(",")

        for part in part_game:

            temp_key = part.strip().split(" ")[1]
            temp_value = int(part.strip().split(" ")[0])

            if (temp_value > cubes_max[temp_key]):
                print("Game {} is not possible".format(game_id))
                game_possible = False
                break

    
    if (game_possible):
        game_sum = game_sum + game_id

print(game_sum)