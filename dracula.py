import re
#lab 43
#myfile=open("text.txt", "r") #opens file specified as read (read by default) 
#myfile.readlines() #
#myfile.close()

#yourfile=open("text.txt")
#for line in yourfile:
#    print(line, end='')
#yourfile.close()

with open("dracula.txt") as suck:
    term="vampire","Dracula"
    for line in suck:
        if term in line:
            print(term)
            #x=line#   print(line)
            #print(re.search("/Adracula",line))
            
            
