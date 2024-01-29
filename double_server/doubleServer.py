import os
import queue
import random
import csv
class task:
    totalWaitingTime,numOftasks=0,0

    def csv(self):
        data=[str(self.id),str(self.IAT),str(self.AT),str(self.ASTBegin),str(self.AST),str(self.ASTEnds),str(self.BSTBegin),str(self.BST),str(self.BSTEnds),str(self.WT),str(self.timespend),str(self.idle)]
        return data
    
    def __init__(self):
        id,IAT,AST,AT,WT,timespend,ASTBegin,ASTEnds,idle=0,0,0,0,0,0,0,0,0
        BST,BSTBegin,BSTEnds=0,0,0
        self.numOftasks+=1
    def IATgenerator(self,RN,m):
        r=RN[m]
        IAT=0
        if r>=0 and r<=24:
            IAT=1
            return IAT
        elif r>=25 and r<=64:
            IAT=2
            return IAT
        elif r>=65 and r<=84:
            IAT=3
            return IAT
        elif r>=85 and r<=99:
            IAT=4
            return IAT
class able:
    state=0
    AbleST=0
    currentST=0
    totalServicesTime=0
    def serviceTimeGeneretorAble(self,RM,m):
        r=RM[m]
        serviceTime=0
        if r>=0 and r<=29:
            serviceTime=2
            return serviceTime
        elif r>=30 and r<=57:
            serviceTime=3
            return serviceTime
        elif r>=58 and r<=82:
            serviceTime=4
            return serviceTime
        elif r>=83 and r<=99:
            serviceTime=5
            return serviceTime
class baker: 
    state=0
    BakerST=0
    currentST=0
    totalServicesTime=0   
    def serviceTimeGeneretorBaker(self,RN,m):
        r=RN[m]
        serviceTime=0
        if r>=0 and r<=34:
            serviceTime=2
            return serviceTime
        elif r>=35 and r<=59:
            serviceTime=3
            return serviceTime
        elif r>=60 and r<=79:
            serviceTime=4
            return serviceTime
        elif r>=80 and r<=99:
            serviceTime=5
            return serviceTime

Able=able()
Baker=baker()
taskQueue =queue.Queue()
taskInfo = []
nextAt,nextIAT,nextWT,totalWT,numOftasksWhoWaited,tempforidleBaker,tempforidleAble=0,0,0,0,0,0,0
simulationTime=int(input("Enter simulation time : "))
choice=int(input("Enter 1 to use same assignment's numbers or Enter 2 to use random numbers from the table\n"))
if choice ==1:
    RN=[94,32,73,96,70,89,82,32,25,67,35,48,61,63,42,99,
    48,98,26,66,88,85,31,58,90,6,55,39,98,15,57,2,70,48,15,
    63,73,85,65,61,74,40,75,16,98,18,72,52,59,71,85,16,98,34,21,96,90]
    m=0
elif choice ==2:
    RN=[94,73,70,82,25,35,61,42,48,26,88,31,90,55,95,58,70
    ,15,73,65,74,75,98,72,59,85,98,21,32,96,89
    ,32,67,48,63,99,98,66,85,58,6,39,15,2,48,63
    ,85,61,40,16,18,52,71,16,34,96,90,85,81,46,53,49,65,17,30,3,50,]
    m=random.randint(0,10)
id=1
for clock in range(0,simulationTime) or queue.size>0 :
    if clock==nextAt:
        newtask=task()
        newtask.id=id
        newtask.AT=nextAt
        newtask.IAT=nextIAT
        taskQueue.put(newtask)
        nextIAT =newtask.IATgenerator(RN,m)
        m+=1
        if nextAt+nextIAT<60:
            nextAt=nextIAT+nextAt
        id +=1
    if Baker.state ==0:
        if taskQueue.empty() == False :
            Baker.state =1
            removedOfQueue=taskQueue.get()
            removedOfQueue.BST=Baker.serviceTimeGeneretorBaker(RN,m)
            m+=1
            removedOfQueue.WT=clock-removedOfQueue.AT
            removedOfQueue.timespend=removedOfQueue.BST+removedOfQueue.WT
            removedOfQueue.BSTBegin=clock
            removedOfQueue.idle=removedOfQueue.BSTBegin-tempforidleBaker
            removedOfQueue.BSTEnds=clock+removedOfQueue.BST
            removedOfQueue.AST,removedOfQueue.ASTBegin,removedOfQueue.ASTEnds=" "," "," "
            tempforidleBaker=removedOfQueue.BSTEnds
            Baker.currentST=removedOfQueue.BST
            Baker.totalServicesTime=Baker.totalServicesTime+removedOfQueue.BST
            taskInfo.append(removedOfQueue)
    else:
        Baker.currentST -= 1
        if Baker.currentST==1:
            Baker.state=0    
    if Able.state ==0:
        if taskQueue.empty() == False :
            Able.state =1
            removedOfQueue=taskQueue.get()
            removedOfQueue.AST=Able.serviceTimeGeneretorAble(RN,m)
            m+=1
            removedOfQueue.WT=clock-removedOfQueue.AT
            removedOfQueue.timespend=removedOfQueue.AST+removedOfQueue.WT
            removedOfQueue.ASTBegin=clock
            removedOfQueue.idle=removedOfQueue.ASTBegin-tempforidleAble
            removedOfQueue.ASTEnds=clock+removedOfQueue.AST
            removedOfQueue.BST,removedOfQueue.BSTBegin,removedOfQueue.BSTEnds=" "," "," "
            tempforidleAble=removedOfQueue.ASTEnds
            Able.currentST=removedOfQueue.AST
            Able.totalServicesTime=Able.totalServicesTime+removedOfQueue.AST
            taskInfo.append(removedOfQueue)
    else:
        Able.currentST -= 1
        if Able.currentST==1:
             Able.state=0    
csv_file=[]
path='simulation.csv'
if os.path.exists(path) and os.path.isfile(path):
    os.remove(path)
file= open(path,'w',newline='')
writer=csv.writer(file)
writer.writerow(['id','IAT','AT','A-ST begin','A-ST','A-ST ends','B-ST begin','B-ST','B-ST ends','WT','Time spend','idle time'])
for i in range(0,len(taskInfo)):
    writer.writerow(taskInfo[i].csv())
    if taskInfo[i].WT >0:
        numOftasksWhoWaited+=1
        totalWT=totalWT+taskInfo[i].WT
file.close()
print("able busy time percentage to total time",(Able.totalServicesTime/nextAt)*100)
print("Average waiting Time =",numOftasksWhoWaited/totalWT)