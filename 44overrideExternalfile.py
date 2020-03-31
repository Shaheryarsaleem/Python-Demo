read_file = open("42read.txt", "w")
read_file.write("Over ride file data")
read_file.close()

file = open("42read.txt", "r")

for filee in file.readlines():
    print(filee)

file.close()    