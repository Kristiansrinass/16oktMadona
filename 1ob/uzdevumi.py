"""""
#skaitļa negativitāte
skaitlis=int(input("ievadi skaitli: "))

#salīdzinu ievadito skaitli
if skaitlis>0: print ("skaitlis ir pozitīvs")
elif skaitlis<0: print("Skaitlis ir negatīvs")
else:print ("skaitlis ir nulle ")

#pāra vai neparā skaitlis
skaitlis=int(input("ievadi skaitli: "))
# % nosaka atlikumu 3/2 atlk.1 10/5 atl.0
if skaitlis %2==0:
    print("skaitlis ir pāra")
else:
    print("skaitlis ir nepāra")

#noteikt kura saitļu vērtība ir leilāka
skaitlis1=int(input("skaitlis1.:"))
skaitlis2=int(input("2.skaitlis: "))
if skaitlis1>skaitlis2:
    print(" skaitlis 1 ir lielāks")
elif skaitlis2>skaitlis1:
    print("skaitlis 2 lielāks")
else:
    print("skaitļi ir vienādi!")
"""""""""""
#vai dalās ar 3?
skaitlis1=int(input("skaitlis 1 :")) 
skaitlis2=3
if skaitlis1/skaitlis2:
    print("dalās")
else:
    print("nedalās")