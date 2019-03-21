# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].str.lower()
df['total'] = df['Jan'] + df['Feb'] + df['Mar']
sum_row = df[['Jan','Feb','Mar','total']].sum()
df_final = df.append(sum_row, ignore_index=True)
print(df_final.tail())


# Code ends here


# --------------
import requests

# Code starts here
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"

response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1.columns = df1.iloc[11]
df1 = df1.iloc[12:]
df1['United States of America'] = df1['United States of America'].str.replace(' ','')
print(df1.head())
# Code ends here


# --------------






df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here

mapping = dict(zip(df1['United States of America'],df1['US']))
df_final.insert(6, 'abbr', '')
df_final['abbr'] = df_final['state'].map(mapping)
print(df_final.head())
#df_final['abbr'] = 


# Code ends here


# --------------
# Code stars here
print(df_final['abbr'].isnull().sum())

df_final.loc[df_final['state']=='mississipi','abbr']='MS'
df_final.loc[df_final['state']=='tenessee','abbr']='TN'
print(df_final['abbr'].isnull().sum())
# Code ends here


# --------------
# Code starts here




df_sub = df_final.groupby('abbr')['abbr','Jan','Feb','Mar','total'].sum()
#print(df_sub)

formatted_df = df_sub.applymap(lambda x: '$'+str(x))
print(formatted_df)
# Code ends here


# --------------
# Code starts here

sum_row = df_final[['Jan','Feb','Mar','total']].sum().to_frame()

df_sub_sum = sum_row.transpose()

df_sub_sum =df_sub_sum.applymap(lambda x:'$'+str(x))

final_table = formatted_df.append(df_sub_sum)

final_table.rename(index={0:'Total'},inplace=True)
print(final_table)




# Code ends here


# --------------
# Code starts here





df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']

print(df_sub)

plt.pie(df_sub['total'],labels=df_sub.index)
plt.show()
# Code ends here


