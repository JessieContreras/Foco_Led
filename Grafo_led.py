'''En el presente codigo permite obtener el recorrido y el orden de los nodos del grafo,
mediante los vertices asignados en cada nodo, recordando que solo puede ser visitado una vez cada nodo
 indicando si el nodo es dirigido o no, cuando son dirigidos debe seguir su direcciín indicada'''

from queue import Queue
#Crea una función llamada gráfico.
class Grafico:
    #Crea objetos instanciando los atributos.
    def __init__(self, numero_de_nodos, dirigido=True):
        #Ingresa por medio de atributos el número de nodos.
        self.m_numero_de_nodos = numero_de_nodos
        #Ingresa el número de nodos mediante el rango usando el atributo número de nodos.
        self.m_nodos = range(self.m_numero_de_nodos)
        # Instancia el atributo dirigido.
        self.m_dirigido = dirigido
       
        #Se implementa una lista adyacente mediante un diccionario.
        '''Para agregar un diccionario tenemos como parámetro crear un objeto por lista agregando
        un bucle de recorrido que empieza de nodo=0 hasta el rango asignado'''
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos} 
        
        # Se agrega un constructor instanciado declarando como atributo dos nodos y el peso.
    '''Permite agregar los dos nodos y el peso de los bordes para cada nodo, verificando si el nodo es dirigido 
     o no, cuando el nodo es dirigido debe verificar que el siguiente tenga el permiso o la dirección correcta 
     para continuar al siguiente nodo, cuando no es dirigido puede ir por cualquier dirección'''
    def add_edge(self, nodo1, nodo2, weight=1):
        #Si el nodo1 es dirigido agrega un vertice del nodo1 al nodo2
        self.m_adj_lista[nodo1].add((nodo2, weight))
        # Cuando el nodo no está dirigido.
        if not self.m_dirigido:
            #Si el nodo2 no es dirigido agrega un vertice del nodo2 al nodo1
             self.m_adj_lista[nodo2].add((nodo1, weight))
    
    ''' Para imprimir la lista de los nodos y su peso de borde se debe agregar la instancia como atributo, 
    agregar un bucle de recorrido que permita imprimir la posición del nodo, con los respectivos datos 
    almacenados en el diccionario de la lista adyacente imprimiendo en el orden del primer nodo'''
    # Imprime la representación gráfica del atributo.
    def print_adj_lista(self):
        #Realiza un sentencia identificando el número de llaves que están conectadas al nodo.
        for llave in self.m_adj_lista.keys():
            #Imprime en orden el número de nodos ingresados con los datos almacenados en el diccionaro
            print("nodo", llave, ": ", self.m_adj_lista[llave])
             