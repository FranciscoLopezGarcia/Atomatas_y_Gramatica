import re

busqueda = """Podrá nublarse el sol eternamente; 
Podrá secarse en un instante el mar; 
Podrá romperse el eje de la tierra 
como un débil cristal. 
¡todo sucederá! Podrá la muerte 
cubrirme con su fúnebre crespón; 
Pero jamás en mí podrá apagarse 
la llama de tu amor."""


patron = re.compile(r'\W+')
palabras = patron.split(busqueda)
palabras [:10]#Primeras 10 palabras

#print(palabras[:10])

#print(re.split(r'\n', busqueda ))#Version no compilada, separa por lineas

print(patron.split(busqueda, 5)) #Version compilada, separa por lineas, solo 5 veces