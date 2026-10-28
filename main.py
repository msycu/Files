
A = float(input("Введите начало интервала: "))
while True:
    B = float(input("Введите конец интервала: "))
    if B>A:
        break
    print("Конец не может быть меньше начала")
while True:
    r = float(input("Введите шаг табулирования: "))
    if 0 < r <=B-A:
        break
    print("Шаг табулированя должен быть больше нуля и меньше длиныинтервала. Повторите")
while True:
    eps = float(input("Введите точность вычисления 0 < eps < 1): "))
    if 0 < eps < 1:
        break
    print(f"Не правильный ввод 0 < eps < 1!!! \n Введите еще раз")
def f(x, e):
    a=2.0/3.0
    s=0
    n=1
    while True:
        s = s + a
        n = n + 1
        s_n=((x**2)*n*(2*n-1))/(((2*n)+1)*(n+1)*(n-1))
        a=a*s_n
        if abs(a) < e:
            break
    return s

dat = [["x","f(x)"]]
print("|" + "-"*10 + "+"+"-"*20 + "|")
print(f"|{dat[0][0]:^10}|{dat[0][1]:^20}|")
i = A
while True:
    print(f"|{i:^10.2g}|{f(i,eps):^20.13g}|")
    if A >= B:
        break
    A = A + r
    i = i + r
print("|" + "-"*10 + "+"+"-"*20 + "|")
