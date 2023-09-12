import re

busqueda = """Podrá nublarse el sol eternamente; 
Podrá secarse en un instante el mar; 
Podrá romperse el eje de la tierra 
como un débil cristal. 
¡todo sucederá! Podrá la muerte 
cubrirme con su fúnebre crespón; 
Pero jamás en mí podrá apagarse 
la llama de tu amor."""

podra = re.compile(r'\b(P|p)odrá\b')
# puede = podra.sub('Puede', busqueda)
# print(puede)
puede = podra.sub('Puede', busqueda, 2)
print(puede)