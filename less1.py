a = int(input("Введите число А: "))
b = int(input("Ввелите число В: "))
if b == a*a:
    print(f"{b} Является квадратом {a}")
elif a == b*b:
    print(f"{a} Является кадратом {b}")
else:
    print(f"{a} Не является квадратом {b}")