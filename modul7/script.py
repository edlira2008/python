from emoji import emojize

import pandas

print(emojize('python is :thumbs_up: , :snake: , :red_heart', variant="emoji_type", language='en'))
print(emojize(':pulgar_hacia_arriba:', language='es'))

#ni tabel t edhanave e paraqet dataframe
df=pandas.DataFrame({'name':['ernes','edlira','rini'],'age':[17,15,16,19], 'gender':['M','F','M','M',pandas.NA]})
print(df['name'][2])

