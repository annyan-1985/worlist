import codecs
import datetime
import time
input = "c:/learn-chinese/worlist/generate/xiezi-2.txt"
output = "c:/learn-chinese/worlist/generate/fullxiezi.txt"



allchar=[]
with codecs.open(input, 'r', encoding='utf8') as f:
    line = f.readline()
    while line:
        allchar.append(line);
        line = f.readline()


with codecs.open(output, 'w', encoding='utf8') as f:
    f.write("");


with codecs.open(output, 'a', encoding='utf8') as f:
    for day in range(55,365):
        time=datetime.datetime.now() + datetime.timedelta(days=(day-65))
        f.write(time.strftime("%Y-%m-%d:"))
        f.write(allchar[day].rstrip())
        f.write(allchar[day-29].rstrip())
        f.write(allchar[day-14].rstrip())
        f.write(allchar[day-7].rstrip())
        f.write(allchar[day-3].rstrip())
        f.write(allchar[day-1]);
