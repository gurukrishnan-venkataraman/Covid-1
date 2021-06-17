#This modified version will check for available vaccination slots every minute and alert you with a ringtone

#Note: There could be some delay of updation of data in the backend systems from which this script is pulling the data

#*************Configuration***************************
numdays=14 # No. of days to monitor from today
dist_inp='Chennai' # refer district_mapping.csv for exact district name
age_limit=18 #put age_limit = 18 or age_limit = 45 or age_limit='' (for both)
vaccine_type = 'COVAXIN' #('COVAXIN'/'COVISHIELD'/'')
Dose = 0 #(0-both,1=1st only, 2-2nd only)
ringtone='tune.mp3'
#*****************************************************

import datetime
import json
import numpy as np
import requests
import pandas as pd
import streamlit as st
from copy import deepcopy
from streamlit import caching
from playsound import playsound
import time
# faking chrome browser
browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_mapping():
    df = pd.read_csv("district_mapping.csv")
    return df

def filter_column(df, col, value):
    df_temp = deepcopy(df.loc[df[col] == value, :])
    return df_temp

def filter_capacity(df, col, value):
    df_temp = deepcopy(df.loc[df[col] > value, :])
    return df_temp



mapping_df = load_mapping()

mapping_dict = pd.Series(mapping_df["district id"].values,
                         index = mapping_df["district name"].values).to_dict()

rename_mapping = {
    'date': 'Date',
    'min_age_limit': 'Minimum Age Limit',
    'available_capacity': 'Available Capacity',
    'available_capacity_dose1': 'Available Capacity for Dose1',
    'available_capacity_dose2': 'Available Capacity for Dose2',
    'vaccine': 'Vaccine',
    'pincode': 'Pincode',
    'name': 'Hospital Name',
    'state_name' : 'State',
    'district_name' : 'District',
    'block_name': 'Block Name',
    'fee_type' : 'Fees'
    }

st.title('CoWIN Vaccination Slot Availability')
st.info('The CoWIN APIs are geo-fenced so sometimes you may not see an output! Please try after sometime ')

# numdays = st.sidebar.slider('Select Date Range', 0, 100, 10)
unique_districts = list(mapping_df["district name"].unique())
unique_districts.sort()


DIST_ID = mapping_dict[dist_inp]

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=(x+1)) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

placeholder=st.empty()
hours_to_run=10
run_ind=0
sleep_time=60
while(run_ind<(hours_to_run*3600)):
    error=''
    final_df = None
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if (response.ok) and ('centers' in json.loads(response.text)):
            resp_json = json.loads(response.text)['centers']
            if resp_json is not None:
                df = pd.DataFrame(resp_json)
                if df.size>0:
                    df = df.explode("sessions")
                    df['min_age_limit'] = df.sessions.apply(lambda x: x['min_age_limit'])
                    df['vaccine'] = df.sessions.apply(lambda x: x['vaccine'])
                    df['available_capacity'] = df.sessions.apply(lambda x: x['available_capacity'])
                    df['available_capacity_dose1'] = df.sessions.apply(lambda x: x['available_capacity_dose1'])
                    df['available_capacity_dose2'] = df.sessions.apply(lambda x: x['available_capacity_dose2'])
                    df['date'] = df.sessions.apply(lambda x: x['date'])
                    df = df[["date", "available_capacity","available_capacity_dose1","available_capacity_dose2", "vaccine", "min_age_limit", "pincode", "name", "state_name", "district_name", "block_name", "fee_type"]]
                    if final_df is not None:
                        final_df = pd.concat([final_df, df])
                    else:
                        final_df = deepcopy(df)
            else:
                error="No rows in the data Extracted from the API"
    #     else:
    #         st.error("Invalid response")

    if (final_df is not None) and (final_df.size>0):
        final_df.drop_duplicates(inplace=True)
        final_df.rename(columns=rename_mapping, inplace=True)
        if age_limit!='':
            final_df = filter_column(final_df, "Minimum Age Limit", age_limit)
        if vaccine_type!='':
            final_df = filter_column(final_df, "Vaccine", vaccine_type)
        if Dose==0:
            final_df = filter_capacity(final_df, "Available Capacity", 0)
        if Dose==1:
            final_df = filter_capacity(final_df, "Available Capacity for Dose1", 0)
        if Dose==2:
            final_df = filter_capacity(final_df, "Available Capacity for Dose2", 0)


        table = deepcopy(final_df)
        table.reset_index(inplace=True, drop=True)
    else:
        error="Unable to fetch data currently, please try after sometime"
    with placeholder.beta_container():
        st.markdown('Last updated:\t'+ datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
        if error == '':
            st.table(table)
            len=final_df.size
            if(len>0):
                playsound(ringtone)
                playsound(ringtone)
                playsound(ringtone)
        else:
            st.error(error)
    time.sleep(sleep_time)
    run_ind=run_ind+sleep_time
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/bhattbhavesh91" target="_blank">Bhavesh Bhatt</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

