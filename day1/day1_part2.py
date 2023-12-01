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

for i in digits:
    if (digits[i] in puzzle_input[0]):
        print("hey")
    pass

sum = 0
i = 0

for line in puzzle_input:
    i=i+1
    num1 = None
    num2 = None

    for letter in range(len(line)):

        if(num1 == None):
            if(line[letter].isnumeric()):
                num1 = line[letter]

        if(num2 == None):
            if(line[-1-letter].isnumeric()):
                num2 = line[-1-letter]
        
        if(num1!=None and num2!=None):
            print("{}:{}{}".format(i,num1,num2))
            sum = sum + (int("{}{}".format(num1,num2)))
            break

print(sum)


sum = 0
i = 0