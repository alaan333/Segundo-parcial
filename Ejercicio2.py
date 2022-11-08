# 2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios
# para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de 
# episodios en los que aparecieron juntos ambos personajes que se relacionan;
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
# c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia,
# Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
# e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los
# personajes.

from grafo import Grafo

grafo_starwars=Grafo(False)

# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de 
# episodios en los que aparecieron juntos ambos personajes que se relacionan;
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia,
# Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
grafo_starwars.insertar_vertice('Obi Wan Kenobi')
grafo_starwars.insertar_vertice('Boba Fett')
grafo_starwars.insertar_vertice('Darth Vader')
grafo_starwars.insertar_vertice('Luke Skywalker')
grafo_starwars.insertar_vertice('Yoda')
grafo_starwars.insertar_vertice('C 3PO')
grafo_starwars.insertar_vertice('Leia')
grafo_starwars.insertar_vertice('Rey')
grafo_starwars.insertar_vertice('Kylo Ren')
grafo_starwars.insertar_vertice('Chewbacca')
grafo_starwars.insertar_vertice('Han Solo')
grafo_starwars.insertar_vertice('R2 D2')
grafo_starwars.insertar_vertice('BB 8')

grafo_starwars.insertar_arista('Obi Wan Kenobi','Darth Vader',12)
grafo_starwars.insertar_arista('Obi Wan Kenobi','Luke Skywalker',30)
grafo_starwars.insertar_arista('Obi Wan Kenobi','Kylo Ren',5)
grafo_starwars.insertar_arista('Obi Wan Kenobi','Chewbacca',16)
grafo_starwars.insertar_arista('Obi Wan Kenobi','Leia',36)
grafo_starwars.insertar_arista('Boba Fett','BB 8',11)
grafo_starwars.insertar_arista('Boba Fett','R2 D2',15)
grafo_starwars.insertar_arista('Darth Vader','Rey',7)
grafo_starwars.insertar_arista('Darth Vader','Yoda',21)
grafo_starwars.insertar_arista('Darth Vader','Luke Skywalker',7)
grafo_starwars.insertar_arista('Luke Skywalker','Yoda',24)
grafo_starwars.insertar_arista('Luke Skywalker','Chewbacca',11)
grafo_starwars.insertar_arista('Yoda','Leia',18)
grafo_starwars.insertar_arista('Yoda','Rey',2)
grafo_starwars.insertar_arista('C 3PO','R2 D2',28)
grafo_starwars.insertar_arista('Leia','Kylo Ren',22)
grafo_starwars.insertar_arista('Rey','Han Solo',35)
grafo_starwars.insertar_arista('Chewbacca','Han Solo',18) 
grafo_starwars.insertar_arista('R2 D2','BB 8',20)
grafo_starwars.insertar_arista('Han Solo','R2 D2',3)

# b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
# arbol_min = grafo_starwars.kruskal()
# arbol_min = arbol_min[0].split('-')
# print(len(arbol_min))
# for nodo in arbol_min:
#     nodo = nodo.split(';')
#     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
# print()

# c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
grafo_starwars.comparten()
print()

# e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los
# personajes.
grafo_starwars.compartio_mayor_cantidad()