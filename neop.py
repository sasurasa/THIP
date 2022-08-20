##clean_up

#import csv 
#Age selection (< 5 year)

import pandas as pd
pd.set_option('display.max_columns', None)
thip = pd.read_csv('/Users/surasaksangkhathat/Desktop/THIP/thip_data.csv')
thip = thip.loc[thip['age_y'] < 5]

#Working with format

thip['dateadm'] = pd.to_datetime(thip['dateadm'], format='%Y%m%d', errors='coerce')
thip['datedsc'] = pd.to_datetime(thip['datedsc'], format='%Y%m%d', errors='coerce')
thip['marry_status'] = thip['marry_status'].dropna()
thip['marry_status'] = thip.marry_status.astype('Int64')
thip.head()

#numeric to time for 'timeadm' and 'timedsc'
def getTime(t):
    return t[:2] + ':' + t[2:]

def fillfour(d):
    j = []
    for i in d:
        if len(i) == 4:
            pass
        elif len(i) == 3:
            i = '0' + i
        elif len(i) == 2:
            i = '00' + i
        j.append(i)
    return j

d = [str(x) for x in thip['timeadm']]
thip['timeadm'] = [getTime(x) for x in fillfour(d)]

e = [str(x) for x in thip['timedsc']]
thip['timedsc'] = [getTime(x) for x in fillfour(e)]



#set selection only interested ICD_10

q_neop = ['Q390','Q391','Q392','Q393','Q410','Q411','Q412','Q418','Q419', 'Q431','Q421', 'Q422', 'Q423', 'Q428', 'Q429','Q790','Q792','Q793']
neop = thip.loc[thip['pdx'].isin(q_neop)
| thip['sdx1'].isin(q_neop)
| thip['sdx2'].isin(q_neop)
| thip['sdx3'].isin(q_neop)
| thip['sdx4'].isin(q_neop)
| thip['sdx5'].isin(q_neop)
| thip['sdx6'].isin(q_neop)
| thip['sdx7'].isin(q_neop)
| thip['sdx8'].isin(q_neop)
| thip['sdx9'].isin(q_neop)
| thip['sdx10'].isin(q_neop)
| thip['sdx11'].isin(q_neop)
| thip['sdx12'].isin(q_neop)
| thip['sdx13'].isin(q_neop)
| thip['sdx14'].isin(q_neop)
| thip['sdx15'].isin(q_neop)
| thip['sdx16'].isin(q_neop)
| thip['sdx17'].isin(q_neop)
| thip['sdx18'].isin(q_neop)
| thip['sdx19'].isin(q_neop)
| thip['sdx20'].isin(q_neop)
]


neop = neop.drop_duplicates(subset=['pid'], keep='first')
len(neop)

#Package for selection by ICD-10 list

def select_Q(source, condition, dupdel = True):
    output = source.loc[source['pdx'].isin(condition)
    | source['sdx1'].isin(condition)
    | source['sdx2'].isin(condition)
    | source['sdx3'].isin(condition)
    | source['sdx4'].isin(condition)
    | source['sdx5'].isin(condition)
    | source['sdx6'].isin(condition)
    | source['sdx7'].isin(condition)
    | source['sdx8'].isin(condition)
    | source['sdx9'].isin(condition)
    | source['sdx10'].isin(condition)
    | source['sdx11'].isin(condition)
    | source['sdx12'].isin(condition)
    | source['sdx13'].isin(condition)
    | source['sdx14'].isin(condition)
    | source['sdx15'].isin(condition)
    | source['sdx16'].isin(condition)
    | source['sdx17'].isin(condition)
    | source['sdx18'].isin(condition)
    | source['sdx19'].isin(condition)
    | source['sdx20'].isin(condition)
    ]
    print('Number of selected records before duplication deletion are', len(output))
    if dupdel == True:
        output = output.drop_duplicates(subset=['pid'], keep='first')
    else:
        exit
    print('Number of selected records after duplication deletion are', len(output))
    return output
        

#Esophageal malformations

q_esop = ['Q390','Q391','Q392','Q393']
esop = thip.loc[thip['pdx'].isin(q_esop)
| thip['sdx1'].isin(q_esop)
| thip['sdx2'].isin(q_esop)
| thip['sdx3'].isin(q_esop)
| thip['sdx4'].isin(q_esop)
| thip['sdx5'].isin(q_esop)
| thip['sdx6'].isin(q_esop)
| thip['sdx7'].isin(q_esop)
| thip['sdx8'].isin(q_esop)
| thip['sdx9'].isin(q_esop)
| thip['sdx10'].isin(q_esop)
| thip['sdx11'].isin(q_esop)
| thip['sdx12'].isin(q_esop)
| thip['sdx13'].isin(q_esop)
| thip['sdx14'].isin(q_esop)
| thip['sdx15'].isin(q_esop)
| thip['sdx16'].isin(q_esop)
| thip['sdx17'].isin(q_esop)
| thip['sdx18'].isin(q_esop)
| thip['sdx19'].isin(q_esop)
| thip['sdx20'].isin(q_esop)
]

esop = esop.drop_duplicates(subset=['pid'], keep='first')
len(esop)

q_esop_390 = ['Q390']
esop_390 = esop.loc[esop['pdx'].isin(q_esop_390)
| esop['sdx1'].isin(q_esop_390)
| esop['sdx2'].isin(q_esop_390)
| esop['sdx3'].isin(q_esop_390)
| esop['sdx4'].isin(q_esop_390)
| esop['sdx5'].isin(q_esop_390)
| esop['sdx6'].isin(q_esop_390)
| esop['sdx7'].isin(q_esop_390)
| esop['sdx8'].isin(q_esop_390)
| esop['sdx9'].isin(q_esop_390)
| esop['sdx10'].isin(q_esop_390)
| esop['sdx11'].isin(q_esop_390)
| esop['sdx12'].isin(q_esop_390)
| esop['sdx13'].isin(q_esop_390)
| esop['sdx14'].isin(q_esop_390)
| esop['sdx15'].isin(q_esop_390)
| esop['sdx16'].isin(q_esop_390)
| esop['sdx17'].isin(q_esop_390)
| esop['sdx18'].isin(q_esop_390)
| esop['sdx19'].isin(q_esop_390)
| esop['sdx20'].isin(q_esop_390)
]


q_esop_391 = ['Q391']
esop_391 = esop.loc[esop['pdx'].isin(q_esop_391)
| esop['sdx1'].isin(q_esop_391)
| esop['sdx2'].isin(q_esop_391)
| esop['sdx3'].isin(q_esop_391)
| esop['sdx4'].isin(q_esop_391)
| esop['sdx5'].isin(q_esop_391)
| esop['sdx6'].isin(q_esop_391)
| esop['sdx7'].isin(q_esop_391)
| esop['sdx8'].isin(q_esop_391)
| esop['sdx9'].isin(q_esop_391)
| esop['sdx10'].isin(q_esop_391)
| esop['sdx11'].isin(q_esop_391)
| esop['sdx12'].isin(q_esop_391)
| esop['sdx13'].isin(q_esop_391)
| esop['sdx14'].isin(q_esop_391)
| esop['sdx15'].isin(q_esop_391)
| esop['sdx16'].isin(q_esop_391)
| esop['sdx17'].isin(q_esop_391)
| esop['sdx18'].isin(q_esop_391)
| esop['sdx19'].isin(q_esop_391)
| esop['sdx20'].isin(q_esop_391)
]

q_esop_392 = ['Q392']
esop_392 = esop.loc[esop['pdx'].isin(q_esop_392)
| esop['sdx1'].isin(q_esop_392)
| esop['sdx2'].isin(q_esop_392)
| esop['sdx3'].isin(q_esop_392)
| esop['sdx4'].isin(q_esop_392)
| esop['sdx5'].isin(q_esop_392)
| esop['sdx6'].isin(q_esop_392)
| esop['sdx7'].isin(q_esop_392)
| esop['sdx8'].isin(q_esop_392)
| esop['sdx9'].isin(q_esop_392)
| esop['sdx10'].isin(q_esop_392)
| esop['sdx11'].isin(q_esop_392)
| esop['sdx12'].isin(q_esop_392)
| esop['sdx13'].isin(q_esop_392)
| esop['sdx14'].isin(q_esop_392)
| esop['sdx15'].isin(q_esop_392)
| esop['sdx16'].isin(q_esop_392)
| esop['sdx17'].isin(q_esop_392)
| esop['sdx18'].isin(q_esop_392)
| esop['sdx19'].isin(q_esop_392)
| esop['sdx20'].isin(q_esop_392)
]

q_esop_393 = ['Q393']
esop_393 = esop.loc[esop['pdx'].isin(q_esop_393)
| esop['sdx1'].isin(q_esop_393)
| esop['sdx2'].isin(q_esop_393)
| esop['sdx3'].isin(q_esop_393)
| esop['sdx4'].isin(q_esop_393)
| esop['sdx5'].isin(q_esop_393)
| esop['sdx6'].isin(q_esop_393)
| esop['sdx7'].isin(q_esop_393)
| esop['sdx8'].isin(q_esop_393)
| esop['sdx9'].isin(q_esop_393)
| esop['sdx10'].isin(q_esop_393)
| esop['sdx11'].isin(q_esop_393)
| esop['sdx12'].isin(q_esop_393)
| esop['sdx13'].isin(q_esop_393)
| esop['sdx14'].isin(q_esop_393)
| esop['sdx15'].isin(q_esop_393)
| esop['sdx16'].isin(q_esop_393)
| esop['sdx17'].isin(q_esop_393)
| esop['sdx18'].isin(q_esop_393)
| esop['sdx19'].isin(q_esop_393)
| esop['sdx20'].isin(q_esop_393)
]

def sex_ratio(anom):
    anom_sex = anom.groupby(['sex'])['sex'].count().to_list()
    anom_sex_ratio = anom_sex[0]/anom_sex[1]
    print(anom_sex_ratio)
    

#Duodenal atresia/stenosis

q_duo = ['Q410']
duo = thip.loc[thip['pdx'].isin(q_duo)
| thip['sdx1'].isin(q_duo)
| thip['sdx2'].isin(q_duo)
| thip['sdx3'].isin(q_duo)
| thip['sdx4'].isin(q_duo)
| thip['sdx5'].isin(q_duo)
| thip['sdx6'].isin(q_duo)
| thip['sdx7'].isin(q_duo)
| thip['sdx8'].isin(q_duo)
| thip['sdx9'].isin(q_duo)
| thip['sdx10'].isin(q_duo)
| thip['sdx11'].isin(q_duo)
| thip['sdx12'].isin(q_duo)
| thip['sdx13'].isin(q_duo)
| thip['sdx14'].isin(q_duo)
| thip['sdx15'].isin(q_duo)
| thip['sdx16'].isin(q_duo)
| thip['sdx17'].isin(q_duo)
| thip['sdx18'].isin(q_duo)
| thip['sdx19'].isin(q_duo)
| thip['sdx20'].isin(q_duo)
]
duo = duo.drop_duplicates(subset=['pid'], keep='first')

len(duo)



q_small = ['Q411','Q412','Q418','Q419'] 
small = thip.loc[thip['pdx'].isin(q_small)
| thip['sdx1'].isin(q_small)
| thip['sdx2'].isin(q_small)
| thip['sdx3'].isin(q_small)
| thip['sdx4'].isin(q_small)
| thip['sdx5'].isin(q_small)
| thip['sdx6'].isin(q_small)
| thip['sdx7'].isin(q_small)
| thip['sdx8'].isin(q_small)
| thip['sdx9'].isin(q_small)
| thip['sdx10'].isin(q_small)
| thip['sdx11'].isin(q_small)
| thip['sdx12'].isin(q_small)
| thip['sdx13'].isin(q_small)
| thip['sdx14'].isin(q_small)
| thip['sdx15'].isin(q_small)
| thip['sdx16'].isin(q_small)
| thip['sdx17'].isin(q_small)
| thip['sdx18'].isin(q_small)
| thip['sdx19'].isin(q_small)
| thip['sdx20'].isin(q_small)
]


small = small.drop_duplicates(subset=['pid'], keep='first')
len(small)

q_hscr = ['Q431']
hscr = thip.loc[thip['pdx'].isin(q_hscr)
| thip['sdx1'].isin(q_hscr)
| thip['sdx2'].isin(q_hscr)
| thip['sdx3'].isin(q_hscr)
| thip['sdx4'].isin(q_hscr)
| thip['sdx5'].isin(q_hscr)
| thip['sdx6'].isin(q_hscr)
| thip['sdx7'].isin(q_hscr)
| thip['sdx8'].isin(q_hscr)
| thip['sdx9'].isin(q_hscr)
| thip['sdx10'].isin(q_hscr)
| thip['sdx11'].isin(q_hscr)
| thip['sdx12'].isin(q_hscr)
| thip['sdx13'].isin(q_hscr)
| thip['sdx14'].isin(q_hscr)
| thip['sdx15'].isin(q_hscr)
| thip['sdx16'].isin(q_hscr)
| thip['sdx17'].isin(q_hscr)
| thip['sdx18'].isin(q_hscr)
| thip['sdx19'].isin(q_hscr)
| thip['sdx20'].isin(q_hscr)
]

hscr = hscr.drop_duplicates(subset=['pid'], keep='first')
len(hscr)

q_arm = ['Q421', 'Q422', 'Q423', 'Q428', 'Q429']
arm = thip.loc[thip['pdx'].isin(q_arm)
| thip['sdx1'].isin(q_arm)
| thip['sdx2'].isin(q_arm)
| thip['sdx3'].isin(q_arm)
| thip['sdx4'].isin(q_arm)
| thip['sdx5'].isin(q_arm)
| thip['sdx6'].isin(q_arm)
| thip['sdx7'].isin(q_arm)
| thip['sdx8'].isin(q_arm)
| thip['sdx9'].isin(q_arm)
| thip['sdx10'].isin(q_arm)
| thip['sdx11'].isin(q_arm)
| thip['sdx12'].isin(q_arm)
| thip['sdx13'].isin(q_arm)
| thip['sdx14'].isin(q_arm)
| thip['sdx15'].isin(q_arm)
| thip['sdx16'].isin(q_arm)
| thip['sdx17'].isin(q_arm)
| thip['sdx18'].isin(q_arm)
| thip['sdx19'].isin(q_arm)
| thip['sdx20'].isin(q_arm)
]

arm = arm.drop_duplicates(subset=['pid'], keep='first')
len(arm)

q_omp = ['Q792']
omp = thip.loc[thip['pdx'].isin(q_omp)
| thip['sdx1'].isin(q_omp)
| thip['sdx2'].isin(q_omp)
| thip['sdx3'].isin(q_omp)
| thip['sdx4'].isin(q_omp)
| thip['sdx5'].isin(q_omp)
| thip['sdx6'].isin(q_omp)
| thip['sdx7'].isin(q_omp)
| thip['sdx8'].isin(q_omp)
| thip['sdx9'].isin(q_omp)
| thip['sdx10'].isin(q_omp)
| thip['sdx11'].isin(q_omp)
| thip['sdx12'].isin(q_omp)
| thip['sdx13'].isin(q_omp)
| thip['sdx14'].isin(q_omp)
| thip['sdx15'].isin(q_omp)
| thip['sdx16'].isin(q_omp)
| thip['sdx17'].isin(q_omp)
| thip['sdx18'].isin(q_omp)
| thip['sdx19'].isin(q_omp)
| thip['sdx20'].isin(q_omp)
]

omp = omp.drop_duplicates(subset=['pid'], keep='first')
len(omp)

q_gas = ['Q793']
gas = thip.loc[thip['pdx'].isin(q_gas)
| thip['sdx1'].isin(q_gas)
| thip['sdx2'].isin(q_gas)
| thip['sdx3'].isin(q_gas)
| thip['sdx4'].isin(q_gas)
| thip['sdx5'].isin(q_gas)
| thip['sdx6'].isin(q_gas)
| thip['sdx7'].isin(q_gas)
| thip['sdx8'].isin(q_gas)
| thip['sdx9'].isin(q_gas)
| thip['sdx10'].isin(q_gas)
| thip['sdx11'].isin(q_gas)
| thip['sdx12'].isin(q_gas)
| thip['sdx13'].isin(q_gas)
| thip['sdx14'].isin(q_gas)
| thip['sdx15'].isin(q_gas)
| thip['sdx16'].isin(q_gas)
| thip['sdx17'].isin(q_gas)
| thip['sdx18'].isin(q_gas)
| thip['sdx19'].isin(q_gas)
| thip['sdx20'].isin(q_gas)
]

gas = gas.drop_duplicates(subset=['pid'], keep='first')
len(gas)

q_cdh = ['Q790']
cdh = thip.loc[thip['pdx'].isin(q_cdh)
| thip['sdx1'].isin(q_cdh)
| thip['sdx2'].isin(q_arm)
| thip['sdx3'].isin(q_cdh)
| thip['sdx4'].isin(q_cdh)
| thip['sdx5'].isin(q_cdh)
| thip['sdx6'].isin(q_cdh)
| thip['sdx7'].isin(q_cdh)
| thip['sdx8'].isin(q_cdh)
| thip['sdx9'].isin(q_cdh)
| thip['sdx10'].isin(q_cdh)
| thip['sdx11'].isin(q_cdh)
| thip['sdx12'].isin(q_arm)
| thip['sdx13'].isin(q_cdh)
| thip['sdx14'].isin(q_cdh)
| thip['sdx15'].isin(q_cdh)
| thip['sdx16'].isin(q_cdh)
| thip['sdx17'].isin(q_cdh)
| thip['sdx18'].isin(q_cdh)
| thip['sdx19'].isin(q_cdh)
| thip['sdx20'].isin(q_cdh)
]

cdh = cdh.drop_duplicates(subset=['pid'], keep='first')
len(cdh)

#Count by groups

neop_year = neop.groupby(['g_year'])['g_year'].count().to_list()
esop_year = esop.groupby(['g_year'])['g_year'].count().to_list()
duo_year = duo.groupby(['g_year'])['g_year'].count().to_list()
small_year = small.groupby(['g_year'])['g_year'].count().to_list()
hscr_year = hscr.groupby(['g_year'])['g_year'].count().to_list()
arm_year = arm.groupby(['g_year'])['g_year'].count().to_list()
omp_year = omp.groupby(['g_year'])['g_year'].count().to_list()
gas_year = gas.groupby(['g_year'])['g_year'].count().to_list()
cdh_year = cdh.groupby(['g_year'])['g_year'].count().to_list()

#Find crude incidence per live birth

live_birth = [656571, 628450, 596736, 569338]

esop_inc = [i*10000 / j for i, j in zip(esop_year, live_birth)]
duo_inc = [i*10000 / j for i, j in zip(duo_year, live_birth)]
small_inc = [i*10000 / j for i, j in zip(small_year, live_birth)]
hscr_inc = [i*10000 / j for i, j in zip(hscr_year, live_birth)]
arm_inc = [i*10000 / j for i, j in zip(arm_year, live_birth)]
omp_inc = [i*10000 / j for i, j in zip(omp_year, live_birth)]
gas_inc = [i*10000 / j for i, j in zip(gas_year, live_birth)]
cdh_inc = [i*10000 / j for i, j in zip(cdh_year, live_birth)]


#Export to CSV

neop
neop.to_csv('neop.csv',index = False, sep=',', encoding='utf-8')




#Health region distribution

esop_region = esop.groupby(['health_region'])['health_region'].count().to_list()
duo_region = duo.groupby(['health_region'])['health_region'].count().to_list()
small_region = small.groupby(['health_region'])['health_region'].count().to_list()
hscr_region = hscr.groupby(['health_region'])['health_region'].count().to_list()
arm_region = arm.groupby(['health_region'])['health_region'].count().to_list()
omp_region = omp.groupby(['health_region'])['health_region'].count().to_list()
gas_region = gas.groupby(['health_region'])['health_region'].count().to_list()
cdh_region = cdh.groupby(['health_region'])['health_region'].count().to_list()

import matplotlib.pyplot as plt
import seaborn as sns
##define data
data = esop_region
labels = ['reg 1', 'reg 2', 'reg 3', 'reg 4', 'reg 5'
          ,'reg 6', 'reg 7', 'reg 8', 'reg 9', 'reg 10'
          , 'reg 11', 'reg 12', 'Bangkok']
##define Seaborn color palette to use
colors = sns.color_palette('bright')[0:5]
##create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()

neop_sex = neop.groupby(['sex'])['sex'].count().to_list()
neop_sex_ratio = neop_sex[0]/neop_sex[1]
eso_sex = esop.groupby(['sex'])['sex'].count().to_list()
duo_sex = duo.groupby(['sex'])['sex'].count().to_list()
small_sex = small.groupby(['sex'])['sex'].count().to_list()

hscr_sex = hscr.groupby(['sex'])['sex'].count().to_list()
hscr_sex_ratio = hscr_sex[0]/hscr_sex[1]

arm_sex = arm.groupby(['sex'])['sex'].count().to_list()

omp_sex = omp.groupby(['sex'])['sex'].count().to_list()

gas_sex = gas.groupby(['sex'])['sex'].count().to_list()
cdh_sex = cdh.groupby(['sex'])['sex'].count().to_list()


esop_count = len(esop)
esop_mortal = esop.loc[esop['death_date'].notnull()]
esop_mortal_region = esop_mortal.groupby(['health_region'])['health_region'].count()
esop_mortal_count = len(esop.loc[esop['discht']==9])+len(esop.loc[esop['discht']==8]) + esop.loc[(esop['discht']!=9) & (esop['discht'] !=8)]['death_date'].notnull().sum()
esop_mortal_rate = 100*esop_mortal_count/esop_count
print(esop_count)
print(esop_mortal_count)
print(esop_mortal_rate)

def mortal(anom):
    anom_count = len(anom)
    anom_mortal = len(anom.loc[anom['death_date'].notnull()])
    anom_mortal_rate = 100*anom_mortal/anom_count
    print('total death cases =', anom_mortal,  'in', anom_count, 'cases')
    print('mortality rate =', anom_mortal_rate)

duo_count = len(duo)
duo_mortal = duo.loc[duo['death_date'].notnull()]
duo_mortal_region = duo_mortal.groupby(['health_region'])['health_region'].count()
print(duo_mortal_region)
duo_mortal_count = len(duo.loc[duo['discht']==9])+len(duo.loc[duo['discht']==8]) + duo.loc[(duo['discht']!=9) & (duo['discht'] !=8)]['death_date'].notnull().sum()
duo_mortal_rate = 100*duo_mortal_count/duo_count
print(duo_count)
print(duo_mortal_count)
print(duo_mortal_rate)

small_count = len(small)
small_mortal_count = len(small.loc[small['discht']==9])+len(small.loc[small['discht']==8]) + small.loc[(small['discht']!=9) & (small['discht'] !=8)]['death_date'].notnull().sum()
small_mortal_rate = 100*small_mortal_count/small_count
print(small_count)
print(small_mortal_count)
print(small_mortal_rate)

hscr_count = len(hscr)
hscr_mortal_count = len(hscr.loc[hscr['discht']==9])+len(hscr.loc[hscr['discht']==8]) + hscr.loc[(hscr['discht']!=9) & (hscr['discht'] !=8)]['death_date'].notnull().sum()
hscr_mortal_rate = 100*hscr_mortal_count/hscr_count
print(hscr_count)
print(hscr_mortal_count)
print(hscr_mortal_rate)

arm_count = len(arm)
arm_mortal_count = len(arm.loc[arm['discht']==9])+len(arm.loc[arm['discht']==8]) + arm.loc[(arm['discht']!=9) & (arm['discht'] !=8)]['death_date'].notnull().sum()
arm_mortal_rate = 100*arm_mortal_count/arm_count
print(arm_count)
print(arm_mortal_count)
print(arm_mortal_rate)

omp_count = len(omp)
omp_mortal_count = len(omp.loc[omp['discht']==9])+len(omp.loc[omp['discht']==8]) + omp.loc[(omp['discht']!=9) & (omp['discht'] !=8)]['death_date'].notnull().sum()
omp_mortal_rate = 100*omp_mortal_count/omp_count
print(omp_count)
print(omp_mortal_count)
print(omp_mortal_rate)

gas_count = len(gas)
gas_mortal_count = len(gas.loc[gas['discht']==9])+len(gas.loc[gas['discht']==8]) + gas.loc[(gas['discht']!=9) & (gas['discht'] !=8)]['death_date'].notnull().sum()
gas_mortal_rate = 100*gas_mortal_count/gas_count
print(gas_count)
print(gas_mortal_count)
print(gas_mortal_rate)

cdh_count = len(cdh)
cdh_mortal_count = len(cdh.loc[cdh['discht']==9])+len(cdh.loc[cdh['discht']==8]) + cdh.loc[(cdh['discht']!=9) & (cdh['discht'] !=8)]['death_date'].notnull().sum()
cdh_mortal_rate = 100*cdh_mortal_count/cdh_count
print(cdh_count)
print(cdh_mortal_count)
print(cdh_mortal_rate)

neop_count = len(neop)
neop_mortal = neop.loc[neop['death_date'].notnull()]
neop_mortal_year = neop_mortal.groupby(['g_year'])['g_year'].count().to_list()
neop_mortal_count = len(neop.loc[neop['discht']==9])+len(neop.loc[neop['discht']==8]) + neop.loc[(neop['discht']!=9) & (neop['discht'] !=8)]['death_date'].notnull().sum()
neop_mortal_rate = 100*neop_mortal_count/neop_count
print(neop_count)
print(neop_mortal_count)
print(neop_mortal_rate)

#Down_association

q_down = ['Q909']

esop_down = esop.loc[esop['pdx'].isin(q_down)
| esop['sdx1'].isin(q_down)
| esop['sdx2'].isin(q_down)
| esop['sdx3'].isin(q_down)
| esop['sdx4'].isin(q_down)
| esop['sdx5'].isin(q_down)
| esop['sdx6'].isin(q_down)
| esop['sdx7'].isin(q_down)
| esop['sdx8'].isin(q_down)
| esop['sdx9'].isin(q_down)
| esop['sdx10'].isin(q_down)
| esop['sdx11'].isin(q_down)
| esop['sdx12'].isin(q_down)
| esop['sdx13'].isin(q_down)
| esop['sdx14'].isin(q_down)
| esop['sdx15'].isin(q_down)
| esop['sdx16'].isin(q_down)
| esop['sdx17'].isin(q_down)
| esop['sdx18'].isin(q_down)
| esop['sdx19'].isin(q_down)
| esop['sdx20'].isin(q_down)
]

duo_down = duo.loc[duo['pdx'].isin(q_down)
| duo['sdx1'].isin(q_down)
| duo['sdx2'].isin(q_down)
| duo['sdx3'].isin(q_down)
| duo['sdx4'].isin(q_down)
| duo['sdx5'].isin(q_down)
| duo['sdx6'].isin(q_down)
| duo['sdx7'].isin(q_down)
| duo['sdx8'].isin(q_down)
| duo['sdx9'].isin(q_down)
| duo['sdx10'].isin(q_down)
| duo['sdx11'].isin(q_down)
| duo['sdx12'].isin(q_down)
| duo['sdx13'].isin(q_down)
| duo['sdx14'].isin(q_down)
| duo['sdx15'].isin(q_down)
| duo['sdx16'].isin(q_down)
| duo['sdx17'].isin(q_down)
| duo['sdx18'].isin(q_down)
| duo['sdx19'].isin(q_down)
| duo['sdx20'].isin(q_down)
]


small_down = small.loc[small['pdx'].isin(q_down)
| small['sdx1'].isin(q_down)
| small['sdx2'].isin(q_down)
| small['sdx3'].isin(q_down)
| small['sdx4'].isin(q_down)
| small['sdx5'].isin(q_down)
| small['sdx6'].isin(q_down)
| small['sdx7'].isin(q_down)
| small['sdx8'].isin(q_down)
| small['sdx9'].isin(q_down)
| small['sdx10'].isin(q_down)
| small['sdx11'].isin(q_down)
| small['sdx12'].isin(q_down)
| small['sdx13'].isin(q_down)
| small['sdx14'].isin(q_down)
| small['sdx15'].isin(q_down)
| small['sdx16'].isin(q_down)
| small['sdx17'].isin(q_down)
| small['sdx18'].isin(q_down)
| small['sdx19'].isin(q_down)
| small['sdx20'].isin(q_down)
]

hscr_down = hscr.loc[hscr['pdx'].isin(q_down)
| hscr['sdx1'].isin(q_down)
| hscr['sdx2'].isin(q_down)
| hscr['sdx3'].isin(q_down)
| hscr['sdx4'].isin(q_down)
| hscr['sdx5'].isin(q_down)
| hscr['sdx6'].isin(q_down)
| hscr['sdx7'].isin(q_down)
| hscr['sdx8'].isin(q_down)
| hscr['sdx9'].isin(q_down)
| hscr['sdx10'].isin(q_down)
| hscr['sdx11'].isin(q_down)
| hscr['sdx12'].isin(q_down)
| hscr['sdx13'].isin(q_down)
| hscr['sdx14'].isin(q_down)
| hscr['sdx15'].isin(q_down)
| hscr['sdx16'].isin(q_down)
| hscr['sdx17'].isin(q_down)
| hscr['sdx18'].isin(q_down)
| hscr['sdx19'].isin(q_down)
| hscr['sdx20'].isin(q_down)
]

arm_down = arm.loc[arm['pdx'].isin(q_down)
| arm['sdx1'].isin(q_down)
| arm['sdx2'].isin(q_down)
| arm['sdx3'].isin(q_down)
| arm['sdx4'].isin(q_down)
| arm['sdx5'].isin(q_down)
| arm['sdx6'].isin(q_down)
| arm['sdx7'].isin(q_down)
| arm['sdx8'].isin(q_down)
| arm['sdx9'].isin(q_down)
| arm['sdx10'].isin(q_down)
| arm['sdx11'].isin(q_down)
| arm['sdx12'].isin(q_down)
| arm['sdx13'].isin(q_down)
| arm['sdx14'].isin(q_down)
| arm['sdx15'].isin(q_down)
| arm['sdx16'].isin(q_down)
| arm['sdx17'].isin(q_down)
| arm['sdx18'].isin(q_down)
| arm['sdx19'].isin(q_down)
| arm['sdx20'].isin(q_down)
]
omp_down = omp.loc[omp['pdx'].isin(q_down)
| omp['sdx1'].isin(q_down)
| omp['sdx2'].isin(q_down)
| omp['sdx3'].isin(q_down)
| omp['sdx4'].isin(q_down)
| omp['sdx5'].isin(q_down)
| omp['sdx6'].isin(q_down)
| omp['sdx7'].isin(q_down)
| omp['sdx8'].isin(q_down)
| omp['sdx9'].isin(q_down)
| omp['sdx10'].isin(q_down)
| omp['sdx11'].isin(q_down)
| omp['sdx12'].isin(q_down)
| omp['sdx13'].isin(q_down)
| omp['sdx14'].isin(q_down)
| omp['sdx15'].isin(q_down)
| omp['sdx16'].isin(q_down)
| omp['sdx17'].isin(q_down)
| omp['sdx18'].isin(q_down)
| omp['sdx19'].isin(q_down)
| omp['sdx20'].isin(q_down)
]

gas_down = gas.loc[gas['pdx'].isin(q_down)
| gas['sdx1'].isin(q_down)
| gas['sdx2'].isin(q_down)
| gas['sdx3'].isin(q_down)
| gas['sdx4'].isin(q_down)
| gas['sdx5'].isin(q_down)
| gas['sdx6'].isin(q_down)
| gas['sdx7'].isin(q_down)
| gas['sdx8'].isin(q_down)
| gas['sdx9'].isin(q_down)
| gas['sdx10'].isin(q_down)
| gas['sdx11'].isin(q_down)
| gas['sdx12'].isin(q_down)
| gas['sdx13'].isin(q_down)
| gas['sdx14'].isin(q_down)
| gas['sdx15'].isin(q_down)
| gas['sdx16'].isin(q_down)
| gas['sdx17'].isin(q_down)
| gas['sdx18'].isin(q_down)
| gas['sdx19'].isin(q_down)
| gas['sdx20'].isin(q_down)
]

cdh_down = cdh.loc[cdh['pdx'].isin(q_down)
| cdh['sdx1'].isin(q_down)
| cdh['sdx2'].isin(q_down)
| cdh['sdx3'].isin(q_down)
| cdh['sdx4'].isin(q_down)
| cdh['sdx5'].isin(q_down)
| cdh['sdx6'].isin(q_down)
| cdh['sdx7'].isin(q_down)
| cdh['sdx8'].isin(q_down)
| cdh['sdx9'].isin(q_down)
| cdh['sdx10'].isin(q_down)
| cdh['sdx11'].isin(q_down)
| cdh['sdx12'].isin(q_down)
| cdh['sdx13'].isin(q_down)
| cdh['sdx14'].isin(q_down)
| cdh['sdx15'].isin(q_down)
| cdh['sdx16'].isin(q_down)
| cdh['sdx17'].isin(q_down)
| cdh['sdx18'].isin(q_down)
| cdh['sdx19'].isin(q_down)
| cdh['sdx20'].isin(q_down)
]


#count and sort procedure
def procdict(diag):
    proc_list = []
    procedure_dict = {}
    proc_list = diag['proc1'].to_list()
    proc_list = proc_list + diag['proc2'].to_list()
    proc_list = proc_list + diag['proc3'].to_list()
    proc_list = proc_list + diag['proc4'].to_list()
    proc_list = proc_list + diag['proc5'].to_list()
    proc_list = proc_list + diag['proc6'].to_list()
    proc_list = proc_list + diag['proc7'].to_list()
    proc_list = proc_list + diag['proc8'].to_list()
    proc_list = proc_list + diag['proc9'].to_list()
    proc_list = proc_list + diag['proc10'].to_list()
    proc_list = proc_list + diag['proc11'].to_list()
    proc_list = proc_list + diag['proc12'].to_list()
    proc_list = proc_list + diag['proc13'].to_list()
    proc_list = proc_list + diag['proc14'].to_list()
    proc_list = proc_list + diag['proc15'].to_list()
    proc_list = proc_list + diag['proc16'].to_list()
    proc_list = proc_list + diag['proc17'].to_list()
    proc_list = proc_list + diag['proc18'].to_list()
    proc_list = proc_list + diag['proc19'].to_list()
    proc_list = proc_list + diag['proc20'].to_list()
    proc_list = [item for item in proc_list if not(pd.isnull(item)) == True]
    for entry in proc_list:
        if entry in(procedure_dict):
            procedure_dict[entry] += 1
        else:
            procedure_dict[entry] = 1
    for key in sorted(procedure_dict.keys()):
        print(key , " :: " , procedure_dict[key])
    

# Select by procedure
proc_eso = ['4251', '4252','4253','4254','4255','4256','4257','4258','4259']

def select_procedure(source, condition):
    output = source.loc[source['proc1'].isin(condition)
    | source['proc2'].isin(condition)
    | source['proc3'].isin(condition)
    | source['proc4'].isin(condition)
    | source['proc5'].isin(condition)
    | source['proc6'].isin(condition)
    | source['proc7'].isin(condition)
    | source['proc8'].isin(condition)
    | source['proc9'].isin(condition)
    | source['proc10'].isin(condition)
    | source['proc11'].isin(condition)
    | source['proc12'].isin(condition)
    | source['proc13'].isin(condition)
    | source['proc14'].isin(condition)
    | source['proc15'].isin(condition)
    | source['proc16'].isin(condition)
    | source['proc17'].isin(condition)
    | source['proc18'].isin(condition)
    | source['proc19'].isin(condition)
    | source['proc20'].isin(condition)
    ]
    print('Number of selected records are', len(output))
    return output

esop_pro = select_procedure(thip, proc_eso)
esop_pro = esop_pro.drop_duplicates(subset=['pid'], keep='first')
