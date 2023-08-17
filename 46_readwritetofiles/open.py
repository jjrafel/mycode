#lab 43
myfile=open("text.txt", "r") #opens file specified as read (read by default) 
myfile.readlines() #
myfile.close()

yourfile=open("text.txt")
for line in yourfile:
    print(line, end='')
yourfile.close()

with open("text.txt") as of: ###important method
        for line in hisfile:
            print("reads file lines and closes")
