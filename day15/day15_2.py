
file = open("day15_input1.txt","r")

words = file.readlines()
file.close()

for line in range(len(words)):
    words[line] = words[line].strip()

steps = words[0].split(',')

def get_hash (step):
    
        current_value = 0

        for i in range(len(step)):

            val = ord(step[i])
            current_value = current_value + val
            current_value = int((current_value * 17) % 256)
        
        return current_value 


all_sum = 0

boxes = []

#steps = ['HASH']

for i in range(256):
    boxes.append([])


focal_len = {}

for step in steps:
    
    if "=" in step:
        label, focal = step.split("=")

        focal = int(focal)
        box = get_hash(label)

        focal_len[label] = focal

        if label in boxes[box]:

            label_index = boxes[box].index(label)
            boxes[box][label_index] = label

        else:
            boxes[box].append(label)

    if "-" in step:
        label = step[:-1]
        box = get_hash(label)
        if label in boxes[box]:
            boxes[box].remove(label)


for box_index, box in enumerate(boxes, start=1):
    for slot_index, label in enumerate(box, start=1):
        all_sum = all_sum + (box_index * slot_index * focal_len[label])

print(all_sum)