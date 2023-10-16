#Izvadiet skaitļus no 1 lidz 100
#kad rez sasniedz skaitli kas dalās ar 3 izvadiet "fizz"
# un katru reizi kad sasniedz skaitli kas dalās ar 5 izvadat "buzz"
# ja skaitlis dalas ar 3 un 5 izvadiet "fizzbuzz"

for skaitlis in range(1, 101):
    if skaitlis%3==0 and skaitlis%5==0:
        print("fizzbuzz")
    elif skaitlis%3==0:
        print("fizz")
    elif skaitlis%5==0:
        print("buzz")
    else:
        print("skaitlis")
