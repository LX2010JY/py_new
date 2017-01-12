import csv
from urllib.request import urlopen
from io import StringIO
csvFile = open("../file/test.csv",'w+')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()


'''
    stringIO 数据读写 不一定是文件，也可以在内存中读写，stringIO 在内存中读写字符串
    csv只能处理文件，如果csv文件在远程，则使用urlopen读取内容到内存，由stringIO读写，可模拟文件open
'''
csvdata = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
csvfile = StringIO(csvdata)
csvReader = csv.reader(csvfile)

for row in csvReader:
    print("The album \""+row[0]+"\" was released in "+row[1])
