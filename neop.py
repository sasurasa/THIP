import pandas as pd

##clean_up

#import csv 
pd.set_option('display.max_columns', None)
thip = pd.read_csv('/Users/surasaksangkhathat/Desktop/THIP/thip_data.csv')

#set selection only interested age (<1)

thip = thip.loc[thip['age_y'] < 1]

#find duplicated identity ('tran_id','pid') and delete

thip = thip.drop_duplicates(subset=['tran_id', 'pid'], keep='first')

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

q_neop = ['Q390','Q391','Q392','Q393','Q410','Q411','Q412','Q418','Q419']
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
len(esop)

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

#Count by groups

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

esop_inc = [i*10000 / j for i, j in zip(eso_year, live_birth)]
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
data = eso_region
labels = ['reg 1', 'reg 2', 'reg 3', 'reg 4', 'reg 5'
          ,'reg 6', 'reg 7', 'reg 8', 'reg 9', 'reg 10'
          , 'reg 11', 'reg 12', 'Bangkok']
##define Seaborn color palette to use
colors = sns.color_palette('bright')[0:5]
##create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()

eso_sex = esop.groupby(['sex'])['sex'].count().to_list()
duo_sex = duo.groupby(['sex'])['sex'].count().to_list()
small_sex = small.groupby(['sex'])['sex'].count().to_list()

hscr_sex = hscr.groupby(['sex'])['sex'].count().to_list()
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


