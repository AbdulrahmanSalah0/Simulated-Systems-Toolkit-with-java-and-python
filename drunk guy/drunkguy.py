import os
import csv
import random
random_numbers=[9,4,7,3,7,0,8,2,2,5,3,5,6,1,4,2,4,8,2,6,8,8,3,1,9,0,5,5,9,5,5,8,7,0,1,5,7,3,6,5,7,4,
           7,5,9,8,7,2,5,9,8,5,9,8,2,1,3,2,9,6,8,9,3,2,6,7,4,8,6,3,9,9,9,8,6,6,8,5,5,8,6,3,9,
           1,5,2,4,8,6,3,8,5,6,1]
def direction(RN):
    if RN>=1 and RN<=5:
        return 1
    if RN>5 and RN<=8:
        return -1
    if (RN>8 and RN<10)or RN==0:
        return 0
sim_no=int(input('Enter number of steps :'))
step=1
r=random.randint(0,10)
x,y=0,0
data=[]
Direction=''
for i in range(sim_no):
    Rn=random_numbers[i+r]
    dis=direction(Rn)
    if dis==1:
       Direction='F'
       y+=1
    elif dis==-1:
        Direction='L'
        x-=1
    elif dis==0:
        Direction='R'
        x+=1
    data.append([str(step),str(Rn),Direction,x,y])
    step+=1
csv_file=[]
path='drunkguy.csv'
if os.path.exists(path) and os.path.isfile(path):
    os.remove(path)
file= open(path,'w',newline='')
writer=csv.writer(file)
writer.writerow(['step','RN','direction','X coordinate','Y coordinate'])
for i in range(0,len(data)):
    writer.writerow(data[i])
file.close()
       