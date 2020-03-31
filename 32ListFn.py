courses = ["a","b","c"]
courses.append("D")
print(courses)

#=============================================

title = ["s","d","f"]
title.insert(2,"O")
print(title)

#=============================================

merging = ["s","d","f"]
merging.extend(title)
print(merging)

#=============================================

#merging.clear()
#print(merging)

#=============================================

courses.remove("a")
print(courses)

#=============================================
#exists

print(merging.index("d"))
print(merging.count("s"))

#=============================================
serial = ["a","v","u","b"]
serial.sort()
#serial.reverse()
print(serial)

series = [1,3,5,2,7,9,8]
series.sort()
series.reverse()
series2=series.copy()
print(series2)
print(series)

#=============================================