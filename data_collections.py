# A daļa - Saraksti
  ## Izveido sarakstu; pievieno elementu ar .append(), dzēš ar .pop()
   ### Saraksts (List)
empty_list = []
print(empty_list)
print(len(empty_list))
List_1 = [1,3,5,8,9,10]
print(List_1)
print(len(List_1))
   ### Pievienošana sarakstam (append)
List_1.append(15)
print(List_1)
   ### Elementu noņemšana no saraksta (pop)
izņemtais_elements = List_1.pop(2)
print("Izņemtais elements:", izņemtais_elements)
print(List_1)
  ## Aprēķina saraksta summu un vidējo vērtību ar 'for' ciklu 
Summa = 0
Skaits = 0
for skaitlis in List_1:
    Summa += skaitlis
    Skaits += 1
videjais = Summa/Skaits
print("Summa:", Summa)
print("Vidējais:", videjais)
  ## Filtrē sarakstu: izveido jaunu sarakstu tikai ar pāra skaitļiem (for + if)
para_sk = []
for x in List_1:
    if x % 2 == 0:
        para_sk.append(x)
print("Pāra skaitļi:", para_sk) 
  ## Šķēlums (slice)
print(List_1[:3]) ### Pirmie 3
print(List_1[-2:]) ### Pēdējie 2
print(List_1[::2]) ### katrs otrais elements
# B daļa — Vārdnīcas
  ## Izveido vārdnīcu ar 3+ studentiem
empty_dict = {} 
print(empty_dict)
print(len(empty_dict))
studenti = {  
    "Aiga": 92, 
    "Žanis": 85, 
    "Inna": 72, 
    "Artūrs": 100
}
print("Studentu balles:")
for vārds, balle in studenti.items():
    print(f"{vārds}: {balle}")
studenti["Baiba"] = 82
print("Aktuāls studentu saraksts:")
print(studenti)
studenti["Inna"] = 79
print(f"\nBaibas balle: {studenti.get('Baiba', 'Nav atrasts')}")
print(f"\nInnas balle: {studenti.get('Inna', 'Nav atrasts')}")
print("Studentu saraksts un balles:")
for vārds, balle in studenti.items():
    print(f"{vārds}: {balle}")
max_balle = -1
best_vārds = ""
for vārds, balle in studenti.items():
    if balle > max_balle:
        max_balle = balle
        best_vārds = vārds
print(f"Students ar augstāko atzīmi: {best_vārds} ({max_balle})!")   
# C daļa — Kombinācija
  ## Izveido sarakstu ar vārdnīcām
empty_dict_list = []
print(empty_dict_list)
studentu_saraksts = [
    {"name": "Aiga", "grade": 92},
    {"name": "Žanis", "grade": 85},
    {"name": "Inna", "grade": 79},
    {"name": "Artūrs", "grade": 100},
    {"name": "Baiba", "grade": 82}
]
print("Studentu saraksts:")
print(studentu_saraksts)
for studenti in studentu_saraksts:
    name = studenti["name"]
    grade = studenti["grade"]
    print(f"{name}: {grade}")
  ## Filtrē: tikai studenti ar atzīmi >= 80
top_studenti = []
for studenti in studentu_saraksts:
    if studenti["grade"] >= 90:
        top_studenti.append(studenti)
print("Labākie studenti:")
print(top_studenti)
for indekss, studenti in enumerate(top_studenti, start=1):
    print(f"{indekss}. {studenti['name']} — {studenti['grade']}")