# LUIS FERNANDO ARELLANO MARTINEZ 250152
#CALCULAR EL PROMEDIO DE CALIFICACIONES DE 3 MATERIAS

print("Calcularemos el promedio de tus calificaciones tomando en cuenta tus materias mas dificiles")

examat,t1mat,t2mat,t3mat = map(float, input("Ingresa la calificacion del Examen de Matematicas y las 3 tareas separandolas por espacio:\n").split())
exafis,t1fis,t2fis = map(float, input("Ingresa la calificacion del Examen de Fisica y las 2 tareas separandolas por espacio:\n").split())
exaqui,t1qui,t2qui,t3qui = map(float, input("Ingresa la calificacion del Examen de Quimica y las 3 tareas separandolas por espacio:\n").split())

protmat= (t1mat+t2mat+t3mat)/3
progmat= (examat*0.90)+(protmat*0.10)

protfis= (t1fis+t2fis)/2
progfis= (exafis*0.80)+(protfis*0.20)

protqui= (t1qui+t2qui+t3qui)/3
progqui= (exaqui*0.85)+(protqui*0.15)

progeneral= (progmat+progfis+progqui)/3

print("------RESULTADOS-----")
print(f"El promedio de Matematicas es: {progmat:.2f}")
print(f"El promedio de Fisica es: {progfis:.2f}")
print(f"El promedio de Quimica es: {progqui:.2f}")
print(f"Tu promedio general es de: {progeneral:.2f} ! Congratulations!🎉")