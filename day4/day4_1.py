

file = open("day4_input1.txt","r")
card_pile = file.readlines()
file.close()


for l in range(len(card_pile)):
    card_pile[l] = card_pile[l].strip()

win_sum = 0


for card in card_pile:

    temp_winning_numbers = (card.split(":")[1]).split("|")[0].strip().split(" ")
    temp_card_numbers = (card.split(":")[1]).split("|")[1].strip().split(" ")

    winning_numbers = []
    card_numbers = []
    n = -1

    for win_num in temp_winning_numbers:

        if (win_num.isnumeric()):
            winning_numbers.append(int(win_num))
    
    for card_num in temp_card_numbers:

        if (card_num.isnumeric()):
            card_numbers.append(int(card_num))

    
    for card_num in card_numbers:
        if (card_num in winning_numbers):
            n = n+1
    

    win_sum = win_sum + int(2**n)


print(win_sum)
pass