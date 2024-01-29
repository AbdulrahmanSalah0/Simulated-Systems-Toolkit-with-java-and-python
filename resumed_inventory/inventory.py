import math
import os
import csv
import random
def RN_Demand(RN):
    if RN>0 and RN<=10:
        return 0
    elif RN>10 and RN<=35:
        return 1
    elif RN>35 and RN<=70:
        return 2
    elif RN>70 and RN<=91:
        return 3
    elif  RN==0 or (RN>91 and RN<=99):
        return 4
def RN_Lead(RN):
    if RN>0 and RN<=6:
        return 1
    elif RN>6 and RN<=9:
        return 2
    elif RN==0:
        return 3

RN_demand=[94,73,70,82,25,35,61,42,48,26,88,31,90,55,95,58,70,15,73,65,74,
           75,98,72,59,85,98,21,32,96,89,32,67,48,63,99,98,66,85,58,6,39,
           15,2,48,63,85,61,40,16,18,52,71,16,34,96,90,85,21,46,53,49,65,
           17,30,3,50,6,66,12,54,71,44,67,83,61,93,43,2,58,61,67,40,74,
           71,67,56,63,16,35,30,71,25,85,82,5,70,42,31,72]
RN_lead=[9,4,7,3,7,0,8,2,2,5,3,5,6,1,4,2,4,8,2,6,8,8,3,1,9,0,5,5,9,5,5,8,7,0,1,5,7,3,6,5,7,4,
           7,5,9,8,7,2,5,9,8,5,9,8,2,1,3,2,9,6,8,9,3,2,6,7,4,8,6,3,9,9,9,8,6,6,8,5,5,8,6,3,9]
cycles=int(input('Enter number of cycles:'))
cycle_days=int(input('Enter number of cycle days:'))
inv_begin=int(input('start quantity:'))
days=cycle_days*cycles
cycle,short,max_stock,order_reach,order,i,temp_for_print_order,lead_time,RN_leadtime=1,0,11,0,0,0,-1,-1,-1
RN_START=random.randint(0,10)
data=[]
for day in range(1,days+1):
    if lead_time>=0:
        lead_time-=1
    if day==order_reach+1:
        order=order-short
        inv_begin+=order
        short,order=0,0
        lead_time=-1
    demand=RN_Demand(RN_demand[day+RN_START])
    inv_end=inv_begin-demand
    if inv_end<0:
        short=math.fabs(inv_end)+short
        inv_end=0
    if day%cycle_days==0:
        order=max_stock-inv_end+short
        temp_for_print_order=order
        RN_leadtime=RN_lead[i+RN_START]
        lead_time=RN_Lead(RN_leadtime)
        order_reach=day+lead_time
        i+=1
    elif day%cycle_days==1 and day!=1:
        cycle+=1
    if temp_for_print_order==-1 and lead_time==-1:
        data.append([str(cycle),str(day),str(inv_begin),str(RN_demand[day-1]),str(demand),str(inv_end),str(short),' ',' ',' '])
    elif temp_for_print_order==-1 :
        data.append([str(cycle),str(day),str(inv_begin),str(RN_demand[day-1]),str(demand),str(inv_end),str(short),' ',' ',str(lead_time)])
    else:
        data.append([str(cycle),str(day),str(inv_begin),str(RN_demand[day-1]),str(demand),str(inv_end),str(short),str(temp_for_print_order),str(RN_leadtime),str(lead_time)])
    RN_leadtime,temp_for_print_order=-1,-1
    inv_begin=inv_end
csv_file=[]
path='inv.csv'
if os.path.exists(path) and os.path.isfile(path):
    os.remove(path)
file= open(path,'w',newline='')
writer=csv.writer(file)
writer.writerow(['Cycle','Days','Inv.B','RN D','Demand','Inv.E','short','Order','RN L','Lead Time'])
for i in range(0,len(data)):
    writer.writerow(data[i])
file.close()
    
    