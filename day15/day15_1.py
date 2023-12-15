
file = open("day15_input1.txt","r")

words = file.readlines()
file.close()

for line in range(len(words)):
    words[line] = words[line].strip()

steps = words[0].split(',')

all_sum = 0

#steps = ['HASH']

for step in steps:
    
    current_value = 0
    
    for i in range(len(step)):

        val = ord(step[i])
        current_value = current_value + val
        current_value = int((current_value * 17) % 256)
    all_sum = all_sum + current_value

print(all_sum)