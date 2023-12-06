
file = open("day3_1_demo.txt","r")

engine = file.readlines()

file.close()

def get_symbols(engine):
    
    symbols = []
    for line in engine:
        for char in line:
            if(char.isnumeric() == False) and char != ".":
                symbols.append(char)
    
    symbols = set(symbols)
    return symbols


def find_adjacent(current_line,engine,start,end,number,symbols):

    #check_oben

    #number_pos_start = engine[current_line].find(number)
    number_pos_start = start


    pos_start = (number_pos_start - 1)
    if pos_start < 0:
           pos_start = 0
       
    pos_end = end+1
    if pos_end > len(engine[current_line])-1:
           pos_end = end

    if (current_line-1 >= 0):
        
        
        if pos_start >= 0:
            
            for i in range(pos_start,pos_end):
                
                if (engine[current_line-1][i] in symbols):
                    return True


    #check_mitte

    if (engine[current_line][pos_start] in symbols):
        return True
    elif(engine[current_line][pos_end-1] in symbols):
        return True

    #check_unten
    if (current_line+1 < len(engine)):

        #start here
        if pos_start >= 0:
            
            for i in range(pos_start,pos_end):
                
                if (engine[current_line+1][i] in symbols):
                    return True
        
    return False


#input bereinigen
for i in range(len(engine)):
    engine[i] = engine[i].strip()

symbols = get_symbols(engine)

sum = 0

for l in range(len(engine)):
    engine[l] = "."+engine[l]+"."


for l in range(len(engine)):
    
    line = engine[l]
    start_index = None
    end_index = None
    position = 0
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

            if (find_adjacent(l,engine,start_index,end_index,number,symbols)):
                #print("{}:{}".format(number,True))
                line2 = line2.replace(str(number),("."*len(number)))
                sum = sum + int(number)
                
            else:
                #print("{}:{}".format(number,False))
                pass
            
            

            number = ""
            end_index = None
            start_index = None
        

        position = position + 1
    print("{:03d} - {}".format(int(l+1),line2))

print(sum)

#537732