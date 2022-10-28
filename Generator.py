from secrets import randbelow
import pandas
import datetime


T0 = datetime.datetime(2001,1,1)
T1 = datetime.datetime(2011,6,30)
T2 = datetime.datetime(2022,12,31)

dates = pandas.date_range(T0,T1,periods=20) #,freq="M"
print(dates)

directors = [("Martin","Wilder"),("Anya","Holding"),("Annabella","Livingston"),("Kendal","Millington"),("Seamus","Howe")]
equipement = ["Armata","Trapez","Lina do chodzenia","Huśtawka","Szczudła",
"Miecz do Połykania","Olej Parafinowy","Kije Do żonglerki","Piłeczki do Żonglerki",
"Monocykl","Trampolina","Basen i Deska do Skakania","Skrzynia do przecinania ludzi"]
location = ["Gdańsk","Poznań","Warszawa","Kraków","Szczecin","Olsztyn","Frombork","Łódź","Lublin","Gdynia","Sopot","Białystok"]
act_name = []
act_desc = []
incidents_report = ["Złamana Ręka","Złamana noga","Rany cięte","Poparzenia","Skręcona kostka","Zwichnięta ręka"]


class Performance:
    def __init__(self,id,art_dir_id,time,location):
        self.id = id
        self.art_dir_id = art_dir_id
        self.time = time
        self.location = location

class Act:
    def __init__(self,id,performance_id,name,desc):
        self.id = id
        self.performance_id = performance_id
        self.name = name
        self.desc = desc

class Act_eq:
    def __init__(self,eq_id,act_id):
        self.eq_id = eq_id
        self.act_id = act_id


class Equipement:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Act_artist:
    def __init__(self,artist_id,act_id):
        self.artist_id = artist_id
        self.act_id = act_id


class Artist:
    def __init__(self,id,name,surname,pseudonym):
        self.id = id
        self.name = name
        self.surname = surname
        self.pseudonym = pseudonym

class Incident:
    def __init__(self,id,type,report,act_id):
        self.id = id
        self.type = type
        self.report = report
        self.act_id = act_id


class Artistic_director:
    def __init__(self,id,name,surname):
        self.id = id
        self.name = name
        self.surname = surname


directors_c = []
performances =[]

i = 0
for dir in directors:
    directors_c.append(Artistic_director(i,dir[0],dir[1]))
    i+= 1

i = 0
for date in dates:
    performances.append(Performance(i,randbelow(len(directors_c)),date,location[randbelow(len(location))]))
    i+=1


    