a = input("у тебя дебитовая карта или кредитка?")
if a == "кредитка":
    print("хорошо")
else:
    print("тогда пока")
    quit()

a = input("какой у неё номер?")
if a.isdigid() and len(a) < 16:
    print("хорошо")
else:
    print("тогда пока")
    quit()

a = input("какой у неё код безопасности")
if a.isdigid() and len(a) < 4:
    print("хорошо")
else:
    print("тогда пока")
    quit()

print("удачи выплачивать кредит")