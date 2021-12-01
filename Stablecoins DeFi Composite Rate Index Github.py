# This only draws data from today. For a graph that includes multiple data points, you only need to store the desired data on a daily basis. 

# This version unfortunately only includes the stablecoins DAI, USDT and USDC. In addition, it is important to know that only the borrow rate is available via Defipulse's free API. When evaluating skew.com "skew. Stablecoin DeFi Composite Index", the borrow and lending rates are included. However, the result should be the same and helps to assess whether there is currently a high demand for stablecoins. 

# However, I am well aware that the metrics from Nansen.ai are much more helpful with regard to stablecoins. I just wanted to offer something in exchange for your top 3 cryptocurrencies for the next bear market.  


import io
import json
import pandas as pd
import requests
import time
import datetime as dt
import datetime
from time import sleep


API_KEY = "" #API key from defipulse    
#token = "DAI"
r = requests.get("https://data-api.defipulse.com/api/v1/defipulse/api/GetRates?", 
        params={
            'api-key': API_KEY,
            "token": "DAI"
        }
)


print(r.status_code)
df = pd.DataFrame(json.loads(r.content.decode()))

df = df.T

df = df.reset_index()


for col in df.columns:
    print(col)

df = df.rename({'Aave V1': "AaveV1", 'Aave V2': 'AaveV2'}, axis=1)


##################
##################
#DAI
##################
##################


## Get Compound data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_Compound'] = df.Compound.apply(get_usdt, which="borrow")
df['supply_Compund'] = df.Compound.apply(get_supply)

## Get Compound data - finished 


## Get Aave V1 data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV1'] = df.AaveV1.apply(get_usdt, which="borrow")
df['supply_AaveV1'] = df.AaveV1.apply(get_supply)

## Get Aave V1 data - finished 


## Get Aave V2 data

def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV2'] = df.AaveV2.apply(get_usdt, which="borrow")
df['supply_AaveV2'] = df.AaveV2.apply(get_supply)

df.to_csv('lending_DAI.csv', index=False)

## Get Aave V2 data

selected_columns = df[["borrow_rate_Compound","supply_Compund","borrow_rate_AaveV1","supply_AaveV1","borrow_rate_AaveV2","supply_AaveV2"]]

DAI_onecolumn = selected_columns.copy()
print(DAI_onecolumn)

DAI_onecolumn = DAI_onecolumn.iloc[1:]

DAI_onecolumn['date'] = datetime.date.today()


##################
##################
#DAI - Finished
##################
##################

##################
##################
#USDT
##################
##################

#token = "USDT"
r = requests.get(
        "https://data-api.defipulse.com/api/v1/defipulse/api/GetRates?", 
        params={
            'api-key': API_KEY,
            "token": "USDT"
        }
)


print(r.status_code)
df = pd.DataFrame(json.loads(r.content.decode()))

df = df.T

df = df.reset_index()


for col in df.columns:
    print(col)

df = df.rename({'Aave V1': "AaveV1", 'Aave V2': 'AaveV2'}, axis=1)

## Get Compound data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_Compound'] = df.Compound.apply(get_usdt, which="borrow")
df['supply_Compund'] = df.Compound.apply(get_supply)


## Get Compound data - finished 


## Get Aave V1 data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV1'] = df.AaveV1.apply(get_usdt, which="borrow")
df['supply_AaveV1'] = df.AaveV1.apply(get_supply)


## Get Aave V1 data - finished 


## Get Aave V2 data

def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV2'] = df.AaveV2.apply(get_usdt, which="borrow")
df['supply_AaveV2'] = df.AaveV2.apply(get_supply)

df.to_csv('lending_USDT.csv', index=False)

## Get Aave V2 data

selected_columns = df[["borrow_rate_Compound","supply_Compund","borrow_rate_AaveV1","supply_AaveV1","borrow_rate_AaveV2","supply_AaveV2"]]

USDT_onecolumn = selected_columns.copy()
print(USDT_onecolumn)

USDT_onecolumn = USDT_onecolumn.iloc[1:]

USDT_onecolumn['date'] = datetime.date.today()


##################
##################
#USDT - Finished
##################
##################

##################
##################
#USDC
##################
##################

#token = "USDC"
time.sleep(1)
r = requests.get(
        "https://data-api.defipulse.com/api/v1/defipulse/api/GetRates?", 
        params={
            'api-key': API_KEY,
            "token": "USDC"
        }
)


time.sleep(1)
print(r.status_code)
df = pd.DataFrame(json.loads(r.content.decode()))

df = df.T

df = df.reset_index()


for col in df.columns:
    print(col)

df = df.rename({'Aave V1': "AaveV1", 'Aave V2': 'AaveV2'}, axis=1)

## Get Compound data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_Compound'] = df.Compound.apply(get_usdt, which="borrow")
df['supply_Compund'] = df.Compound.apply(get_supply)

## Get Compound data - finished 


## Get Aave V1 data


def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV1'] = df.AaveV1.apply(get_usdt, which="borrow")
df['supply_AaveV1'] = df.AaveV1.apply(get_supply)

## Get Aave V1 data - finished 


## Get Aave V2 data

def get_usdt(r, which="borrow"):
    try:
        return r[which]['rate']
    except:
        return 0

def get_supply(r):
    try:
        return r['supply']
    except:
        return 0

df['borrow_rate_AaveV2'] = df.AaveV2.apply(get_usdt, which="borrow")
df['supply_AaveV2'] = df.AaveV2.apply(get_supply)

df.to_csv('lending_USDC.csv', index=False)

## Get Aave V2 data

selected_columns = df[["borrow_rate_Compound","supply_Compund","borrow_rate_AaveV1","supply_AaveV1","borrow_rate_AaveV2","supply_AaveV2"]]

USDC_onecolumn = selected_columns.copy()
print(USDC_onecolumn)

USDC_onecolumn = USDC_onecolumn.iloc[1:]

##################
##################
#USDC - Finished
##################
##################


##########################################
##########################################
# Combine all stablecoin data
##########################################
##########################################

All_Together=DAI_onecolumn.append(USDT_onecolumn,ignore_index=True)

All_Together=All_Together.append(USDC_onecolumn,ignore_index=True)


Total_supply_Compund = All_Together['supply_Compund'].sum()

Total_supply_AaveV1 = All_Together['supply_AaveV1'].sum()

Total_supply_AaveV2 = All_Together['supply_AaveV2'].sum()


All_Together["supply_Compund_multipliedwith_borrow_rate_Compound"] = All_Together["supply_Compund"] * All_Together["borrow_rate_Compound"]

All_Together["supply_AaveV1_multipliedwith_borrow_rate_AaveV1"] = All_Together["supply_AaveV1"] * All_Together["borrow_rate_AaveV1"]

All_Together["supply_AaveV2_multipliedwith_borrow_rate_AaveV2"] = All_Together["supply_AaveV2"] * All_Together["borrow_rate_AaveV2"]


All_Together_Compund = All_Together["supply_Compund_multipliedwith_borrow_rate_Compound"].sum()

All_Together_AAve1 = All_Together["supply_AaveV1_multipliedwith_borrow_rate_AaveV1"].sum()

All_Together_AAve2 = All_Together["supply_AaveV2_multipliedwith_borrow_rate_AaveV2"].sum()


CompositeBid_Compound = All_Together_Compund / Total_supply_Compund

CompositeBid_AAVE1 = All_Together_AAve1 / Total_supply_AaveV1

CompositeBid_AAVE2 = All_Together_AAve2 / Total_supply_AaveV2


Total_supply = Total_supply_Compund + Total_supply_AaveV1 + Total_supply_AaveV2


Total_supply_Compund_Perc = Total_supply_Compund / Total_supply

Total_supply_AaveV1_Perc = Total_supply_AaveV1 / Total_supply

Total_supply_AaveV2_Perc = Total_supply_AaveV2 / Total_supply


CompositeBid = Total_supply_Compund_Perc * CompositeBid_Compound + Total_supply_AaveV1_Perc * CompositeBid_AAVE1 + Total_supply_AaveV2_Perc * CompositeBid_AAVE2

CompositeBid_df = pd.DataFrame([CompositeBid], columns=['Composite Bid'])

CompositeBid_df['date'] = datetime.date.today()



#CompositeBid_df_yesterday = pd.read_csv (r'CompositeBid_df_yesterday.csv')

#CompositeBid_df_new=CompositeBid_df_yesterday.append(CompositeBid_df,ignore_index=False)

#CompositeBid_df_new.to_csv('CompositeBid_df_yesterday.csv', index=False)


from glassnode import GlassnodeClient
from functools import reduce

gn = GlassnodeClient()
gn.set_api_key("Key of free API")

price_usd = gn.get('https://api.glassnode.com/v1/metrics/market/price_usd', a='BTC')

usd = pd.DataFrame({'date':price_usd.index, 'price':price_usd.values})

CompositeBid_df_new['date'] = CompositeBid_df_new['date'].astype('datetime64')

dfs = [CompositeBid_df_new, usd]

df_final = reduce(lambda left,right: pd.merge(left,right,on='date'), dfs)

df_final.to_csv('CompositeBid_df_yesterday_withprice.csv', index=False)

time.sleep(1)


from matplotlib import pyplot as plt    
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()

df_finalplot = df_final

df_finalplot["Composite Bid"] = df_finalplot["Composite Bid"] * 5000

df_finalplot.plot(kind='line',x='date',y='Composite Bid',ax=ax)
df_finalplot.plot(kind='line',x='date',y='price', color='red', ax=ax)

ax.set_ylim([0,70000])
ax.set_title('Stablecoins DeFi Composite Rate Index \n USDT - USDC - DAI')
ax.set_ylabel('Rate Index | Price BTC')

#plt.show()
plt.savefig('Stablecoins DeFi Composite Rate Index.png', dpi=100)
