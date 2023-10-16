
def validet_vardu(vards):
    if len(vards) <3:
     return "Vārds ir pārāk īss"
    elif len(vards)>20:
       return "Vārds ir pārāk garš"
    elif not vards.isalpha(): 
       return "vārds drīkst saturēt tik burtus"
    else:
       return "vārds ir derīgs"

ievade=input("ievadi savu vārdu")
rezultats=validet_vardu(ievade)
print(rezultats)