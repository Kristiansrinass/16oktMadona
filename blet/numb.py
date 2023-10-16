
#virknes ir masīvi
a="Lab"
print(a[1])
for x in "Lab":
    print(x)

#virknes len()
#len funkcija atgriež vrknes garumu
#kā pārbaudīt
a="pieci eiro"
print("eiro" in (a))

#virkņu sadalīšana
a="Primdiena"
print(a[2:5])#iegūstot rakstzīmes no 2. pozīcijas uz 5 pozīciju
print(a[:5]) #no sākuma lidz 5.poz
print(a[2:]) #iegūstot rakstzīmes no 2. poz lidz galam
#var negatīvos indeksus
print(a[-5:-2]) #die

#lietotājam ievadīt vārdu un pēc tam izvada to apgriezto vaidu
#izmantot ciklu un ... nu
vards=input("ievadi vārdu: ")

#kur glabāsies apgrieztais vārds?
apgriezts_vards='' #tukša virkne

#Jaiziet cauri simbolu virknes apgrieztā secība un katrs burts
#
for burts in vards[::-1]:
    apgriezts_vards=apgriezts_vards+burts

#izvadam apgriezto vārdu
print("apgrieztā versija ir: " + apgriezts_vards)
"""
            lauks
            01234
"""