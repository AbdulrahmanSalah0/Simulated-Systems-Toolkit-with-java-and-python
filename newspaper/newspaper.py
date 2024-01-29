import os
import csv
import random
RN=[94,73,70,82,25,35,61,42,48,26,88,31,90,55,95,58,70,15,73,65,74,
           75,98,72,59,85,98,21,32,96,89,32,67,48,63,99,98,66,85,58,6,39,
           15,2,48,63,85,61,40,16,18,52,71,16,34,96,90,85,21,46,53,49,65,
           17,30,3,50,6,66,12,54,71,44,67,83,61,93,43,2,58,61,67,40,74,
           71,67,56,63,16,35,30,71,25,85,82,5,70,42,31,72]
def Type(RN):
    if RN>=1 and RN<=35:
        return 1
    if RN>=36 and RN<=80:
        return 2
    if RN>=81 or RN==0:
        return 3
def demand(RN,TypeOfNews):
    if TypeOfNews==1:
        if RN>=1 and RN<=3:
            return 40
        elif RN>=4 and RN<=8:
            return 50
        elif RN>=9 and RN<=23:
            return 60
        elif RN>=24 and RN<=43:
            return 70
        elif RN>=44 and RN<=78:
            return 80
        elif RN>=79 and RN<=93:
            return 90
        elif RN>=94 or RN==0:
            return 100
    elif TypeOfNews==2:
        if RN>=1 and RN<=10:
            return 40
        elif RN>=11 and RN<=28:
            return 50
        elif RN>=29 and RN<=68:
            return 60
        elif RN>=69 and RN<=88:
            return 70
        elif RN>=89 and RN<=96:
            return 80
        elif RN>=97 or RN==0:
            return 90
    elif TypeOfNews==3:
        if RN>=1 and RN<=44:
            return 40
        elif RN>=45 and RN<=66:
            return 50
        elif RN>=67 and RN<=82:
            return 60
        elif RN>=83 and RN<=94:
            return 70
        elif RN>=95 or RN==0:
            return 80
days=int(input('Enter simulaion time (in days) :'))
order=int(input('Enter  number of newspapers purchase order :'))
temp,totalprofit,dailyProfit,scrapRevenue=random.randint(0,10),0,0,0
data=[]
i=1
T=''
for i in range(days):
    RN_NT=RN[temp]
    NT=Type(RN_NT)
    if NT==1:
        T='good'
    elif NT==2:
        T='fair'
    elif NT==3:
        T='poor'
    temp+=1
    RN_D=RN[temp]
    temp+=1
    Demand=demand(RN_D,NT)
    costOfNews=order*.33
    if Demand<=order:
        RevenueFromSales=Demand*.5
        lostprofit=0
        scrapRevenue=(order-Demand)*.05
    elif Demand>order:
        RevenueFromSales=order*.5
        lostprofit="%.1f"%((Demand-order)*.17)
    dailyProfit="%0.1f"%(RevenueFromSales-costOfNews-lostprofit+scrapRevenue)
    totalprofit+=float(dailyProfit)
    data.append([str(i+1),str(RN_NT),T,str(RN_D),str(Demand),str(RevenueFromSales),str(costOfNews),str(lostprofit),str(scrapRevenue),str(dailyProfit)])
    scrapRevenue,lostprofit=0,0
csv_file=[]
path='News.csv'
if os.path.exists(path) and os.path.isfile(path):
    os.remove(path)
file= open(path,'w',newline='')
writer=csv.writer(file)
writer.writerow(['day','RN for NT','NewsType','RN Demand','Demand','Revenue from sales','cost of NPs','Lost profit','Scrap Revenue','Daily profit'])
for i in range(0,len(data)):
    writer.writerow(data[i])
file.close()
print('Total profit =',"%0.1f"%totalprofit)