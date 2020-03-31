new_file = open("45NewFile.txt","w")
new_file.write("This is new file")
new_file.close()

file = open("45NewFile.txt","r")
for filee in file.readlines():
    print(filee)
file.close()    