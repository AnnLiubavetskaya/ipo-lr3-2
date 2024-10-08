first_num = float(input("Введите первое число для сравнения:"))
second_num = float(input("Введите второе число для сравнения:"))
if first_num > second_num:
    print(f"второе число является наименьшим ({second_num})")
elif second_num > first_num :
    print(f"первое число является наименьшим ({first_num})")
else:
    print(f"первое число равняется второму ({first_num}={second_num})")
