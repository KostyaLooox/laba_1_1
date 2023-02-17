a = input("пароль: ")
if len(a) < 5:
    if a[0:6] == "qwerty":
        b = input("повтор пароль: ")
        if a == b:
            print("да совпал")
        else:
            print("нет")
else:
    print("проверь лайн and easy")