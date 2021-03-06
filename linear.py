#import pandas as pd
#from pulp import *

import pulp
from decimal import getcontext, Decimal
import numpy as np
from random import seed
from random import randint
from random import gauss
import json

getcontext().prec = 3
cases = 17615
#ventilator = 10000
ventilators = input ("Enter number of ventilators: ")
#ventilators = "10000"
ventilator = int(ventilators)

used = .14 * cases - .05 * cases
ventilator = ventilator - used

import requests

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

querystring = {"country":"India"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "1785afdd39msh2137b157fb3ce6bp1b8682jsna9019ab09790"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

data = response.json()

newcases = data['latest_stat_by_country'][0]['active_cases']
#print (type(newcases))
cases = int(newcases.replace(',',''))
#print (type(cases))
#print (cases)

#print(response['latest_stat_by_country']['active_cases'])
#print (newcases)

print ("Given that 14% of cases are severe and 5% of cases are critical, we will allocate ventilators to those patients first. This takes away a total of " + str(round(used)) + " ventilators")

print ("There are " + str(cases) + " cases and only " + str(int(ventilator)) + " ventilators")
#print (cases)
#print ("and only")
#print (ventilator)
#print ("ventilators.")

# directory the data is saved
in_dir = '/Users/Vineet/Documents/Linear/covid19-ventilators'

# load data
#age_data = pd.read_csv(os.path.join(in_dir, 'PercentIndia.csv'))

age_groups = [1,11,21,31,41,51,61,71,81,91]
percents = [.0364, .0806, .2040, .2366, .1669, .1439, .0959, .0301, 0.004, 0.001]
num_aff = [0,0,0,0,0,0,0,0,0,0]
life = [0,0,0,0,0,0,0,0,0,0]
survWvent = [.77, .73, .67, .63, .58, .23, .21, .16, .16]
survWO = [.4, .35, .35, .3, .25, .12, .15, .08, .08]
arrrate = [.01, .06, .08, .12, .16, .2, .25, .06, .06]
num_cases = [0,0,0,0,0,0,0,0,0,0]
years = np.array([0,0,0,0,0,0,0,0,0])
ventilator_usage = [0,0,0,0,0,0,0,0,0]
# Convert the impt data into dicts with keys as the day number, age-brackets & days of use of ventilator
#age_brackets = age_data['Group'].toList()
x = 0
for i in percents:
    num_cases[x] = cases * i
    #print (num_aff[x])
    x = x + 1
#print (num_cases)
#print ("Life Expenctancies:")
x = 0
for i in age_groups:
    expectancy = 68.7 - i - 5.5;
    if expectancy >= 0:
        life[x] = expectancy
   # print (life[x])
    x = x + 1

#print (round(life[6],1))
#x = 0    
#print ("Number of cases:")

'''
sumnum = 0
for i in arrrate:
    num_cases[x] = i * cases;
    sumnum  = sumnum + num_cases[x]
    #print (num_cases[x])
    x = x + 1
print(num_cases)
'''


# print (sumnum)
print ("Patients in each age group")
print ("O - 10 years: " + str(round(num_cases[0])) + " patients")
print ("11 - 20 years: " + str(round(num_cases[1])) + " patients")
print ("21 - 30 years: " + str(round(num_cases[2])) + " patients")
print ("31 - 40 years: " + str(round(num_cases[3])) + " patients")
print ("41 - 50 years: " + str(round(num_cases[4])) + " patients")
print ("51 - 60 years: " + str(round(num_cases[5])) + " patients")
print ("61 - 70 years: " + str(round(num_cases[6])) + " patients")
print ("71 - 80 years: " + str(round(num_cases[7])) + " patients")
print ("81 - 90 years: " + str(round(num_cases[8])) + " patients")

'''
x = 0
for i in num_cases:
    years[x] = i * life[x] * survWvent[x]
    #print (years[x])
    x = x + 1
'''
x = 0

seed(1)
for _ in range(int(ventilator)):
    value = gauss(55, 15)
    x = x + 1
   
        
    if value < 11:
        ventilator_usage[0] = ventilator_usage[0] + 1
    elif (value < 21):
        ventilator_usage[1] = ventilator_usage[1] + 1
    elif (value < 31):
        ventilator_usage[2] = ventilator_usage[2] + 1
    elif (value < 41):
        ventilator_usage[3] = ventilator_usage[3] + 1
    elif (value < 51):
        ventilator_usage[4] = ventilator_usage[4] + 1
    elif (value < 61):
        ventilator_usage[5] = ventilator_usage[5] + 1
    elif (value < 71):
        ventilator_usage[6] = ventilator_usage[6] + 1
    elif (value < 81):
        ventilator_usage[7] = ventilator_usage[7] + 1
    else:
        ventilator_usage[8] = ventilator_usage[8] + 1
        
print ("Ventilator usage in each age group")
print ("O - 10 years: " + str(round(ventilator_usage[0])) + " patients")
print ("11 - 20 years: " + str(round(ventilator_usage[1])) + " patients")
print ("21 - 30 years: " + str(round(ventilator_usage[2])) + " patients")
print ("31 - 40 years: " + str(round(ventilator_usage[3])) + " patients")
print ("41 - 50 years: " + str(round(ventilator_usage[4])) + " patients")
print ("51 - 60 years: " + str(round(ventilator_usage[5])) + " patients")
print ("61 - 70 years: " + str(round(ventilator_usage[6])) + " patients")
print ("71 - 80 years: " + str(round(ventilator_usage[7])) + " patients")
print ("81 - 90 years: " + str(round(ventilator_usage[8])) + " patients")
# print(x)
totalyears = survWvent[0] * round(life[0],1) * ventilator_usage[0] + survWO[0]*round(life[0],1)*(num_cases[0]-ventilator_usage[0]) + survWvent[1]*round(life[1],1) * ventilator_usage[1] + survWO[1]*round(life[1],1)*(num_cases[1]-ventilator_usage[1]) + survWvent[2]*round(life[2],1) * ventilator_usage[2] + survWO[2]*round(life[2],1)*(num_cases[2]-ventilator_usage[2]) + survWvent[3]*round(life[3],1) * ventilator_usage[3] + survWO[3]*round(life[3],1)*(num_cases[3]-ventilator_usage[3]) + survWvent[4]*round(life[4],1) * ventilator_usage[4] + survWO[4]*round(life[4],1)*(num_cases[4]-ventilator_usage[4]) + survWvent[5]*round(life[5],1) * ventilator_usage[5] + survWO[5]*round(life[5],1)*(num_cases[5]-ventilator_usage[5]) + survWvent[6]*round(life[6],1) * ventilator_usage[6] + survWO[6]*round(life[6],1)*(num_cases[6]-ventilator_usage[6]) + .16 * ventilator_usage[7] + .08*(num_cases[7]-ventilator_usage[7])  + .16 * ventilator_usage[8] + .08*(num_cases[8]-ventilator_usage[8])     
#totalyears = .77*62.2 * ventilator_usage[0] + .4*62.2*(num_cases[0]-ventilator_usage[0]) + .73*52.2 * ventilator_usage[1] + .35*52.2*(num_cases[1]-ventilator_usage[1]) + .67*42.2 * ventilator_usage[2] + .35*42.2*(num_cases[2]-ventilator_usage[2]) + .63*32.2 * ventilator_usage[3] + .3*32.2*(num_cases[3]-ventilator_usage[3]) + .58*22.2 * ventilator_usage[4] + .25*22.2*(num_cases[4]-ventilator_usage[4]) + .23*12.2 * ventilator_usage[5] + .12*12.2*(num_cases[5]-ventilator_usage[5]) + .21*2.2 * ventilator_usage[6] + .15*2.2*(num_cases[6]-ventilator_usage[6]) + .16 * ventilator_usage[7] + .08*(num_cases[7]-ventilator_usage[7])  + .16 * ventilator_usage[8] + .08*(num_cases[8]-ventilator_usage[8])     
print ("Current life years expected upon random selection of patients using a normal distribution to emulate 'first come first serve' policy: " + str(round(totalyears)))

# print (ventilator_usage)  
#print (sum(ventilator_usage))  

# print ("Total years:")
#totalyears = sum(years)
'''
for i in range(9):
    totalyears = totalyears + years[i]
   # print (totalyears)
    
print ("Total years")
print (totalyears)
        '''
#expectedtotalyears = 17615 * .01 * 62.2 + 17615 * 0.06 * 52.2 + 17616 * 0.08 * 42.2 + 17615 * .12 + 17615 * .16 * 32.2 + 17615 * .2 * 22.2 + 17615 * .25 * 12.2 + 17615 * .12 * 2.2
#print (expectedtotalyears)


model = pulp.LpProblem("Life year maximizing problem", pulp.LpMaximize)

A = pulp.LpVariable('0', lowBound=0, cat='Integer')
B = pulp.LpVariable('11', lowBound=0, cat='Integer')
C = pulp.LpVariable('21', lowBound=0, cat='Integer')
D = pulp.LpVariable('31', lowBound=0, cat='Integer')
E = pulp.LpVariable('41', lowBound=0, cat='Integer')
F = pulp.LpVariable('51', lowBound=0, cat='Integer')
G = pulp.LpVariable('61', lowBound=0, cat='Integer')
H = pulp.LpVariable('71', lowBound=0, cat='Integer')
I = pulp.LpVariable('81', lowBound=0, cat='Integer')
V = pulp.LpVariable('Ventilators', upBound=10000, cat='Integer')


#model += 30000 * A + 45000 * B, "Profit"
# constraint - ventilators <= 10000
# Constraints
#model += .77*62.2 * A + .73*52.2 * B + .67*42.2 * C + .63*32.2 * D + .58*22.2 * E + .23*12.2 * F + .21*2.2 * G + .16 * H
#model +=  V <= 10000
model += survWvent[0] * round(life[0],1)* A + survWO[0]*round(life[0],1)*(641-A) + survWvent[1] * round(life[1],1) * B + survWO[1]*round(life[1],1)*(1419-B) + survWvent[2] * round(life[2],1) * C + survWO[2]*round(life[2],1)*(3593-C) + survWvent[3] * round(life[3],1) * D + survWO[3]*round(life[3],1)*(4167-D) + survWvent[4] * round(life[4],1) * E + survWO[4]*round(life[4],1)*(2940-E) + survWvent[5] * round(life[5],1) * F + survWO[5]*round(life[5],1)*(1689-F) + survWvent[6] * round(life[6],1) * G + survWO[6]*round(life[6],1)*(530-G) + .16 * H + .08*(70-H) + .16 * I + .08*(70-I) 
#model += .77*62.2 * A + .4*62.2*(641-A) + .73*52.2 * B + .35*52.2*(1419-B) + .67*42.2 * C + .35*42.2*(3593-C) + .63*32.2 * D + .3*32.2*(4167-D) + .58*22.2 * E + .25*22.2*(2940-E) + .23*12.2 * F + .12*12.2*(1689-F) + .21*2.2 * G + .15*2.2*(530-G) + .16 * H + .08*(70-H) + .16 * I + .08*(70-I) 
model += A <= num_cases[0]
model += B <= num_cases[1]
model += C <= num_cases[2]
model += D <= num_cases[3]
model += E <= num_cases[4]
model += F <= num_cases[5]
model += G <= num_cases[6]
model += H <= num_cases[7]
model += I <= num_cases[8]
model += A + B + C + D + E + F + G + H + I <= ventilator

model.solve()
print (pulp.LpStatus[model.status])

# Print our decision variable values
print ("Ventilator usage in each age group")
print ("O - 10 years: " + str(A.varValue) + " patients")
print ("11 - 20 years: " + str(B.varValue) + " patients")
print ("21 - 30 years: " + str(C.varValue) + " patients")
print ("31 - 40 years: " + str(D.varValue) + " patients")
print ("41 - 50 years: " + str(E.varValue) + " patients")
print ("51 - 60 years: " + str(F.varValue) + " patients")
print ("61 - 70 years: " + str(G.varValue) + " patients")
print ("71 - 80 years: " + str(H.varValue) + " patients")
print ("81 - 90 years: " + str(I.varValue) + " patients")



#print "Production of Car B = {}".format(B.varValue)

# Print our objective function value
#print pulp.value(model.objective)

print ("Total life years through optimization of ventilator usage: " + str(round(pulp.value(model.objective))))


difference = int(round(pulp.value(model.objective))) - totalyears
print ("By optimizing ventilator usage, we were able to increase expected life years by " + str(round(difference)))
#print(age_data['Percent'][1])

''''
x = 0
for i in range(10):
    age_data['NumAffected'][i] = age_data['Percent'][i]* cases * .01;
    print(age_data['NumAffected'][i])
'''''



''''

model = pulp.LpProblem("Life Year maximising problem", pulp.LpMaximize)

A = pulp.LpVariable('lifeyears', lowBound=0, cat='Integer')
B = pulp.LpVariable('patients', lowBound=0, cat='Integer')
C = pulp.LpVariable('ventilators', upBound=10000, cat='Integer')

model += 30000 * A + 45000 * B, "Profit"

# Constraints
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21

model.solve()
print (pulp.LpStatus[model.status])

# Print our decision variable values
print (A.varValue)
print (B.varValue)
#print "Production of Car B = {}".format(B.varValue)

# Print our objective function value
#print pulp.value(model.objective)

print (pulp.value(model.objective))

'''
