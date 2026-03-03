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