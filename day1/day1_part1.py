'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

puzzle = open("input_day1.txt","r")

puzzle_input = puzzle.readlines()
puzzle.close()


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