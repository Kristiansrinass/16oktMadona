"""""
#dalības operātori iekš IF
# in, not in

burts="t"

if burts not in"Java":
    print("Jā!")
else:
    print("Nē!")

#un, vai izmanto IF
#and or

s=3000
t=1000

if 2>t and t%2 == 0: 
    print("Abi noteikumi izpildās!")
else:
    print("raw")

x=200
y=1000
if((x<y) or (y%11==0)):
    print("Viens no nsacijumiem izpildās")
"""""
#priekšraksts pass
x=100
y=4
if x<y:
    pass
print("labrīt!")