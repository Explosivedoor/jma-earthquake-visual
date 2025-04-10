# JMA Earthquake Visual using Streamlit 
For now you can run the jma_database.py with 
<code>streamlit run jma_database.py</code>




## JMA format for the data:
This an example of line of data from the JMA data file:<br> 

<code>J2021100722412305 014 353545 035 1400620 054 749912459D60W711B2 3 93CENTRAL CHIBA PREF       39K
 </code>
 J2021100722412305 includes agency, date and time in format AYYYYMMDDHHMMSSSS 

_014:  Standard error in time (Seconds) <br>
353545: Latitude (read as 35.3545)<br>
_035:  stadard error in latitude (minutes)<br>
1400620: Longitude (read as 140.0620)<br>
_054: stadard error in latitude (minutes)<br>
_7499: Depth in kilometers  (read as _74.99) <br>
124: stadard error in kilometers (read as 12.4) <br> 
59: Magnitude 1 (read as 5.9) Refer to the table below  for negative values <br> 
D: Magnitude type 1 Refer to the table below <br> 
60: Magnitude 2 <br> 
W: Magnitutde type 2 <br> 
7: Travel time table	<br> 
1: Hypocenter location precision	<br> 
1: Subsidiary information	<br> 
B: Maximum intensity	<br> 
2: Damage class	<br> 
_: Tsunami class	<br> 
3: District number	<br> 
_93: Region number	<br> 
CENTRAL CHIBA PREF------: Region name<br> 
_39: Number of stations<br> 
K: Hypocenter determination flag<br> 









<br> <br> 

## JMA's Hypocenter record format table: 
Taken from https://www.data.jma.go.jp/eqev/data/bulletin/data/format/hypfmt_e.html

<table class="data2">
        <tbody><tr>
          <th>Col.</th>
          <th>Type</th>
          <th>Item</th>
          <th>Description</th> </tr>
        <tr>
          <td><tt>01</tt></td>
          <td><tt>A1</tt></td>
          <td>Record type identifier</td>
          <td>Agency codes:<br> J: Hypocenter record determined by JMA<br> U: Hypocenter record determined by USGS<br> I: Hypocenter record determined by other international organizations (ISC, IASPEI, etc.)</td> </tr>
        <tr>
          <td><tt>02 – 05</tt></td>
          <td><tt>I4</tt></td>
          <td>Year</td>
          <td>Year of origin time (Japan Standard Time = UTC + 9 h; the same applies below.)</td> </tr>
        <tr>
          <td><tt>06 – 07</tt></td>
          <td><tt>I2</tt></td>
          <td>Month</td>
          <td>Month of origin time</td> </tr>
        <tr>
          <td><tt>08 – 09</tt></td>
          <td><tt>I2</tt></td>
          <td>Day</td>
          <td>Day of origin time</td> </tr>
        <tr>
          <td><tt>10 – 11</tt></td>
          <td><tt>I2</tt></td>
          <td>Hour</td>
          <td>Hour of origin time</td> </tr>
        <tr>
          <td><tt>12 – 13</tt></td>
          <td><tt>I2</tt></td>
          <td>Minute</td>
          <td>Minute of origin time</td> </tr>
        <tr>
          <td><tt>14 – 17</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Second</td>
          <td>Second of origin time<br>blank after the decimal point in case of fixed hypocenter</td> </tr>
        <tr>
          <td><tt>18 – 21</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Standard error (seconds)</td>
          <td>Standard error for origin time (seconds)<br>Blank when hypocenter is fixed, or when hypocenter of template event is adopted in the Matched filter method.</td> </tr>
        <tr>
          <td><tt>22 – 24</tt></td>
          <td><tt>I3</tt></td>
          <td>Latitude (degrees)</td>
          <td>Latitude of hypocenter (degrees)</td> </tr>
        <tr>
          <td><tt>25 – 28</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Latitude (minutes)</td>
          <td>Latitude of hypocenter (minutes)<br>blank after the decimal point in case of fixed hypocenter</td> </tr>
        <tr>
          <td><tt>29 – 32</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Standard error (minutes)</td>
          <td>Standard error for latitude (minutes)<br>Blank when hypocenter is fixed, or when hypocenter of template event is adopted in the Matched filter method.</td> </tr>
        <tr>
          <td><tt>33 – 36</tt></td>
          <td><tt>I4</tt></td>
          <td>Longitude (degrees)</td>
          <td>Longitude of hypocenter (degrees)</td> </tr>
        <tr>
          <td><tt>37 – 40</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Longitude (minutes)</td>
          <td>Longitude of hypocenter (minutes)<br>blank after the decimal point in case of fixed hypocenter</td> </tr>
        <tr>
          <td><tt>41 – 44</tt></td>
          <td><tt>F4.2</tt></td>
          <td>Standard error (minutes)</td>
          <td>Standard error for longitude (minutes)<br>Blank when hypocenter is fixed, or when hypocenter of template event is adopted in the Matched filter method.</td> </tr>
        <tr>
          <td rowspan="2"><tt>45 – 49</tt></td>
          <td><tt>F5.2</tt></td>
          <td rowspan="2">Depth (kilometers)</td>
          <td>Depth in kilometers (depth-free method)<br> The depth of focus is treated as an unknown variable.</td> </tr>
        <tr>
          <td><tt>I3, 2X</tt></td>
          <td>Depth in kilometers (depth-slice method)<br> The optimal solution is sought with different source depths.<br> Width of change: 10 km (1926 – 1960, 1967 – 1982)<br> Width of change: 20 km (1961 – 1966)<br> Width of change: 1 km (1983 – )<br> Hypocenters from before 1982 are being re-examined and relocated based on calculation<br> using the depth-free method or the 1 km-width depth-slice method.</td> </tr>
        <tr>
          <td><tt>50 – 52</tt></td>
          <td><tt>F3.2</tt></td>
          <td>Standard error (kilometers)</td>
          <td>Standard error for depth (kilometers)<br> Blank when depth is determined using the depth-slice method, or when hypocenter of template event is adopted in the Matched filter method.</td> </tr>
        <tr>
          <td><tt>53 – 54</tt></td>
          <td><tt>F2.1</tt></td>
          <td>Magnitude 1</td>
          <td>See magnitude type 1<br> When the magnitude is less than 0, this column is denoted as follows:<br> -0.1: -1&nbsp;&nbsp; -0.9: -9&nbsp;&nbsp; -1.0: A0<br> -1.9: A9&nbsp;&nbsp; -2.0: B0&nbsp;&nbsp; -3.0: C0</td> </tr>
        <tr>
          <td rowspan="4"><tt>55</tt></td>
          <td rowspan="4"><tt>A1</tt></td>
          <td rowspan="4">Magnitude type 1</td>
          <td>JMA magnitudes<br> J: M<sub>J</sub> — Local Meteorological Office magnitude<br> D: M<sub>D</sub> — Displacement magnitude<br> d: As per M<sub>D</sub>, but for two stations<br> V: M<sub>V</sub> — Velocity magnitude<br> v: As per M<sub>V</sub>, but for two or three stations</td> </tr>
        <tr>
          <td>Moment magnitudes<br> W: M<sub>W</sub> — When the Agency Code is J, moment magnitude is based on JMA's centroid moment tensor solution. Otherwise, moment magnitude is determined by JMA or another organization such as USGS.</td> </tr>
        <tr>
          <td>Other organizations' magnitudes<br> B: mb — USGS body wave magnitude<br> S: M<sub>S</sub> — USGS surface wave magnitude</td> </tr>
        <tr>
          <td>blank: Undetermined</td> </tr>
        <tr>
          <td><tt>56 – 57</tt></td>
          <td><tt>F2.1</tt></td>
          <td>Magnitude 2</td>
          <td>See magnitude 1</td> </tr>
        <tr>
          <td><tt>58</tt></td>
          <td><tt>A1</tt></td>
          <td>Magnitude type 2</td>
          <td>See magnitude type 1</td> </tr>
        <tr>
          <td><tt>59</tt></td>
          <td><tt>A1</tt></td>
          <td>Travel time table</td>
          <td>Type of travel time table
            <br> 1: Reported by Ichikawa and Mochizuki (1971), Hamada (1984) (hereafter 83A) and others
            <br> 2: Reported by Ichikawa (1978) (hereafter LL) (for the area far east of the Sanriku district)
            <br> 3: Tables reported by Ichikawa and Mochizuki (1971) and LL, or 83A and LL (for the area east of Hokkaido)
            <br> 4: Tables reported by Ichikawa and Mochizuki (1971) and LL, or 83A and LL (for southern parts of the Kurile Islands）
            <br> 5: Table reported by Ueno et al. (2002) (hereafter JMA2001)
            <br> 6: JMA2001 and LL (with the mesh interval of LL matched to that of JMA2001) (for southern parts of the Kurile Islands)
            <br> 7: JMA2001A for inland stations, JMA2020A for those within landward slopes, JMA2020B for those in outer-rise regions of the Japan Trench, and JMA2020C for those within the Nankai Trough area
            <br> Blank: Determined by other agencies
          <br>
          <br>The tables are used when a hypocenter is determined in these areas:
          <br>2: Far east of Sanriku
          <br>3: East of Hokkaido
          <br>4 or 6: Southern parts of the Kurile Islands
          <br>7: Tables corresponding to individual station locations used in hypocenter calculation
          </td>
          </tr>
        <tr>
          <td><tt>60</tt></td>
          <td><tt>A1</tt></td>
          <td>Hypocenter location precision</td>
          <td>Hypocenter location precision<br> 1: Depth-free method<br> 2: Depth-slice method<br> 3: Fixed depth<br> 4: Based on depth phase<br> 5: Based on S−P time<br> 7: Poor solution (before March 2016)<br> 8: Undetermined or not accepted<br> 9: Hypocenter fixed (of which the most close station)<br> M: Matched filter method</td> </tr>
        <tr>
          <td><tt>61</tt></td>
          <td><tt>A1</tt></td>
          <td>Subsidiary information</td>
          <td>Subsidiary information on event<br> 1: Natural earthquake<br> 2: Insufficient number of JMA stations<br> 3: Artificial event<br> 4: Eruption earthquake and others<br> 5: Low-frequency earthquake</td> </tr>
        <tr>
          <td><tt>62</tt></td>
          <td><tt>A1</tt></td>
          <td>Maximum intensity</td>
          <td>1: One<br> 2: Two<br> 3: Three<br> 4: Four<br> 5: Five (until September 1996)<br> 6: Six (until September 1996)<br> 7: Seven<br> A: Five lower<br> B: Five upper<br> C: Six lower<br> D: Six upper<br> R: Remarkable earthquake (shock felt over 300 km away) (until 1977)<br> M: Moderate earthquake (shock felt over 200 km away but not over 300 km away) (until 1977)<br> S: Small earthquake (shock felt over 100 km away but not over 200 km away) (until 1977)<br> L: Local earthquake (shock felt less than 100 km away) (until 1977)<br> F: Felt earthquake (until 1984)<br> X: Shock felt by some people but not by JMA observers (until September 1996)</td> </tr>
        <tr>
          <td><tt>63</tt></td>
          <td><tt>A1</tt></td>
          <td>Damage class</td>
          <td>Damage class (after Utsu)<br> 1: Slight damage (cracks on walls and ground)<br> 2: Light damage (damage to houses, roads, etc.)<br> 3: 2 – 19 fatalities or 2 – 999 houses destroyed<br> 4: 20 – 199 fatalities or 1,000 – 9,999 houses destroyed<br> 5: 200 – 1,999 fatalities or 10,000 – 99,999 houses destroyed<br> 6: 2,000 – 19,999 fatalities or 100,000 – 999,999 houses destroyed<br> 7: 20,000+ fatalities or 1,000,000+ houses destroyed<br> X: Injury or damage of unclear scale (until 1988)<br> Y: Injury and damage included in the grade for the preceding or following event (until 1988)</td> </tr>
        <tr>
          <td rowspan="2"><tt>64</tt></td>
          <td rowspan="2"><tt>A1</tt></td>
          <td rowspan="2">Tsunami class</td>
          <td>1923 – 1988 Tsunami class (after Utsu)<br> 1: Tsunami recorded by tidal gage but no damage caused<br> T: Tsunami generated</td> </tr>
        <tr>
          <td>1989 – Tsunami class (after Imamura and Iida, 1958)<br> Height/damage<br> 1: 50 cm/none<br> 2: 1 m/very slight damage<br> 3: 2 m/slight damage to coastal areas and vessels<br> 4: 4 – 6 m/human injury<br> 5: 10 – 20 m/damage along more than 400 km of coastline<br> 6: 30 m+/damage along more than 500 km of coastline</td> </tr>
        <tr>
          <td><tt>65</tt></td>
          <td><tt>I1</tt></td>
          <td>District number</td>
          <td>Number of epicenter location district based on <a href="../../catalog/appendix/appendix_e.html#REGION">Appendix 1.A.3 Geographical region names</a></td> </tr>
        <tr>
          <td><tt>66 – 68</tt></td>
          <td><tt>I3</tt></td>
          <td>Region number</td>
          <td>Number of epicenter location region</td> </tr>
        <tr>
          <td><tt>69 – 92</tt></td>
          <td><tt>A24</tt></td>
          <td>Region name</td>
          <td>Name of epicenter location region</td> </tr>
        <tr>
          <td><tt>93 – 95</tt></td>
          <td><tt>I3</tt></td>
          <td>Number of stations</td>
          <td>Number of stations contributing to hypocenter determination</td> </tr>
        <tr>
          <td rowspan="2"><tt>96</tt></td>
          <td rowspan="2"><tt>A1</tt></td>
          <td rowspan="2">Hypocenter determination flag</td>
          <td rowspan="2">K: High-precision hypocenters (Manual, closely examined)<br> S: Low-precision hypocenters (Manual, closely examined)<br> k: Middle-precision hypocenters (Manual)<br> s: Low-precision hypocenters (Manual)<br> A: Middle-precision hypocenters (Auto)<br> a: Low-precision hypocenters (Auto)<br> N: Undetermined or not accepted or fixed hypocenters<br> F: Far field<br> </td> </tr>
        <tr>
        </tr> </tbody></table>
