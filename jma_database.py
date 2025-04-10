import streamlit as st
import pandas as pd 
import numpy as np
import sqlite3
import os
from jma_database_make import makedb

st.title("JMA Earthquakes")
st.caption("Warning will be very slow if selecting more than 3 Years")
#TODO add damage? 
#TODO add depth? 

#TODO mag class needs to be updated to include B and C levels somhow and negitive numbers










check = os.listdir("./")
if "eq.db" in check:
    
    pass
else:
    st.write("Database not found, makeing database...")
    makedb()
    st.write("Database made! Please refresh")


con = sqlite3.connect(r"eq.db")
cursor = con.cursor()

#getting years for selectbox 
q = f"SELECT year FROM years"  
years = pd.read_sql_query(q, con)
year_select = st.multiselect("Year(s)",years)




q = f"SELECT * FROM appendix"  
df = pd.read_sql_query(q, con)

districts = df['district'].unique().tolist()

district_pairs = df[['district_number', 'district']].drop_duplicates()
district_dict = dict(zip(map(str, district_pairs['district_number']), district_pairs['district']))

 
#create columns
col1,col2 = st.columns(2)
#create select button
select = col1.radio( "Filter Type",["Magnitude","Intensity"])


#this is to put placeholders in the query depending on number of years selected 
placeholders = ','.join('?' * len(year_select))


if select == "Magnitude":
    mag_select = col2.multiselect("Magnitude", ["0", "1", "2", "3", "4", "5", "6", "7"], "0")
    
    
    mag_conditions = []
    for mag in mag_select:
        lower_bound = float(mag)
        upper_bound = float(mag) + 0.9
        mag_conditions.append("magnitude BETWEEN ? AND ?")
    
   
    mag_where_clause = " OR ".join(mag_conditions) if mag_conditions else "1=1"
    

    q = f"""
        SELECT magnitude, latitude, longitude, district_name, area_name, mag_scaled, color 
        FROM earthquake 
        WHERE year IN ({placeholders})
        AND ({mag_where_clause})
    """
    
   
    params = year_select
    for mag in mag_select:
        params.append(float(mag))       
        params.append(float(mag) + 0.9)  
    
    filtered = pd.read_sql_query(q, con, params=params)
    
else:
    
    st.caption("A: Five lower B: Five upper C: Six lower D: Six upper")
    intensity_select = col2.multiselect("Intensity",[" ","1","2","3","4","5","6","7","A","B","C","D"])
    placeholders_i = ','.join('?' * len(intensity_select))
    
    q = f"""
    SELECT intensity, latitude, longitude,district_name,area_name,mag_scaled,color FROM earthquake 
    WHERE  year IN ({placeholders})
    AND intensity IN ({placeholders_i})

"""
   
    params = year_select + intensity_select 
    
    filtered = pd.read_sql_query(q, con, params=params)
    
    #filtered = filtered[filtered['intensity'].isin(intensity_select)]

col5, col6 = st.columns(2)
 


checkbox_district  = col1.checkbox("Filter By District")

if checkbox_district:
    district_select =  col5.selectbox("District",districts)
    filtered = filtered[filtered['district_name'].str.strip() == district_select.strip()]

    select_regions = filtered['area_name'].unique().tolist()
    checkbox_region  = col2.checkbox("Filter By Region")
    
    if checkbox_region:
        region_select = col6.selectbox("Region",select_regions)
        filtered = filtered[filtered['area_name'].str.strip() == region_select.strip()]
        
    



st.map(
    filtered,
    latitude="lat",
    longitude="lon",
    size="mag_scaled",
    color="color"
)

