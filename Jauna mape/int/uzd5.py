#uzd

"""
Lietotājs ievada 2 skaitļus, jāizveido programma, kas šos skaitļus salīdzina,
izveidojot funkciju ar diviem parametriem.
"""

def noteikt_skaitlus(skaitlis1 , skaitlis2 ):
   if skaitlis1>0 and skaitlis2>0: 
      return "abi pozitīvi"
    elif skaitlis1<0 and skaitlis2<0:
      return "Abi negatīvi"
    elif skaitlis1==0 or skaitlis2==0:
     return "vismaz 1 ir sk ir 0"
    else:
        return "skatļi ir ar dažām zīmēm"

sk1=int(input("ievadi 1.sk"))
sk2=int(input("ievadi 2.sk"))
rezultats=noteikt_skaitlus(sk1, sk2)
