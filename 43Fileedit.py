# how to edit file
append_file = open("42read.txt", "a")
append_file.write("\nAppending one")
append_file.write("\nAppending two")
append_file.write("\nAppending three")
append_file.close()

# how to read or show file
file = open("42read.txt", "r")

for fileee in file.readlines():
    print(fileee)
file.close()    