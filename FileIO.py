# Part 1 – Write a program that reads the file abespeech.txt and:

with open ('abespeech.txt', 'r') as file:
    line_number = 1 #Prints out the line number, starting at 1

    for line in file:
        line= line.rstrip() #Strips the newline
        print(line_number)
        print(line[::-1]) #Prints each line backwards
        line_number += 1


#Part 2: Write a program that reads the file smedleybutler.txt and:
#Copy all the lines that contain a word > 9 characters to a file named bigwords.txt

import os
with open ('smedleybutler.txt', 'r') as file:
    def has_big_word(line):
        word = line.split()
        for word in line:
            if len(word) > 9: 
                return True
input_file = 'smedleybutler.txt'
output_file = 'bigwords.txt'

os.system('type bigwords.txt')