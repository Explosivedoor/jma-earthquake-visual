import streamlit as st
import pandas as pd 
import numpy as np
import sqlite3
import os
import wget
from zipfile import ZipFile
#NOTE 1997 is split into two files for some reason, downloaded mannually. 1967-1919 files span multiple years in just 4 files, also manually downloaded 
#TODO add files below just so they're there 
#Below is download and extracting the data commented out
"""for i in range(1982,2023):
    try:
        wget.download(f'https://www.data.jma.go.jp/eqev/data/bulletin/data/hypo/h{i}.zip')
        with ZipFile(f'h{i}.zip', 'r') as zip_ref:
            zip_ref.extractall(r"D:\Downloads\eqdata")
        os.remove(f'h{i}.zip')
    except Exception as e:
        print(e)
        continue"""

#TODO add damage? 
#TODO add depth? 




con = sqlite3.connect(r"eq.db")
cursor = con.cursor()


q = f"SELECT * FROM appendix"
df = pd.read_sql_query(q, con)

districts = df['district'].unique().tolist()
district_pairs = df[['district_number', 'district']].drop_duplicates()
district_dict = dict(zip(map(str, district_pairs['district_number']), district_pairs['district']))







#TODO mag class needs to be updated to include B and C levels somhow and negitive numbers
mag_class = {-1:-0.1,   9 :-0.9, "A0":-1.0,"A1":-1.1,"A2":-1.2,"A3":-1.3,"A4":-1.4,"A5":-1.5,"A6":-1.6,"A7":-1.7,"A8":-1.8
,"A9":-1.9, "B0":-2.0, "C0":-3.0}
color_scale = [
    "#FFFFFFFF",  # White
    "#FFC0CBFF",  # Pink
    "#00FF00FF",  # Green
    "#00FFFFFF",  # Cyan
    "#0000FFFF",  # Blue
    "#FFFF00FF",  # Yellow
    "#704214FF",  # Brown
    "#800080FF",  # Purple
    "#FFA500FF",  # Orange
    "#FF0000FF"   # Red
]
#This is to make the points bigger or smaller depending on the magnitute of the quake 
mag_scale = [
    100,  
    200,     
    300,    
    400,      
    500,    
    600,   
    700,   
    800,    
    900,  
    1000    
]


cursor.execute('''
    CREATE TABLE IF NOT EXISTS years (
        year INTEGER )
''')



cursor.execute('''
    CREATE TABLE IF NOT EXISTS earthquake (
        date TEXT, 
        time TEXT,
        latitude REAL,
        longitude REAL,
        magnitude REAL,
        intensity TEXT,
        area_code INTEGER,
        district INTEGER,
        district_name TEXT, 
        area_name TEXT, 
        color TEXT,
        mag_scaled REAL      
    )
''')

#this takes the data file and puts it into the database. It is done this way, as opposed to the way in the df only version, to conserve memory. 
file_list = os.listdir("eqdata")
for file in file_list:
    with open(f"eqdata\{file}", 'r') as doc:
        lines = doc.readlines()

    
    

        for line in lines: 
            #only from JMA
            if line[0] == "J":
                try:
                    
                    #get intensity 
                    inten = line[61]
                    
                  

                    
                    #try to see if there is an magnitute listed, makes it be eg. 2.3, if not it is 0. There are codes in places for negitive values which start with a letter A1 B2 or a -. currently just positive magnitutes 
                    #TODO fix mag_class
                    try:
                        mag = float(f'{line[52]}.{line[53]}')
                        
                    except Exception as e:
                        #edge case where magnitude is missing 
                        mag = f'{line[52]}{line[53]}'
                        if mag == '  ':
                            mag = 0
                        #TODO fix this to make it have all negatives     
                        else:
                            mag = mag_class[f'{line[52]}{line[53]}']
                            
                                
                                
                    

                    #Area name, damage classification and lat and lon min 
                    area = line[68:92] 
                    damage = line[62]
                    lat_min = float(line[21:24])
                    lon_min = float(line[33:36])
                
                    #from 1983-1995 there are only 3 digits of percision for lat and lon sec, also some data is just missing from 1919-1982


                    try:
                        lat_sec = line[24:28].strip()
                        if len(lat_sec) == 4:

                            lat_sec = round(float(lat_sec)/6000,3)
                        else:
                            lat_sec = round(float(lat_sec)/600,3)
                    except:
                        continue
                        
                    
                    try:
                        lon_sec = line[36:40].strip()
                        if len(lon_sec) == 4:
                            lon_sec = round(float(lon_sec)/6000,3)            
                        else:
                            lon_sec = round(float(lon_sec)/600,3)
                        
                    except:
                        
                        continue



                    lat = lat_min + lat_sec
                    lon = lon_min + lon_sec        
                    
                    
                    year = line[1:5] 
                    month = line[5:7] 
                    day = line[7:9] 
                    #made this way for database
                    date = f"{year}-{month}-{day}"
                    hour = line[9:11] 
                    minute = line[11:13] 
                    second = line[13:15] 
                    #this is ignoring the hundreths of a second 
                    time = f"{hour}:{minute}:{second}"
                    
                    
                    
                    
                    district_name = district_dict[line[64]]  
                    
                    
                    try:
                        cursor.execute("INSERT INTO earthquake (date, time, latitude,longitude,magnitude,intensity,area_code,district,district_name,area_name,color,mag_scaled) VALUES (?, ?,?, ?,?, ?, ?,?, ?, ?,?, ?)",
                            (date, time, lat,lon,mag,inten,line[65:68],line[64],district_name,area,color_scale[abs(int(mag))],mag_scale[abs(int(mag))]))
                        
                    except Exception as e:
                        print(e)
                except:
                    continue

#Basically this creates an index to help speed up pulling from the database 
cursor.execute("ALTER TABLE earthquake ADD COLUMN year INTEGER")
cursor.execute("UPDATE earthquake SET year = CAST(strftime('%Y', date) AS INTEGER)")
cursor.execute("CREATE INDEX idx_year ON earthquake(year)")
cursor.execute("""
    INSERT OR IGNORE INTO years (year)
    SELECT DISTINCT year FROM earthquake
""")

con.commit()