# imports
import pandas as pd
from pulp import *

# directory the data is saved
in_dir = '/Users/rahuldcosta/Desktop/MATH214/FinalProject/Data1/Data'

# load data
age_data_df = pd.read_csv(os.path.join(in_dir, 'Age Data.csv'))
daily_data_df = pd.read_csv(os.path.join(in_dir, 'Daily Expectations.csv'))
vent_usage_exp_df = pd.read_csv(os.path.join(in_dir, 'Vent Usage Days.csv'))

# Convert the impt data into dicts with keys as the day number, age-brackets & days of use of ventilator
vent_usage_days = vent_usage_exp_df['Days'].tolist()
age_brackets = age_data_df['Age Bracket'].tolist()
days = daily_data_df['t'].tolist()
vent_usage_prob_days = dict(zip(vent_usage_days, vent_usage_exp_df['Prob'].tolist()))
exp_pat_arr = dict(zip(days, daily_data_df['Exp Pat Arr'].tolist()))
vent_curr_and_back = dict(zip(days, daily_data_df['Vent Curr and Back'].tolist()))
arr_rates_age = dict(zip(age_brackets, age_data_df['Arrival Rate'].tolist()))
surv_wo_vent_rates = dict(zip(age_brackets, age_data_df['Surv WO Vent'].tolist()))
surv_w_vent_rates = dict(zip(age_brackets, age_data_df['Surv W Vent'].tolist()))
ass_rm_yrs = dict(zip(age_brackets, age_data_df['Ass Rem Yrs'].tolist()))

model = pulp.LpProblem("Max Life", LpMaximize)
x = pulp.LpVariable.dicts('Allow_Ventilator',
                          [(day, age_b) for age_b in age_brackets for day in days],
                            lowBound = 0,
                            upBound = 1,
                            cat = LpInteger)

model += lpSum([(arr_rates_age[ab]*exp_pat_arr[d]*ass_rm_yrs[ab]) * \
                (x[(d,ab)] * surv_w_vent_rates[ab] +  \
                (1 - x[(d,ab)]) * surv_wo_vent_rates[ab]) \
                for ab in age_brackets for d in days]) # for all

lpSum([x[(day, ab)]*(arr_rates_age[ab]*exp_pat_arr[day]) \
              for ab in age_brackets]) + lpSum([(arr_rates_age[ab]*exp_pat_arr[d])*x[(d,ab)] * \
       vent_usage_prob_days[days_used] \
       for ab in age_brackets \
       for d in range(max(day-vent_usage_exp_df.shape[0], 0),day) \
       for days_used in vent_usage_days if d + days_used > day])
#<= vent_curr_and_back[day], f"Vent supp day {day}"

import os
cwd = os.getcwd()
solverdir = 'Cbc-2.3.2-mac-osx-x86_64-gcc4.3.3-parallel\\bin\\cbc.exe'
solverdir = os.path.join(cwd, solverdir)
solver = COIN_CMD(path=solverdir)
model.solve(solver)

print("Status:", LpStatus[model.status])
print("Value:", model.objective.value())
# A nice table for our results:
decision_table_df = pd.DataFrame(index=days, columns=age_brackets)
for key in [(day, age_b) for age_b in age_brackets for day in days]:
    print(x[key].name, "=", x[key].varValue)
    decision_table_df.at[key[0], key[1]] = x[key].varValue
# take a look at how many 'leftover', ventilators we had on each day
for name, c in list(model.constraints.items()):
    print(name, ":\t\t", round(-1 * c.slack))
