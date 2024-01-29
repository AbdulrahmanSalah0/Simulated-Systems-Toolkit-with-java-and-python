import math
import pandas as pd
import scipy.stats
alpha=float(input('Enter the significance level to use :'))
data=pd.DataFrame({'period':[0,1,2,3,4,5,6,7,8,9,10,11],'frequency':[12,10,19,17,10,8,7,5,5,3,3,1]})
n=sum(data['frequency'])
print(data)
mean=sum(data['period']*data['frequency'])/100
Var=((sum((data['period']**2)*data['frequency']))-100*mean**2)/(n-1)
Ex=[0]*len(data)
chi=[0]*len(data)
for i in range(len(data)):
   Ex[i]=n*((math.exp(-mean)*mean**data['period'][i])/math.factorial(data['period'][i]))
data.insert(2,'E(x)',Ex)
for i in range(len(data)):
   chi[i]=((data['frequency'][i]-Ex[i])**2/Ex[i])
data.insert(3,'chi test',chi)
chi_result=sum(data['chi test'])
df=len(data)-2
chi_alpha=scipy.stats.chi2.ppf(1-alpha,df)
print(data)
print('The calculated chi-square value =',chi_result)
if chi_result >chi_alpha:
    print("The hypothesis is rejected")
else :
    print('The hypothesis is not rejected')