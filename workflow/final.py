import pandas as pd
import numpy as np

df1 = pd.read_csv('op.csv')
df2 = pd.read_csv('ind.csv')

def get_ind():
    st = df2['ind'][0]
    st = st[1:len(st)-1]
    l = st.split(',')
    ind = [int(i) for i in l]
    return ind

def get_op():
    return list(df1['ans'])


ind = get_ind()
op = get_op()
final_op = ['' for i in range(692542)]
print(len(ind))
print(len(op))

for i in ind:
    final_op[i] = op[0]
    op.pop(0)


print(len(op))
final_df = pd.DataFrame()
final_df['fuzzy_ans'] = final_op
final_df.to_csv('final.csv', index = False)