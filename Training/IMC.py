peso = int(input("Peso (KG): "))
altura = float(input("Altura (Metros): "))

IMC = round((peso / altura**2), 1)

if IMC < 18.5:
    print("IMC: " + str(IMC) + " - Magreza")
elif IMC > 18.5 and IMC < 24.9:
    print("IMC: " + str(IMC) + " - Normal" )
elif IMC > 24.9 and IMC <  29.9:
    print("IMC: " + str(IMC) + " - Sobrepeso (Obesidade I)" )
elif IMC > 29.9 and IMC < 39.9:
    print("IMC: " + str(IMC) + " - Obesidade II" )
else:
    print("IMC: " + str(IMC) + " - Obesidade Grave III")


    



