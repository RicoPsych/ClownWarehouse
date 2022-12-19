from secrets import randbelow
import pandas
import datetime


T0 = datetime.date(1990,1,1)
T1 = datetime.date(2006,6,30)
T2 = datetime.date(2022,12,31)

dates = pandas.date_range(T0,T1,periods=3750) #,freq="M"
dates2 = pandas.date_range(T1,T2,periods=3750)

directors_name = [("Martin","Wilder"),("Anya","Holding"),("Annabella","Livingston"),("Kendal","Millington"),("Seamus","Howe")]
equipement_name = ["Armata","Trapez","Lina do chodzenia","Huśtawka","Szczudła",
"Miecz do Połykania","Olej Parafinowy","Kije Do żonglerki","Piłeczki do Żonglerki",
"Monocykl","Trampolina","Basen i Deska do Skakania","Skrzynia do przecinania ludzi"]
location_name = ["Gdańsk","Poznań","Warszawa","Kraków","Szczecin","Olsztyn","Frombork","Łódź","Lublin","Gdynia","Sopot","Białystok"]
act_name = ["Wystrzał z armaty","Sztuczki na trapezie","Chodzenie po linie","Huśtanie Ekstremalne","Chodzenie na szczudłach",
"Połykanie miecza","Plucie ogniem","Żonglerka Kijami","Żonglerka Kulami","Jazda na monocyklu","Wysokie skoki na trampolinie","Skoki do wody","Sztuczka z przecinaniem"]
act_desc = ["..."]
incidents_report = [["Brak"],["Złamana Ręka","Złamana noga","Rany cięte","Poparzenia","Skręcona kostka","Zwichnięta ręka"],["Złamanie","Przetarcie","Pęknięcie","Rozregulowanie"]]
producers = ["Yamaha","Klaunopol","Klaunex","Cyrkowo","Cyrkowe akcesoria","ClownStuff"]

art_name = ["Hubert","Paweł","Szymon","Ola","Ania","Adam"]
art_surname = ["Wiewór","Kojot","Kotek","Szczur","Mysz","Młot","Gracz","Klaunowski"]
art_pseud1 = ["Duży","Mały","Gruby","Czerwony","Czarny","Szary"]
art_pseud2 = ["Nos","Lis","Kot","Szop","Gibuś","Kangur","Grzyb","Żongler"]

#X - performance , 3x - acts act_eq act_art, 1.5x - incident , okolo 11.5 * ilość dat



class Performance:
    def __init__(self,id,art_dir_id,time,location):
        self.id = id
        self.art_dir_id = art_dir_id
        self.time = time
        self.location = location
    
    def SQL(self):
        txt = "INSERT INTO performances (id,artistic_director_id,time,location) VALUES ("
        txt += str(self.id)+ ","  
        txt += str(self.art_dir_id)+ ","
        txt += str(self.time)+ ","
        txt += "'" + str(self.location) + "'"
        txt += ");\n"
        return txt

class Act:
    def __init__(self,id,performance_id,id_accident,id_artist,id_eq,name,desc):
        self.id = id
        self.performance_id = performance_id
        self.name = name
        self.desc = desc
        self.accident_id = id_accident
        self.artist_id = id_artist 
        self.equipment_id = id_eq

    def SQL(self):
        txt = "INSERT INTO acts (id,performance_id,artist_id,accident_id,equipment_id,name,description) VALUES ("
        txt += str(self.id)+ ","  
        txt += str(self.performance_id)+ ","
        txt += str(self.artist_id)+ ","

        txt += str(self.accident_id)+ ","

        txt += str(self.equipment_id)+ ","

        txt += "'" + str(self.name)+ "',"
        txt += "'" + str(self.desc) + "'"
        txt += ");\n"
        return txt

class Act_eq:
    def __init__(self,eq_id,act_id):
        self.eq_id = eq_id
        self.act_id = act_id

    def SQL(self):
        txt = "INSERT INTO act_equipement (equipement_id,act_id) VALUES ("
        txt += str(self.eq_id)+ ","  
        txt += str(self.act_id)
        txt += ");\n"
        return txt

class Equipement:
    def __init__(self,id,name,producer):
        self.id = id
        self.name = name
        self.producer = producer

    def SQL(self):
        txt = "INSERT INTO equipment (id,name,producer) VALUES ("
        txt += str(self.id)+ ","  
        txt += "'" + str(self.name)+ "',"
        txt += "'" + str(self.producer)+ "'"

        txt += ");\n"
        return txt

class Act_artist:
    def __init__(self,artist_id,act_id):
        self.artist_id = artist_id
        self.act_id = act_id

    def SQL(self):
        txt = "INSERT INTO artist_act (artist_id,act_id) VALUES ("
        txt += str(self.artist_id)+ ","  
        txt += str(self.act_id)
        txt += ");\n"
        return txt

class Artist:
    def __init__(self,id,name,surname,pseudonym):
        self.id = id
        self.name = name
        self.surname = surname
        self.pseudonym = pseudonym

    def SQL(self):
        txt = "INSERT INTO artists (id,name,surname,pseudonym) VALUES ("
        txt += str(self.id)+ ","          
        txt += "'" + str(self.name)+ "',"
        txt += "'" + str(self.surname)+ "',"
        txt += "'" + str(self.pseudonym) + "'"
        txt += ");\n"
        return txt

class Incident:
    def __init__(self,id,type,report):
        self.id = id
        self.type = type
        self.report = report
        #self.act_id = act_id
    
    def SQL(self):
        txt = "INSERT INTO accidents (id,type,report) VALUES ("
        txt += str(self.id)+ ","          
        txt +=  str(self.type)+ ","
        txt += "'" + str(self.report)+ "',"
        #txt += str(self.act_id) 
        txt += ");\n"
        return txt

class Artistic_director:
    def __init__(self,id,name,surname):
        self.id = id
        self.name = name
        self.surname = surname
    
    def SQL(self):
        txt = "INSERT INTO artisitc_directors (id,name,surname) VALUES ("
        txt += str(self.id)+ ","          
        txt += "'" + str(self.name)+ "',"
        txt += "'" + str(self.surname)+ "'"
        txt += ");\n"
        return txt


directors = []
artists = []
equipement = []


performances =[[],[]]
acts = [[],[]]

eq_acts = [[],[]]
art_acts = [[],[]]
injuries = []


##Dyrektorzy
i = 0
for dir in directors_name:
    directors.append(Artistic_director(i,dir[0],dir[1]))
    i+= 1
##Ekwipunek
i = 0
for eq in equipement_name:
    equipement.append(Equipement(i,eq,producers[randbelow(len(producers))]))
    i+= 1

##Artyści
i = 0
for name in range(6):
    for surname in range(8):
        artists.append(Artist(i,art_name[name],art_surname[surname],art_pseud1[name]+" "+art_pseud2[surname]))
        i+=1
##Wypadki
i= 0
for type in range(3):
    for report in incidents_report[type]:
        injuries.append(Incident(i,type,report))
        i+=1


##Tworzenie występów

i = 0
for date in dates:
    date: datetime.date
    performances[0].append(Performance(i,randbelow(len(directors)),"'"+date.strftime("%Y-%m-%d")+"'" ,location_name[randbelow(len(location_name))]))
    i+=1

for date in dates2:
    date: datetime.date
    performances[1].append(Performance(i,randbelow(len(directors)),"'"+date.strftime("%Y-%m-%d")+"'" ,location_name[randbelow(len(location_name))]))
    i+=1


##Tworzenie pliku csv 
i = 0
x = 0
for zzz in range(2):

    file = open("Survey"+str(zzz)+".csv","w")
    txt = "Id,Name,Survey nr,id1,avg1,id2,avg2,id3,avg3\n"

    
    for performance in performances[zzz]: 
        performance : Performance
        
        txt+= str(performance.id) +",placeholder," + str(randbelow(3000))

        for xx in range(3): 
            random_nr = randbelow(len(act_name))
            ##Akty
            acts[zzz].append(Act(i,performance.id, randbelow(len(injuries)) ,randbelow(len(artists)),random_nr,act_name[random_nr],act_desc[0]))
            #eq_acts[zzz].append(Act_eq(random_nr,i))
            #art_acts[zzz].append(Act_artist(randbelow(len(artists)),i))
            #injuries
            txt+= ","+str(i)+"," + str(randbelow(1000)/100)

            i+=1
        txt+="\n"


    file.write(txt)
    file.close()
    print("csv"+str(zzz))

#dodać 1 okres czasowy

file = open("SQL_Queries.sql","w")
txt = ""
for x in directors:
    txt+= x.SQL()
txt+="\n"

for x in artists:
    txt+= x.SQL()
txt+="\n"

for x in equipement:
    txt+= x.SQL()
txt+="\n"

for x in injuries:
    txt+= x.SQL()


for x in performances[0]:
    txt+= x.SQL()
txt+="\n"

for x in acts[0]:
    txt+= x.SQL()
txt+="\n"

# for x in eq_acts[0]:
#     txt+= x.SQL()
# txt+="\n"

# for x in art_acts[0]:
#     txt+= x.SQL()
# txt+="\n"



file.write(txt)
file.close()

print("sql1")
#drugi okres czasowy

file = open("SQL_Queries2.sql","w")
txt = "Update equipment set producer = 'Yamaha' where id = 3;\nUpdate equipment set producer = 'Yamaha' where id = 2;\nUpdate performances set location='Sopot' where id = 12433;\nUpdate artists set surname='Grzegorzewicz' where id = 15;\n"


for x in performances[1]:
    txt+= x.SQL()
txt+="\n"

for x in acts[1]:
    txt+= x.SQL()
txt+="\n"

for x in eq_acts[1]:
    txt+= x.SQL()
txt+="\n"

for x in art_acts[1]:
    txt+= x.SQL()

txt+="\n"


file.write(txt)
file.close()
print("X")