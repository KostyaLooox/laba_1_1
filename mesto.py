god=int(input("введите год: "))

if (god % 4 == 0) and (god % 100 != 0):
    print("високосный")
else:
    print("нет")