#cikla konstrukcijas

#1. for cikls ***iterācija***
"""
saraksts=[1,2,3,4,5]
for elements in saraksts:
    print(elements)

#2. cilks for apstrādājot skaitļu intervālu
a= int(input("ievadiet skaitli: "))
s=0
for i in range(1, a+1):
    s+=i
print(s)

#3. cikls for apstrādājot elementu kopumu
burti=["aka", "paka", "laka"]
for i in burti:
    print( "Sveiki," "+i+"!" )

#4. cikls ar priekšnosacijumu
s=0
a=int(input("skaitlis: "))
while a>0:
    s+=a #s=s+a
    a=int(input("Nākošais skaitlis: "))
print(s)

#while cikls izpildīs ciklu kamēr 
skaitlis=1
while skaitlis<=5:
    print(skaitlis)
    skaitlis+=1

#cikla pārtraukšana vai turpināšana
saraksts=[1,2,3,4,5]
for elements in saraksts:
    if elements==3:
        continue #Pārtrauc iterāciju un turpina ar nakamo
    if elements==5:
        break # iziet no cikla
    print(elements)

#Enumerate cikls
saraksts=['a','b','c']
for index, vertiba in enumerate(saraksts):
    print(f"Indekss ir: {index}, Vērtība: {vertiba}")

#uzd izdrukāt visus pāra skaitļus no 10 lidz 100 galapunktus ieskaitot
#1 risinājums
for skaitlis in range(10, 101):
    if skaitlis % 2==0:
        print(skaitlis)

#2. risinājums
for skaitlis in range(10,101,2):
    print(skaitlis)

#for cikls ar sarakstu apstrādi
saraksts=[10,20,30,40,50]
rezultats=[] # tukšs saraksts
for skaitlis in saraksts:
    rezultats.append(skaitlis*2)
print(rezultats)

#while cikls ar lietotāja ievadi
ievade='' #simbolu virkne ir tukša
while ievade !="iziet":
    ievade=input("ievadiet 'iziet', lai pārtrauktu!")
"""
#for cikls ar vairākiem sarakstiem /ZIP funkciju
vardi=["Anna", "Beta", "Gints"]
vecumi=[25,30,35]
for vards, vecums in zip(vardi, vecumi):
    print(f"{vards} ir {vecums} gadus vecs/veca")

