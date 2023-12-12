
file = open("day3_input2.txt","r")

engine = file.readlines()

file.close()



def find_numbers(l,engine):

    
    line = engine[l]
    start_index = None
    end_index = None
    position = 0
    numbers = []
    number = ""
    line2 = line
    for character in line:
        if (character.isnumeric() and start_index == None):
            start_index = position
        if (character.isnumeric() and end_index == None):
            end_index = position
        elif(character.isnumeric() and (position >= end_index)):
            end_index = position
        elif(start_index != None and end_index != None):
            end_index = end_index+1
            number = line[start_index:end_index]
            numbers.append([number,start_index,end_index])
            number = ""
            end_index = None
            start_index = None
        position = position + 1
    return numbers


def find_adjacent(current_line,engine,start):

    search_number_index = None
    line_before_num = find_numbers(current_line-1,engine)
    line_current_num = find_numbers(current_line,engine)
    line_below_num = find_numbers(current_line+1,engine)
    numbers = []
    #temp_numbers = []
    #Check oben
    for i in range(-1,2):
        if(engine[current_line-1][start+i].isnumeric()):
            for num in line_before_num:
                if ((start+i)>=num[1] and (start+i) <=num[2]):
                    numbers.append(int(num[0]))

    
    #check mitte
    for i in range(-1,2):
        if(engine[current_line][start+i].isnumeric()):
            for num in line_current_num:
                if ((start+i)>=num[1] and (start+i) <=num[2]):
                    numbers.append(int(num[0]))
    
    #check unten
    for i in range(-1,2):
        if(engine[current_line+1][start+i].isnumeric()):
            for num in line_below_num:
                if ((start+i)>=num[1] and (start+i) <=num[2]):
                    numbers.append(int(num[0]))


    return set(numbers)
        
        


    pass


#input bereinigen
for l in range(len(engine)):
    engine[l] = engine[l].strip()
    engine[l] = "."+engine[l]+"."

engine.append("."*len(engine[0]))
engine.insert(0,"."*len(engine[0]))



sum = 0


for l in range(len(engine)):
    
    line = engine[l]
    start_index = None
    end_index = None
    position = 0
    number = ""
    line2 = line
    for character in line:

        if character == '*':
            start_index = position

            numbers = find_adjacent(l,engine,start_index)
            
            if (len(numbers) == 2):
                sum = sum + (list(numbers)[0] * list(numbers)[1])
            else:
                print("error",numbers)

            
        
        

        position = position + 1
    print("{:03d} - {}".format(int(l+1),line2))

print(sum)

#537732