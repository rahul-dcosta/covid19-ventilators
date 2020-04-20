#import pandas as pd
#from pulp import *

import pulp

cases = 17615
ventilator = 10000

ventilator = ventilator - .14 * cases - .05 * cases

print ("There are")
print (cases)
print ("and only")
print (ventilator)
print ("ventilators.")

# directory the data is saved
in_dir = '/Users/Vineet/Documents/Linear/covid19-ventilators'

# load data
#age_data = pd.read_csv(os.path.join(in_dir, 'PercentIndia.csv'))

age_groups = [1,11,21,31,41,51,61,71,81,91]
percents = [.0364, .0806, .2040, .2366, .1669, .1439, .0959, .0301, 0.004, 0.001]
num_aff = [0,0,0,0,0,0,0,0,0,0]
life = [0,0,0,0,0,0,0,0,0,0]
# Convert the impt data into dicts with keys as the day number, age-brackets & days of use of ventilator
#age_brackets = age_data['Group'].toList()
x = 0
for i in percents:
    num_aff[x] = cases * i
    print (num_aff[x])
    x = x + 1

print ("Life Expenctancies")
x = 0
for i in age_groups:
    expectancy = 68.7 - i - 5.5;
    if expectancy >= 0:
        life[x] = expectancy
    print (life[x])
    x = x + 1

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

#model +=  V <= 10000
model += 62.2 * A + 52.2 * B + 42.2 * C + 32.2 * D + 22.2 * E + 12.2 * F + 2.2 * G + 0 * I
model += A <= 641
model += B <= 1419
model += C <= 3593
model += D <= 4167
model += E <= 2940
model += F <= 1689
model += G <= 530
model += H <= 70
model += I <= 17
model += A + B + C + D + E + F + G + H + I <= ventilator

model.solve()
print (pulp.LpStatus[model.status])

# Print our decision variable values
print (A.varValue)
print (B.varValue)
print (C.varValue)
print (D.varValue)
print (E.varValue)
print (F.varValue)
print (G.varValue)
print (H.varValue)
print (I.varValue)
#print "Production of Car B = {}".format(B.varValue)

# Print our objective function value
#print pulp.value(model.objective)

print (pulp.value(model.objective))

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
