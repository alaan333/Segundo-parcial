# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de 
# personajes de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. Además deberá 
# contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
# e. mostrar un listado por nivel de los personajes del árbol;
# f. determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.

from arbol import (
    nodoArbol,
    insertar_nodo,
    modificar_info,
    busqueda,
    eliminar_nodo,
    inorden,
    inorden_altura_baja,
    inorden_peso,
    por_nivel
)

info_personajes=[
{'nombre':'qui-gon jin','altura':1.93, 'peso':76},
{'nombre':'obi-wan kenobi','altura':1.82, 'peso':75},
{'nombre':'anakin skywalker/darth vader','altura':1.88, 'peso':80},
{'nombre':'luke skywalker','altura':1.76, 'peso':77},
{'nombre':'yoda','altura':0.66, 'peso':33},
{'nombre':'mace windu','altura':1.88, 'peso':80},
{'nombre':'ki-adi-mundi','altura':1.98, 'peso':100},
{'nombre':'plo koon','altura':1.88, 'peso':86},
{'nombre':'saesee tiin','altura':1.88, 'peso':86},
{'nombre':'yaddle','altura':0.61, 'peso':38},
{'nombre':'incluso pieli','altura':1.22, 'peso':53},
{'nombre':'oppo rancisis','altura':1.38, 'peso':55},
{'nombre':'mandalorian','altura':1.84, 'peso':86},
{'nombre':'yarael poof','altura':2.64, 'peso':148},
{'nombre':'grogu','altura':1.71, 'peso':76},
{'nombre':'depa billaba','altura':1.68, 'peso':63},
{'nombre':'kit fisto','altura':1.96, 'peso':89},
{'nombre':'luminara unduli','altura':1.76, 'peso':73},
{'nombre':'barriss offee','altura':1.66, 'peso':67},
{'nombre':'shaak ti','altura':1.87, 'peso':80},
{'nombre':'coleman trebor','altura':2.13, 'peso':134},
{'nombre':'jocasta nu','altura':1.69, 'peso':70},
{'nombre':'aayla secura','altura':1.72, 'peso':81},
{'nombre':'sifo-dyas','altura':1.88, 'peso':95},
{'nombre':'conde dooku','altura':1.93, 'peso':103},
{'nombre':'pablo-jill','altura':1.60, 'peso':57},
{'nombre':'bultar cisne','altura':1.68, 'peso':64},
{'nombre':'agen kolar','altura':1.90, 'peso':93},
{'nombre':'stass allie','altura':1.80, 'peso':75}
]
class Datos_personajes:
    def __init__(self, nombre, altura, peso):
        self.nombre=nombre 
        self.altura=altura
        self.peso=peso
    def __str__(self):
        return f'{self.nombre}'

arbol_personajes=nodoArbol()

for i in info_personajes:
    insertar_nodo(arbol_personajes,i['nombre'].title(),Datos_personajes(i['nombre'].title(),
                                                i['altura'],
                                                i['peso']))
print()    

# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja; 
print('Seleccione una accion:')
print('1.Cargar nuevo')
print('2.Modifiar personaje')
print('3.Dar de baja')
c=input()
if c=='1':
    print('Ingrese los datos del nuevo personaje: ')
    nombre=input('Nombre: ').title()
    altura=input('Altura: ')
    peso=input('Peso: ')
    insertar_nodo(arbol_personajes,nombre,Datos_personajes(nombre.title(),peso,altura))
    print()
    inorden(arbol_personajes)
elif c=='2':
    dato=input('Ingrese personaje que desea modificar:').title()
    print()
    modificar_info(arbol_personajes,dato)
else:
    dato=input('Ingrese el personaje que desea dar de baja: ').title()
    if dato:
        eliminar_nodo(arbol_personajes,dato)
        print(f'{dato} se dio de baja')
    else:
        print('Personaje no encontrado')
print()

# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
pers=['Yoda','Mandalorian','Luke Skywalker']
for v in pers:
    buscado=busqueda(arbol_personajes,v)
    if buscado:
        print(buscado['datos'])
        print('Altura:',buscado['datos'].altura)
        print('Peso:',buscado['datos'].peso)
        print()
    else:
        print(f'{v} no esta en la lista')
print()

# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
print('Personajes que miden menos de 0.9')
inorden_altura_baja(arbol_personajes)
print()

# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
print('Personajes que pesan mas de 75 kilos')
inorden_peso(arbol_personajes)
print()

# e. mostrar un listado por nivel de los personajes del árbol;
print('Por nivel:')
por_nivel(arbol_personajes)
print()

# f. determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.
buscado=busqueda(arbol_personajes,'Grogu')
if buscado:
    print(buscado['datos'])
    print('Altura:',buscado['datos'].altura)
    print('Peso:',buscado['datos'].peso)
    if (buscado['altura']==arbol_personajes['altura']):
        print(f'Grogu esta hubicado en el nodo raiz')
    elif (buscado['izq']==None) and (buscado['der']==None):
        print(f'Grogu esta hubicado en un nodo hoja')
    elif (buscado['izq']!=None) or (buscado['der']!=None):
        print(f'Grogu esta hubicado en un nodo intermedio')
    print('Altura en la que se encuentra el nodo de Grogu:',buscado['altura'])
print()