nome = input("Digite o seu nome:")
mes = int(input("Digite o mês que você quer consultar:"))
dia = int(input("Digite o dia que você quer consultar:"))

if(mes == 1):
    print("Verão")
elif(mes == 2):
    print("Verão")
elif(mes == 3 and dia < 21):
    print("Verão")
elif(mes == 3 and dia >= 21):
    print("Outono")
elif(mes == 4):
    print("Outono")
elif(mes == 5):
    print("Outono")
elif(mes == 5 and dia < 21):
    print("Outono")
elif(mes == 5 and dia >= 21):
    print("Inverno")
elif(mes == 6):
    print("Inverno")
elif(mes == 7):
    print("Inverno")
elif(mes == 8):
    print("Inverno")
elif(mes == 9 and dia < 23):
    print("Inverno")
elif(mes == 9 and dia >= 23):
    print("Primavera")
elif(mes == 10):
    print("Primavera")
elif(mes == 11):
    print("Primavera")
elif(mes == 12 and dia < 21):
    print("Primavera")
elif(mes ==12 and dia >= 21):
    print("Verão")