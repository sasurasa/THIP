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
]

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
]

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
]

q_arm = ['Q421', 'Q422', 'Q423', 'Q428', 'Q429']
arm = thip.loc[thip['pdx'].isin(q_arm)
| thip['sdx1'].isin(q_arm)
| thip['sdx3'].isin(q_arm)
| thip['sdx4'].isin(q_arm)
| thip['sdx5'].isin(q_arm)
| thip['sdx6'].isin(q_arm)
| thip['sdx7'].isin(q_arm)
| thip['sdx8'].isin(q_arm)
| thip['sdx9'].isin(q_arm)
| thip['sdx10'].isin(q_arm)
]


q_omp = ['Q792']
omp = thip.loc[thip['pdx'].isin(q_omp)
| thip['sdx1'].isin(q_omp)
| thip['sdx3'].isin(q_omp)
| thip['sdx4'].isin(q_omp)
| thip['sdx5'].isin(q_omp)
| thip['sdx6'].isin(q_omp)
| thip['sdx7'].isin(q_omp)
| thip['sdx8'].isin(q_omp)
| thip['sdx9'].isin(q_omp)
| thip['sdx10'].isin(q_omp)
]

q_gas = ['Q793']
gas = thip.loc[thip['pdx'].isin(q_gas)
| thip['sdx1'].isin(q_gas)
| thip['sdx3'].isin(q_gas)
| thip['sdx4'].isin(q_gas)
| thip['sdx5'].isin(q_gas)
| thip['sdx6'].isin(q_gas)
| thip['sdx7'].isin(q_gas)
| thip['sdx8'].isin(q_gas)
| thip['sdx9'].isin(q_gas)
| thip['sdx10'].isin(q_gas)
]

q_cdh = ['Q790']
cdh = thip.loc[thip['pdx'].isin(q_cdh)
| thip['sdx1'].isin(q_cdh)
| thip['sdx3'].isin(q_cdh)
| thip['sdx4'].isin(q_cdh)
| thip['sdx5'].isin(q_cdh)
| thip['sdx6'].isin(q_cdh)
| thip['sdx7'].isin(q_cdh)
| thip['sdx8'].isin(q_cdh)
| thip['sdx9'].isin(q_cdh)
| thip['sdx10'].isin(q_cdh)
]

#Count by groups

eso_year = esop.groupby(['g_year'])['g_year'].count().to_list()
duo_year = duo.groupby(['g_year'])['g_year'].count().to_list()
small_year = small.groupby(['g_year'])['g_year'].count().to_list()
hscr_year = hscr.groupby(['g_year'])['g_year'].count().to_list()
arm_year = arm.groupby(['g_year'])['g_year'].count().to_list()
omp_year = omp.groupby(['g_year'])['g_year'].count().to_list()
gas_year = gas.groupby(['g_year'])['g_year'].count().to_list()
cdh_year = cdh.groupby(['g_year'])['g_year'].count().to_list()

#Find crude incidence per live birth

live_birth = [656571, 628450, 596736, 569338]

eso_inc = [i*10000 / j for i, j in zip(eso_year, live_birth)]
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

eso_region = esop.groupby(['health_region'])['health_region'].count().to_list()
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




