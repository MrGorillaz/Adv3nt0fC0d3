#unfinished


file = open("day7_demo1.txt")
card_game = file.readlines()
file.close()

strength = {

            "A" : 14,
            "K" : 13,
            "Q" : 12,
            "J" : 11,
            "T" : 10,
            "9" : 9,
            "8" : 8,
            "7" : 7,
            "6" : 6,
            "5" : 5,
            "4" : 4,
            "3" : 3,
            "2" : 2

}

hands = {}

for i in range(len(card_game)):
    card_game[i] = card_game[i].strip()

#put games in dict
for h in card_game:
    hand = (h.split(" "))[0]
    bid = (h.split(" "))[1]
    
    hands[hand] = {"bid":int(bid),"type":None}

    temp_hand = (list(hand))
    temp_hand.sort()






pass