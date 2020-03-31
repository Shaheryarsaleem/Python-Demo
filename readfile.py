# absolute path , relative path, simple path

#read from other file
##open("read.txt", "r")

#write
##open("read.txt", "w")

#append info at the end of file
##open("read.txt", "a")

#read & write
##open("read.txt", "r")


courses_file = open("42read.txt", "r")
if courses_file.readable():
    print(courses_file.read())
    ##print(courses_file.readline())
    ##print(courses_file.readline())
    ###print(courses_file.readlines())
else:
    print("Not not allowed to open")

courses_file.close()   


#=====================


courses_file = open("42read.txt", "w")
if courses_file.readable():
    for content in courses_file.readlines():
        print(content)
else:
    print("Not not allowed to open")

courses_file.close()   