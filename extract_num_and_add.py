# Desciption: This program reads through and parses a file with text and numbers
# All the numbers in the file are extracted to compute sum of the numbers.

import re 

#Parsing file and extracting numbers:
fid = "regex_sum_13134.txt"
contents = open(fid)

num_list = []

for line in contents:
    line = line.rstrip()
    extracted_num = re.findall('[0-9]+',line)
    num_list = num_list + extracted_num

#Converting numbers to int data type
num_list = list (map (int, num_list))

#Adding extracted numbers
i = 0
sum = 0
while (i<len(num_list)):
    sum = sum + num_list[i]
    i = i+1

print ("Number of Terms, ",i)
print ("Sum= ", sum)
