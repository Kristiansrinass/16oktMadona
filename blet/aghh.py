#ievada tekstu un aprēķina burtu un vardu skaitu tajā

#ievadītais teksts
teksts=input("Ievadiet tekstu: ")

#burtu skaitu apreķina kā zinas ka tas ir burts %aka
#isalpha()
burtuskaits=0
for burts in teksts:
    if burts.isalpha():
        burtuskaits+=1 #burtuskaits=burtuskaits+!

#sadalīt pa vardiem
vardi=teksts.split()
#apreķina vardu skaitu
varduskaits=len(vardi)
#izvadīt rezultatu
print(f"burtu skaits ir {burtuskaits}")
print(f"vardu skaits ir {varduskaits}")