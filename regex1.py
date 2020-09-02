''' Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833) '''


import re
fh=open('actual.txt')
lst=[]
for lines in fh:
  lines=lines.rstrip()
  x= re.findall('[0-9]+',lines)
  if len(x)<1 : continue
  for i in range(len(x)):
    lst.append(x[i])

#print(lst)

sum=0
for j in lst:
  sum+=int(j)

print(sum)
