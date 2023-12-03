'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

'''

digits ={1:"one",
         2:"two",
         3:"three",
         4:"four",
         5:"five",
         6:"six",
         7:"seven",
         8:"eight",
         9:"nine"}




puzzle = open("input2_day1.txt","r")

puzzle_input = puzzle.readlines()
puzzle.close()


sum = 0
j = 0

for line in puzzle_input:
    j=j+1
    num1 = None
    num2 = None

    first_num_int = {
    "value": None,
    "index": None

    }

    first_num_word = {
    "value": None,
    "index": None

    }

    second_num_word = {
    "value": None,
    "index": None
    }

    second_num_int = {
    "value": None,
    "index": None

    }

    for i in digits:
        if (digits[i] in line):

            temp_index_left = line.find(digits[i])
            temp_index_right = line.rfind(digits[i])
            
            if ((first_num_word["index"] == None) or (first_num_word["index"] > temp_index_left)):
                first_num_word["value"] = i
                first_num_word["index"] = line.find(digits[i])
                num1 = i
            
            if ((second_num_word["index"] == None) or (second_num_word["index"] < temp_index_right) ):
                second_num_word["value"] = i
                second_num_word["index"] = line.rfind(digits[i])
                num2 = i

    for letter in range(len(line)):

        if(first_num_int["index"] == None):
            if(line[letter].isnumeric()):
                first_num_int["value"] = line[letter]
                first_num_int["index"] = line.find(line[letter])

                if ((first_num_word["index"] == None)) :
                    num1 = first_num_int["value"]

                elif (first_num_int["index"] < first_num_word["index"]):
                    num1 = first_num_int["value"]
                    


        if(second_num_int["index"] == None):
            if(line[-1-letter].isnumeric()):
                second_num_int["value"] = line[-1-letter]
                second_num_int["index"] = line.rfind(line[-1-letter])
                
                if (second_num_word["index"] == None):
                    num2 = second_num_int["value"]

                elif(second_num_int["index"] > second_num_word["index"]):
                    num2 = second_num_int["value"]

        
    if(num1!=None and num2!=None):
        print("{}:{}{}".format(j,num1,num2))
        sum = sum + (int("{}{}".format(num1,num2)))

    
print(sum)
