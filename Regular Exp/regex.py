import re
name=input('enter file:')
if len(name)<1:
    name='regex_sum_2084043.txt'
text=open(name)
sum=0
for line in text:
    line=line.rstrip()
    x=re.findall("[0-9]+",line)
    if len(x)>0:
        print(x)
    for num in x:
        sum=sum+int(num)
print(sum)