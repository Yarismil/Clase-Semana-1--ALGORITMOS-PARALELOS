carrera= ["ISC","INF"]

nombre=input("Carrera selecciona:")
nombre.upper()
if nombre in carrera:
    print("Carrera Disponible")
else:
    print("Carrera no disponible en este recinto")