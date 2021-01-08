import csv
import time
start=time.time()
d=dict()
with open('french_dictionary.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        d[row[0]]=row[1]
l=[]
d1=dict()
with open('find_words.txt', 'r') as file:
    for i in file.readlines():
        i=i.replace('\n','')
        #print(i)
        l.append(i)
s=""
l1=[]
with open('t8.shakespeare.txt', 'r') as file:
    for line in file:
        for word in line.split():
            l1.append(word)
s=" ".join(l1)
with open("unique time repce.csv",'w',newline='') as csvfile:
    for i in l:
        if s.count(i)>0:
            d1[i]=s.count(i)
            writer=csv.writer(csvfile)
            writer.writerow([i])
        s=s.replace(i,d[i])
with open("replaced.text",'w') as file:
    file.write(s)
with open("frequency of each word replaced.csv",'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    for i in d1.keys():
        writer.writerow([i,d1[i]])
end=time.time()
print("Time taken to process : ",end-start)
