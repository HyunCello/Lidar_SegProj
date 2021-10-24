import numpy

mylist = numpy.arange(0, 748.1, 0.1)
print(len(mylist))
f = open("times.txt",'w')
for num in mylist:
    num = numpy.round(num,1)
    data = format(num,'.6e')
    data = str(data)+"\n"
    # print(data)
    f.write(data)
f.close