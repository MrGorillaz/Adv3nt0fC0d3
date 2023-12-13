

file = open("day4_input2.txt","r")
card_pile = file.readlines()
file.close()

instances = {}
copies = {}

for l in range(len(card_pile)):
    card_pile[l] = card_pile[l].strip()
    instances[str( (card_pile[l].split(":")[0]))] = 1
    copies[str( (card_pile[l].split(":")[0]))] = 0

win_sum = 0
line = 0


for card in card_pile:

    temp_winning_numbers = (card.split(":")[1]).split("|")[0].strip().split(" ")
    temp_card_numbers = (card.split(":")[1]).split("|")[1].strip().split(" ")
    card_instance = card.split(":")[0]

    winning_numbers = []
    card_numbers = []
    n = 0
    line = line +1

    for win_num in temp_winning_numbers:

        if (win_num.isnumeric()):
            winning_numbers.append(int(win_num))
    
    for card_num in temp_card_numbers:

        if (card_num.isnumeric()):
            card_numbers.append(int(card_num))

    
    for card_num in card_numbers:
        if (card_num in winning_numbers):
            n = n+1
    
    start = card_pile.index(card)+1

    while (copies[card_instance]>=0):
        for i in range(start,start+n):
            card_instance_loop = card_pile[i].split(":")[0]
            instances[card_instance_loop] = instances[card_instance_loop]+1
            copies[card_instance_loop] = copies[card_instance_loop]+1
        copies[card_instance] = copies[card_instance] -1

    
for inst in instances:
    win_sum = win_sum + int(instances[inst])


print(win_sum)
pass