
file = open("day9_input1.txt","r")

values = file.readlines()
file.close()

for line in range(len(values)):
    values[line] = values[line].strip()
    values[line] = values[line].split(" ")


def build_diffs (data,row):

    temp_dataset = {}
    temp_list = []
    temp = []

    for num in range(len(data)-1):
        diff = int(data[num+1]) - int(data[num])
        temp_list.append(diff)

    for elem in temp_list:
        if elem != 0:
            temp = build_diffs(temp_list,row+1)
            temp_dataset.update(temp)
            break
    temp_dataset.update({str(row):temp_list})
    return temp_dataset


data_counter = 0
all_sum =0

for dataset in values:
    temp_dataset = {}

    temp_dataset = build_diffs(dataset,data_counter)
    temp_dataset = dict(sorted(temp_dataset.items()))
    pred = 0
    for i in reversed(range(len(temp_dataset))):

        pred =pred + temp_dataset[str(i)][-1]
        pass
    
    pred = pred + int(dataset[-1])
    #print(pred)
    all_sum = all_sum + pred



    

print(all_sum)


