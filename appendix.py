from bs4 import BeautifulSoup
import requests
import sqlite3
con = sqlite3.connect('eq.db')
con = sqlite3.connect(r"I:\Dev\JMA-data\eq.db")
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS appendix (
        "district"	TEXT,
	"district_number"	INTEGER,
	"region_number"	INTEGER UNIQUE,
	"region"	REAL,
	PRIMARY KEY("region_number")
        
    )
''')

f = open("demofile2.txt", "a")
f.write("District,District Number,Region Number,Region \n")
for x in range(1,9):
    print(x)
    url = f"https://www.data.jma.go.jp/eqev/data/bulletin/catalog/appendix/regname{x}_e.html"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    district = soup.find('caption')

    print(f"Paragraph: {district.text}")

    district_number = soup.find('td')
    region_number = soup.find_all('td')[1::2]
    region_name = soup.find_all('td')[2::2]
    
    
    for i, p in enumerate(region_name, 0):
        print(f'"{district.text}",{district_number.text},{region_number[i].text}, {region_name[i].text}')
        f.write(f'"{district.text}",{district_number.text},{region_number[i].text}, {region_name[i].text} \n')
        cursor.execute("INSERT INTO appendix (district, district_number,region_number,region) VALUES (?, ?, ?,? )",
            (district.text, district_number.text, region_number[i].text,region_name[i].text))

con.commit()