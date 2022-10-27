import pandas
import datetime


T0 = datetime.datetime(2001,1,1)
T1 = datetime.datetime(2011,6,30)
T2 = datetime.datetime(2022,12,31)

dates = pandas.date_range(T0,T1,freq="M",periods=2)
print(dates)

directors = [("","")]
equipement = ["Armata","Trapez","Lina do chodzenia","Huśtawka","Szczudła",
"Miecz do Połykania","Olej Parafinowy","Kije Do żonglerki","Piłeczki do Żonglerki",
"Monocykl","Trampolina","Basen i Deska do Skakania","Skrzynia do przecinania ludzi"]
act_name = []
act_desc = []
incidents_report = []