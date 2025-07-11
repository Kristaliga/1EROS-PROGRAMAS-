# LUIS FERNANDO ARELLANO MARTINEZ 250152
#PROGRAMA CALCULAR EL TIEMPO PROMEDIO EN EL QUE UNA PERSONA CORRE, EN LOS DIAS DETERMINADOS

print("Calcularemos el tiempo promedio en el que recorres la ruta")
lun= float(input("Cual fue tu tiempo el dia Lunes?: "))
mier= float(input("Cual fue tu tiempo el dia Miercoles?: "))
vie= float(input("Cual fue tu tiempo el dia Viernes?: "))

prom= lun+mier+vie/3

print(f"El tiempo promedio en esos 3 dias fue de: {prom:.2f}")

