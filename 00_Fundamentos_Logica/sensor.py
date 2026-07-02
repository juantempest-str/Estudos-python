temperatura = float(input("Informe a temperatura atual do motor (em ºc): "))
if temperatura < 80:
    print("Status: Motor operando a frio ou aquecendo. ")
elif temperatura <= 100:
    print("Status: Temperatura ideal de trabalho. ")
else:
    temperatura > 100
    print("Status CRÍTICO: Superaquecimento. Desligue a máquina imediatamente!")
