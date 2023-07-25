
# file = open('./Python-file/test.txt')
# print(file.readline())
# print(file.read())
# file.close()
## by the help of "with" we can open and close the file by one command

with open('./Python-file/test.txt') as file: # the file close by it self
    print(file.readline())
    print(file.read())   

## Capitilze the file

with open('./Python-file/test.txt') as file:
    for line in file:
        # print(line.upper()) # it has with spaces acros the each line
        # To remove read line character we can use this
        print(line.strip().upper())

# Read each line of the file and make sorted

file = open('./Python-file/test.txt')
lines= file.readlines()
file.close()
lines.sort() ## Sort the file lines
print(lines) # It has \n as the end of each line we can remove this by 